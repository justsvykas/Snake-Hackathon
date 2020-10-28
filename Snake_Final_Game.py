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
from AI_Snake_Function import aiSnakeController

##
# Variables
ticksPerTurn = 10
windowWidth = 500
windowHeight = 500

gridsize = 20                                     #rect size
grid_width = windowWidth / gridsize              #number of rect on x axis
grid_height = windowHeight / gridsize             #number of rect on y axis

up = (0,-1) 
down = (0,1)
left = (-1,0)
right = (1,0)

white = (255, 255, 255)
red = (255, 0, 0)
pygame.init()
window = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
font_style = pygame.font.SysFont(None, 30)

##
# The Human Snake
class HumanSnake():
    def __init__(self):
        self.length = 1
        self.positions = [((windowWidth * 0.6), (windowHeight * 0.4))]    #starts slight right
        self.direction = random.choice([up, down, right])         #points in random direction
        self.color = (17, 24, 47)
        self.score = 0
        
    def get_head_position(self):
        return self.positions[0]           #updates where the snake is

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:      #if snake length is more than 1 it can go just in 3 directions 
            return
        else:
            self.direction = point
        

    
    def move(self):
        cur = self.get_head_position()  
        x, y = self.direction             #current direction of a snake
        new = (((cur[0] + (x * gridsize)) % windowWidth), (cur[1] + (y * gridsize)) % windowHeight)  #new position of snake
        if len(self.positions) > 2 and new in self.positions[2:]:      #if snake touches itself gameover
            #self.reset()
            gameover = True
            while(gameover == True):
                window.fill(white)
                message("You Lost! Press Q-Quit or C-Play Again", red)
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
            self.positions.insert(0, new)             #else we will reposition snake
            if len(self.positions) > self.length:
                self.positions.pop()                  

    def reset(self):                                              #this is where we should write game over screen
        self.length = 1
        self.position = [((windowWidth / 2), (windowHeight / 2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)               #we will draw rect of snake head
            pygame.draw.rect(surface, (93, 216, 228), r, 1)        #draw the rest of body

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:        #player wants to quit
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:        #if player pressed Keys turn snake acordingly
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
class aiSnake():
    def __init__(self):
        self.length = 1
        self.positions = [((windowWidth * 0.4), (windowHeight * 0.4))]    #starts slight left 
        self.direction = random.choice([up, down, left])         #points in random direction
        self.color = (17, 24, 47)
        self.score = 0
        
    def get_head_position(self):
        return self.positions[0]           #updates where the snake is

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:      #if snake length is more than 1 it can go just in 3 directions 
            return
        else:
            self.direction = point
        

    
    def move(self):
        cur = self.get_head_position()  
        x, y = self.direction             #current direction of a snake
        new = (((cur[0] + (x * gridsize)) % windowWidth), (cur[1] + (y * gridsize)) % windowHeight)  #new position of snake
        if len(self.positions) > 2 and new in self.positions[2:]:      #if snake touches itself gameover
            #self.reset()
            gameover = True
            while(gameover == True):
                window.fill(white)
                message("You Lost! Press Q-Quit or C-Play Again", red)
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
            self.positions.insert(0, new)             #else we will reposition snake
            if len(self.positions) > self.length:
                self.positions.pop()                  

    def reset(self):                                              #this is where we should write game over screen
        self.length = 1
        self.position = [((windowWidth / 2), (windowHeight / 2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)               #we will draw rect of snake head
            pygame.draw.rect(surface, (93, 216, 228), r, 1)        #draw the rest of body



##
# The food (Pie)
class Pie():
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width - 1) * gridsize, random.randint(0, grid_height - 1) * gridsize)  #randomly position food

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))   #draw a rect of food in randomized position
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if(x + y) % 2 == 0:
                r = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))     
                pygame.draw.rect(surface, (93, 216, 228), r)                           #Draws a rect on even coordinates
            else:
                rr = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                pygame.draw.rect(surface, (84, 194, 205), rr)                          #Draws even darker rect on odd coordinates

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [windowWidth/3, windowHeight/3])


##
# The game
def runGame():
    #pygame.init() #Activates the pygame Library
    clock = pygame.time.Clock() #Used to keep game time
    #window = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)

    surface = pygame.Surface(window.get_size())
    surface = surface.convert()

    gameover = False
    
    drawGrid(surface)                         
    
    humanSnake = HumanSnake()                       #humanSake class obj
    pie = Pie()                               #Pie class obj

    myfont = pygame.font.SysFont("monospace", 16)  #introduce kind of text

    while(True):
        
        #Hold the loop for so many ticks
        clock.tick(ticksPerTurn)
        
        #Get users key stroke
        humanSnake.handle_keys() 

        #Repaint the window so it would be clear of previous snake movements
        drawGrid(surface)                  

        #Move Snake
        humanSnake.move()                              

        #If snake head is in food make the snake longer and respawn the food
        if humanSnake.get_head_position() == pie.position:
            humanSnake.length += 1
            humanSnake.score += 1
            pie.randomize_position()

        #If snake head is in wall or self end the game
        

        #Draw snake
        humanSnake.draw(surface)

        #Draw food
        pie.draw(surface)

        #Overlays main screen with event
        window.blit(surface, (0, 0))

        #Create text of score
        text = myfont.render("Score {0}".format(humanSnake.score), 1, (0, 0, 0))  
        window.blit(text, (5, 10))

        #Update the display
        pygame.display.update()
    

runGame()
