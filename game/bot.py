#Autor/en:  Lucas Voelz
#Version:   1.0

from weapon import Weapon
from player import Player
import pygame

RED = (255, 0, 0)

class Bot(Player):
    def __init__(self, nick = 'nick'):
        '''
        Initialisierung vom Bot
        Parameter:      -
        return values:  -
        '''
        Player.__init__(self, nick)
        self.image.fill(RED)
        self.nick = nick

    def shoot(self, xPosition, yPosition, eventPosition):
        '''
        Ueberschreibung vom Schuss, der bot soll momentan nichts machen
        Parameter:      int, xPosition
                        int, yPosition
                        Tuple (int, int), eventPosition
        return values:  -
        '''
        pass

    def update(self, gamemap):
        '''
        Ueberschreibung vom Update des Bots
        Parameter:      Spielobjekt, gamemap
        return values:  -
        '''
        pass
