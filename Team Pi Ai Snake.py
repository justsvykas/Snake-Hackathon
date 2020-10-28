#!Python3
# Tested on Python 3.7.8 with pygame (pip3 install pygame)
# Team Pi's AI Snake for AUAI Hackathon AI
# With credits to:  Kiteco https://github.com/kiteco/python-youtube-code/tree/master/snake
#                   Edureka! https://www.edureka.co/blog/snake-game-with-pygame/

##
# Imports
import pygame
import random

##
# Variables
bgColour = (0, 0, 0)
hSnakeColour = (255, 255, 255)
foodColour = (255, 255, 255)
ticksPerTurn = 10
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
    def __init__(self):
        self.length = 1 #Set start length as 1
        self.pos = [((windowWidth * 0.4), (windowHeight * 0.5))] #Set initial position as left of middle
        self.direction = random.choice([up, down, left]) #Set starting direction as any way but right
        self.colour = hSnakeColour
        self.score = 0

    def get_head_pos(self):
        return self.pos[0] #Return the the first element in the list of body parts

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction: #Inverse the direction choice, don't let the snak eat its neck
            return
        else: #Update the snake direction
            self.direction = point

    def move(self):
        headPos = self.get_head_pos() #give headPos the x,y of the head
        x, y = self.direction #Assign -1, 0, or 1 to x, y
        newHead = ( ((headPos[0]+(x*gridSqSize))%windowWidth), ((headPos[1]+(y*gridSqSize))%windowHeight) )
        if newHead in self.pos: #If the new head will hit the snake
            self.reset()
        else:
            self.pos.insert(0,newHead) #Insert the new head at the begining of the pos list
            if len(self.pos) > self.length: #If the snake is longer than it should be pop off the tail
                self.pos.pop()


    def reset(self):
        self.length = 1 #Set start length as 1
        self.pos = [((windowWidth * 0.3), (windowHeight * 0.5))] #Set initial position as left of middle
        self.direction = random.choice([up, down, left]) #Set starting direction as any way but right
        self.score = 0

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
# The AI snake
class aiSnake():
    pass

##
# The food (Pie)
class pie():
    def __init__(self):
        self.pos = (0, 0) #Initial food spawn point
        self.colour = foodColour

    def random_pos(self):
        pass

    def draw(self, surface):
        pass

##
# The game

pygame.init() #Activates the pygame Library
clock = pygame.time.Clock() #Used to keep game time
window = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
pygame.display.set_caption('Snake by Team Pi')

surface = pygame.Surface(window.get_size())
surface = surface.convert()

# pie = pie()
humanSnake = humanSnake()
# aiSnake = aiSnake()

while(True):
    #Refresh the surface to black (This one took me a while to figure out)
    surface.fill(bgColour)

    #Hold the loop for so many ticks
    clock.tick(ticksPerTurn)
    
    #Get users key stroke
    humanSnake.checkKeyPress()

    #Move Snake
    humanSnake.move()

    #If snake head is in food make the snake longer and respawn the food
    pass

    #If snake head is in wall or self end the game
    pass

    #Draw elements
    humanSnake.draw(surface)

    #Pin the surface in the window (its the same size so top left corner 0,0)
    window.blit(surface, (0, 0))

    #Update the window display
    pygame.display.update()
