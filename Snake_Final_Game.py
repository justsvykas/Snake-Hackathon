#!Python3
# Tested on Python 3.7.8 with pygame (pip3 install pygame)
# Team Pi's AI Snake for AUAI Hackathon AI
# With credits to:  Kiteco https://github.com/kiteco/python-youtube-code/tree/master/snake
#                   Edureka! https://www.edureka.co/blog/snake-game-with-pygame/

##
# Imports
import pygame
import random
import sys

##
# Variables
ticksPerTurn = 10
windowWidth = 500
windowHeight = 500

gridsize = 20                                     #rect size
grid_width = windowWidth / gridsize               #number of rect on x axis
grid_height = windowHeight / gridsize             #number of rect on y axis

up = (0,-1) 
down = (0,1)
left = (-1,0)
right = (1,0)

silver = (192, 192, 192)                          #RGB based so (more light bigger number,     ,     )
gray = (128, 128, 128)
dimGray = (105, 105, 105)
white = (255, 255, 255)
red = (255, 0, 0)
mediumBlue = (0, 0, 205)
dodgerBlue = (30, 144, 255)
crimson = (220, 20, 60)
indianRed = (205, 92, 92)
limeGreen = (50, 205, 50)
lime = (0, 255, 0)
black = (0, 0, 0)

pygame.init()
window = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
font_YouDied = pygame.font.SysFont('Helvetica', 110)
font_PlayAgain = pygame.font.SysFont('Verdana', 20)
##
# The Human Snake
class HumanSnake():
    def __init__(self):
        self.length = 1
        self.positions = [((windowWidth * 0.6), (windowHeight * 0.4))]    #starts slight right
        self.direction = random.choice([up, down, right])         #points in random direction
        self.color = indianRed
        self.score = 0
        
    def get_head_position(self):
        return self.positions[0]                                                  #updates where the snake is

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:      #if snake length is more than 1 it can go just in 3 directions 
            return
        else:
            self.direction = point
        

    
    def move(self, aiS):
        cur = self.get_head_position()  
        x, y = self.direction                                                                        #current direction of a snake
        new = (((cur[0] + (x * gridsize)) % windowWidth), (cur[1] + (y * gridsize)) % windowHeight)  #new position of snake
        if (len(self.positions) > 2 and new in self.positions[2:]) or new in aiS: #if snake touches a snake game over
            gameover = True
            while(gameover == True):
                surfaceLocal = pygame.Surface(window.get_size())
                surfaceLocal = surfaceLocal.convert()
                window.fill(white)
                #drawMeniu(surfaceLocal)
                message("YOU DIED!", red)
                message2("Please press q - to quit c - to try again", red)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            #gameClose = True
                            pygame.quit
                            sys.exit()
                        if event.key == pygame.K_c:
                            runGame()
        else:
            self.positions.insert(0, new)                         #else we will reposition snake
            if len(self.positions) > self.length:
                self.positions.pop()                  

    def reset(self):                                               #this is where we should write game over screen
        self.length = 1
        self.positions = [((windowWidth * 0.6), (windowHeight * 0.4))]    #starts slight right
        self.direction = random.choice([up, down, right])         #points in random direction\
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)               #we will draw rect of snake head
            pygame.draw.rect(surface, crimson, r, 2)        #draw the rest of body

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                          #player wants to quit
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:                     #if player pressed Keys turn snake acordingly
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)

##
# The AI snake
class AISnake():
    def __init__(self):
        self.length = 1
        self.positions = [((windowWidth * 0.4), (windowHeight * 0.4))]    #starts slight left 
        self.direction = random.choice([up, down, left])         #points in random direction
        self.color = dodgerBlue
        self.score = 0
        
    def get_head_position(self):
        return self.positions[0]           #updates where the snake is

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:      #if snake length is more than 1 it can go just in 3 directions 
            return
        else:
            self.direction = point
        

    
    def move(self,hS):
        cur = self.get_head_position()  
        x, y = self.direction             #current direction of a snake
        new = (((cur[0] + (x * gridsize)) % windowWidth), (cur[1] + (y * gridsize)) % windowHeight)  #new position of snake
        if (len(self.positions) > 2 and new in self.positions[2:]) or new in hS: #if snake touches a snake game over
            #self.reset()
            gameover = True
            while(gameover == True):
                window.fill(white)
                message("YOU WIN!", red)
                message2("Please press q - to quit c - to try again", red)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit
                            sys.exit()
                        if event.key == pygame.K_c:
                            runGame()
        else:
            self.positions.insert(0, new)             #else we will reposition snake
            if len(self.positions) > self.length:
                self.positions.pop()                  

    def reset(self):                                              #this is where we should write game over screen
        self.length = 1
        self.positions = [((windowWidth * 0.4), (windowHeight * 0.4))]    #starts slight left 
        self.direction = random.choice([up, down, left])         #points in random direction\
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)               #we will draw rect of snake head
            pygame.draw.rect(surface, mediumBlue, r, 2)        #draw the rest of body
    
    def aiSnakeController(self,hS,pi):
        aiHeadX, aiHeadY = self.get_head_position() #Assign coordinates for ai head
        piX, piY = pi #Assign coordinates for Pie

        disX = aiHeadX - piX #Distance to Pie on x axis, pos int left, neg int right
        disY = aiHeadY - piY #Distance to Pie on y axis, pos int up, neg int down

        #Set direction priority list for snake
        if (disY >= 0) and (disX <= 0): #If Pie is NE of Snake
            if abs(disY) > abs(disX): #If more north than east
                directionPriority = [up, right, left, down]
            else:
                directionPriority = [right, up, down, left]

        elif (disY <= 0) and (disX <= 0): #If Pie is SE of Snake
            if abs(disY) > abs(disX): #If more south than east
                directionPriority = [down, right, left, up]
            else:
                directionPriority = [right, down, up, left]

        elif (disY <= 0) and (disX >= 0): #If Pie is SW of Snake
            if abs(disY) > abs(disX): #If more south than west
                directionPriority = [down, left, right, up]
            else:
                directionPriority = [left, down, up, right]

        elif (disY >= 0) and (disX >= 0): #If Pie is NW of Snake
            if abs(disY) > abs(disX): #If more north than west
                directionPriority = [up, left, right, down]
            else:
                directionPriority = [left, down, up, right]

        #check direction priorities for the first that doesn't collide
        for i in range(4):
            x, y = directionPriority[i]
            newHead = (((aiHeadX + (x * gridsize)) % windowWidth), (aiHeadY + (y * gridsize)) % windowHeight)  #new position of snake
            if (newHead not in self.positions) and (newHead not in hS): #if snake doesnt touch itself of other player were good
                self.turn(directionPriority[i])
                return

##
# The food (Pie)
class Pie():
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position((0,0),(0,0))

    def randomize_position(self, hS, aiS):
        while (self.position == (0, 0)) or (self.position in hS) or (self.position in aiS): #Position food till its not in a snake
            self.position = (random.randint(0, grid_width - 1) * gridsize, random.randint(0, grid_height - 1) * gridsize)  #randomly position food

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))   #draw a rect of food in randomized position
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 2)


def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if(x + y) % 2 == 0:
                r = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))     
                pygame.draw.rect(surface, gray, r)                           #Draws a rect on even coordinates
            else:
                rr = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, dimGray, rr)                          #Draws even darker rect on odd coordinates

#   for y in range(0, int(grid_height)):
#        for x in range(0, int(grid_width)):
#            if(y == 0 or y == grid_width):
#                r = pygame.Rect((y * gridsize, x * gridsize ), (gridsize, gridsize))
#                pygame.draw.rect(surface, (93, 216, 228), r)
#            elif(x == 0 or x == grid_width):
#                rr = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
#                pygame.draw.rect(surface, (93, 216, 228), rr)   

def drawIntro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameover = True
        while(gameover == True):
            window.fill(white)
            message("Get Ready!", red)
            #message2("MENU", red)         #(x axis, y axix, x axis rect side, y axis rect side)

            button("AI vs Hu", 180, 200, 150, 40, limeGreen, lime, "B")
            button("Watch AI", 180, 270, 150, 40, limeGreen, lime, "A")
            button("Just Hu", 180, 350, 150, 40, limeGreen, lime, "H")
            button("QUIT", 180, 420, 150, 40, crimson, red, "Q")

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit
                        sys.exit()
                    if event.key == pygame.K_s:
                        runGame()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ac, ic, action = None):  #msg- message, x - yaxis, y - xaxis, w - rect width, h - rect height, ic - darker color, ac - lighter color
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:             #mouse[0]== x axis mouse[1]== y axis
        pygame.draw.rect(window, ic, (x, y, w, h))                #!= not equal
        if click[0] == 1 and action == "B":
            runGame(action)
        elif click[0] == 1 and action == "A":
            runGame(action)
        elif click[0] == 1 and action == "H":
            runGame(action)
        elif click[0] == 1 and action == "Q":
            quitGame()
                                                           #click(0, 0, 0) first position = (1, 0, 0)
    else:
        pygame.draw.rect(window, ac, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w/2)), (y + (h/2)))  #(X axis, Y axis)
    window.blit(textSurf, textRect)


def message(msg, color):
    mesg = font_YouDied.render(msg, True, color)
    window.blit(mesg, [windowWidth/20, windowHeight/7])

def message2(msg, color):
    mesg = font_PlayAgain.render(msg, True, color)
    window.blit(mesg, [windowWidth / 2, windowHeight / 1.5])

def quitGame():
    pygame.quit()
    quit()


##
# The game
def runGame(gMode="B"): #Gamemode "B"oth, "A"i, or "H"uman

    clock = pygame.time.Clock()                          #Used to keep game time

    surface = pygame.Surface(window.get_size())
    surface = surface.convert()
    
    drawGrid(surface)                         
 
    aiSnake = AISnake()
    humanSnake = HumanSnake()                            #humanSake class obj

    if gMode == "A": #If AI
        humanSnake.positions = (-100, -100)

    if gMode == "H": #If Human
        aiSnake.positions = (-100, -100)
    
    pie = Pie()                                          #Pie class obj

    myfont = pygame.font.SysFont("monospace", 16)        #introduce kind of text

    while(True):
        
        #Hold the loop for so many ticks
        clock.tick(ticksPerTurn)

        #Repaint the window so it would be clear of previous snake movements
        drawGrid(surface) 

        #Human key input incase of exit
        humanSnake.handle_keys()

        if gMode == "H" or gMode == "B": #If Human
            #Get users key stroke and move the snake
            humanSnake.move(aiSnake.positions)
            #Draw snake
            humanSnake.draw(surface)
                 
        if gMode == "A" or gMode == "B": #If AI
            #Ask the AI which way to go and move the AI Snake (Second to give the human the advantage)
            aiSnake.aiSnakeController(humanSnake.positions,pie.position)
            aiSnake.move(humanSnake.positions)
            #Draw snake
            aiSnake.draw(surface)

        #If snake head is in food make the snake longer and respawn the food
        if (gMode == "H" or gMode == "B") and humanSnake.get_head_position() == pie.position: #Human
            humanSnake.length += 1
            humanSnake.score += 1
            pie.randomize_position(humanSnake.positions,aiSnake.positions)
        
        elif (gMode == "A" or gMode == "B") and aiSnake.get_head_position() == pie.position: #AI
            aiSnake.length += 1
            aiSnake.score += 1
            pie.randomize_position(humanSnake.positions,aiSnake.positions)

        #Draw food
        pie.draw(surface)

        #Overlays main screen with event
        window.blit(surface, (0, 0))

        #Create text of score
        text = myfont.render("Your Score {0} | AI Score {1}".format(humanSnake.score,aiSnake.score), 1, (0, 0, 0))  
        window.blit(text, (5, 10))

        #Update the display
        pygame.display.update()
    
drawIntro()