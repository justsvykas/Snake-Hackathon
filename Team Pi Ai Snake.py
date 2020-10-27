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
ticksPerTurn = 10
windowWidth = 500
windowHeight = 500
up = (0,-1) 
down = (0,1)
left = (-1,0)
right = (1,0)

##
# The Human Snake
class humanSnake(object):
    pass

##
# The AI snake
class aiSnake(object):
    pass

##
# The food (Pie)
class pie(object):
    pass

##
# The game
def runGame():
    pygame.init() #Activates the pygame Library
    clock = pygame.time.Clock() #Used to keep game time
    window = pygame.display.set_mode((windowWidth, windowHeight))

    surface = pygame.Surface(window.get_size())
    surface = surface.convert()

    while(True):
        #Hold the loop for so many ticks
        clock.tick(ticksPerTurn)
        
        #Get users key stroke
        pass

        #Move Snake
        pass

        #If snake head is in food make the snake longer and respawn the food
        pass

        #If snake head is in wall or self end the game
        pass

        #Update the display
        pygame.display.update()

runGame()
