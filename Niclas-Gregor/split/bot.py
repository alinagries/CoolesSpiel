#Autor/en:  Niclas, Gregor
#Datum:     ????
#Version:   1.0

from screen import Screen
from player import Player
import pygame

GREEN = (0, 255, 0)
RED = (255, 0, 0)
screensize = Screen().screensize
screenWidth = screensize[0]
screenHeight = screensize[1]
screen = pygame.display.set_mode([screenWidth, screenHeight])

class Bot(Player):
    def __init__(self, nick = 'nick'):
        '''
        Initialisierung vom Player1
        Parameter:      -
        return values:  -
        '''
        Player.__init__(self, nick)
        self.image.fill(RED)

    def update(self):
        pass