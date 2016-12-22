#Autor/en:  Niclas, Gregor
#Datum:     ????
#Version:   1.0

import pygame
import math

BLACK = (0, 0, 0)
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        """
        Initialisierung der Klasse Bullet
        Parameter:      -
        return value:   -
        """ 
        super(Bullet,self).__init__()# Call the parent class (Sprite) constructor
        
        self.vector=(0,0)
        self.image = pygame.image.load("ball2.png")#pygame.Surface([4, 10])
        #self.image.fill(BLACK)
        self.rect = self.image.get_rect()

    def updateVector(self, vec):
        '''
        updatet den Vektor
        Parameter:      -
        return values:  -
        '''
        self.vector = vec

    def lenVector(self):
        '''
        errechnet die laenge des Vektors mit hypot
        Parameter:      -
        return values:  -
        '''
        return math.hypot(self.vector[0], self.vector[1])

        
    def adjustVector(self):
        '''
        Gleicht den Vektor an, sodass die Kugel nicht schneller wird, wenn sie weiter vom Spieler entfernt ist.
        Paramter : -
        Rueckgabewerte: (x,y) (angepasster Vektor)
        '''
        #muss n mal aufgerugen werden, soll, wenn es gegen eine Wand, hinderniss etc. fliegt
        length = self.lenVector()
        try:
            x = (self.vector[0] / (length /10)) #5 Geschwindigkeit des Schusses
            y = (self.vector[1] / (length /10))
            return ((x+(length/100)),(y+(length/100)))
        except:
            return self.vector

        
 
    def update(self):
        '''
        Bewegt die Kugel, benutzt dabei den Vektor, der mit adjustVektor angepasst wurde.
        Paramter : -
        Rueckgabewerte: -
        '''
        newVec = self.adjustVector()
        self.rect.y += newVec[1]
        self.rect.x += newVec[0]
        
        #bullet.move_ip(vector)
