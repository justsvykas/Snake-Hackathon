#!Python3
# Tested on Python 3.7.8 with pygame (pip3 install pygame)
# Team Pi's AI Snake for AUAI Hackathon AI
# With credits to:  Kiteco https://github.com/kiteco/python-youtube-code/tree/master/snake
#                   Edureka! https://www.edureka.co/blog/snake-game-with-pygame/

##
# Imports
import pygame
import random
from AI_Snake_Function import aiSnakeController

##
# Variables
bgColour = (0, 0, 0)
hSnakeColour = (255, 255, 255)
aiSnakeColour = (0, 150, 50)
foodColour = (255, 255, 255)
fps = 10
windowWidth = 400
windowHeight = 300
gridSqSize = 10 #How large the squares are
gridWidth = windowWidth / gridSqSize
gridHeight = windowHeight / gridSqSize

up = (0,-1) 
down = (0,1)
left = (-1,0)
right = (1,0)

##
# The Human Snake
class humanSnake():
    def __init__(self): #Initial humansnake() values
        self.length = 1 #Set start length as 1
        self.pos = [((windowWidth * 0.4), (windowHeight * 0.5))] #Set initial position as left of middle
        self.direction = random.choice([up, down, left]) #Set starting direction as any way but right
        self.colour = hSnakeColour

    def getHeadPos(self):
        return self.pos[0] #Return the the first element in the list of body parts

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction: #Inverse the direction choice, don't let the snak eat its neck
            return
        else: #Update the snake direction
            self.direction = point

    def move(self):
        headPos = self.getHeadPos() #give headPos the x,y of the head
        x, y = self.direction #Assign -1, 0, or 1 to x, y
        newHead = ( ((headPos[0]+(x*gridSqSize))%windowWidth), ((headPos[1]+(y*gridSqSize))%windowHeight) )
        if newHead in self.pos or newHead in aiSnake.pos: #If the new head will hit the snake
            pygame.time.wait(2000) #Wait 2 Sec
            self.reset()
        else:
            self.pos.insert(0,newHead) #Insert the new head at the begining of the pos list
            if len(self.pos) > self.length: #If the snake is longer than it should be pop off the tail
                self.pos.pop()


    def reset(self):
        self.length = 1 #Set start length as 1
        self.pos = [((windowWidth * 0.5), (windowHeight * 0.5))] #Reset pos to the middle
        self.direction = random.choice([up, down, left, right]) #Set starting direction as any

    def draw(self, surface):
       for p in self.pos: #Run for each possition of the snake
           r = pygame.Rect( (p[0], p[1]), (gridSqSize, gridSqSize) ) #Create a square in position
           pygame.draw.rect(surface, self.colour, r) #Draw that square on the surface

    def checkKeyPress(self):
        for event in pygame.event.get(): #For events in the last clock cycle
            if event.type == pygame.KEYDOWN: #If the user pressed a key
                if event.key == pygame.K_UP:
                    self.turn(up)
                if event.key == pygame.K_DOWN:
                    self.turn(down)
                if event.key == pygame.K_LEFT:
                    self.turn(left)
                if event.key == pygame.K_RIGHT:
                    self.turn(right)

##
# The AI Snake
class aiSnake():
    def __init__(self): #Initial humansnake() values
        self.length = 1 #Set start length as 1
        self.pos = [((windowWidth * 0.6), (windowHeight * 0.5))] #Set initial position as right of middle
        self.direction = random.choice([up, down, right]) #Set starting direction as any way but left
        self.colour = aiSnakeColour

    def getHeadPos(self):
        return self.pos[0] #Return the the first element in the list of body parts

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction: #Inverse the direction choice, don't let the snak eat its neck
            return
        else: #Update the snake direction
            self.direction = point

    def move(self):
        headPos = self.getHeadPos() #give headPos the x,y of the head
        x, y = self.direction #Assign -1, 0, or 1 to x, y
        newHead = ( ((headPos[0]+(x*gridSqSize))%windowWidth), ((headPos[1]+(y*gridSqSize))%windowHeight) )
        if newHead in self.pos or newHead in humanSnake.pos: #If the new head will hit the snake
            pygame.time.wait(2000) #Wait 2 Sec
            self.reset()
        else:
            self.pos.insert(0,newHead) #Insert the new head at the begining of the pos list
            if len(self.pos) > self.length: #If the snake is longer than it should be pop off the tail
                self.pos.pop()


    def reset(self):
        self.length = 1 #Set start length as 1
        self.pos = [((windowWidth * 0.5), (windowHeight * 0.5))] #Reset pos to the middle
        self.direction = random.choice([up, down, left, right]) #Set starting direction as any

    def draw(self, surface):
       for p in self.pos: #Run for each possition of the snake
           r = pygame.Rect( (p[0], p[1]), (gridSqSize, gridSqSize) ) #Create a square in position
           pygame.draw.rect(surface, self.colour, r) #Draw that square on the surface

##
# The food (Pie)
class pie():
    def __init__(self): #Initial pie() values
        self.pos = (0, 0)
        self.colour = foodColour
        self.randomPos()

    def randomPos(self):
        while (self.pos == (0, 0)) or (self.pos in humanSnake.pos) or (self.pos in aiSnake.pos): #reposition Pie if in either snake or first run (0,0)
            self.pos = ( (random.randint(0, gridWidth-1) * gridSqSize) , (random.randint(0, gridHeight-1) * gridSqSize) ) #Possition somewhere random on the grid

    def draw(self, surface):
        r = pygame.Rect( (self.pos[0], self.pos[1]), (gridSqSize, gridSqSize) ) #Create a square in position
        pygame.draw.rect(surface, self.colour, r) #Draw that square on the surface

##
# The game
pygame.init() #Activates the pygame Library
clock = pygame.time.Clock() #Used to keep game time
window = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
pygame.display.set_caption('Snake by Team Pi')

surface = pygame.Surface(window.get_size())
surface = surface.convert()

humanSnake = humanSnake() #Starts the Human Snake
aiSnake = aiSnake() #Starts the AI Snake
pie = pie() #Adds the Pie (has to come after players added, otherwise can't avoid them)

while(True):
    
    

    #Should hold the loop a division of frames in a decond 10th of a sec etc. 
    clock.tick(fps)
    
    #Get users key stroke and move the snake
    humanSnake.checkKeyPress()
    humanSnake.move()

    #Ask the AI which way to go and move the AI Snake (Second to give the human the advantage)
    aiSnake.turn(aiSnakeController(aiSnake.pos,humanSnake.pos,pie.pos))
    aiSnake.move()

    #If snake head is in food make the snake longer and respawn the food
    if aiSnake.getHeadPos() == pie.pos:
        print("AI Got Pie!")
        aiSnake.length += 1
        pie.randomPos()
    
    if humanSnake.getHeadPos() == pie.pos:
        print("Human Got Pie!")
        humanSnake.length += 1
        pie.randomPos()

    #If snake head is in wall end the game
    pass

    #Refresh the surface to black (This one took me a while to figure out) and draw elements
    surface.fill(bgColour)
    humanSnake.draw(surface)
    aiSnake.draw(surface)
    pie.draw(surface)

    #Pin the surface in the window (its the same size so top left corner 0,0)
    window.blit(surface, (0, 0))

    #Update the window display
    pygame.display.update()
