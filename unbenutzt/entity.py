# -*- coding: cp1252 -*-
#Datum :    09-14.12.16
#Autor/en:  Lucas V.
#Version:   1.0

import pygame

'''
Player und Bullet erben von der Klasse
'''


class Entity():
    def __init__(self, rect = (0, 0, 0, 0), speed = 1):
        '''
        Initialisation von Entity
        Parameter:      rect
                            int mit der distanz nach links
                            int mit der disanz nach oben
                            int width von dem Objekt
                            int heigth von dem Objekt
                        speed
                            Float, speed vom Objekt (Bewegungsgeschwindigkeit)
        return values:  -
        '''
        self.rect = pygame.Rect(rect)
        self.speed = speed
        

##################### Getters und Setters, die momentan nirgends gebraucht werden, aber dazu gehoeren #####################

    def getSize(self):
        '''
        gibt breite und hoehe des Objektes wieder
        Parameter:      -
        return values:  size
                            int width von dem Objekt
                            int height von dem Objekt
        '''
        return self.rect[2], self.rect[3]

    def setSize(self, width, height):
        '''
        gibt breite und hoehe des Objektes wieder
        Parameter:      size
                            int width von dem Objekt
                            int height von dem Objekt
        return values:  -
        '''
        self.rect = pygame.Rect(self.rect[0], self.rect[1], width, height)

    def getRect(self):
        '''
        gibt position, breite und hoehe des Objektes aus
        Parameter:      -
        return values:  rect
                            int x-Koordinate des Objektes
                            int y-Koordinate des Objektes
                            int width des Objektes
                            int height des Objektes
        '''
        return self.rect
    
    def setRect(self, xCoord, yCoord, width, height):
        '''
        setzt position, breite und hoehe des Objektes
        Parameter:      int x-Koordinate des Objektes
                        int y-Koordinate des Objektes
                        int width des Objektes
                        int height des Objektes
        return Values   -
        '''
        self.rect = pygame.Rect(xCoord, yCoord, width, height)
 
    def getPosition(self):
        '''
        gibt position des Objektes aus
        Parameter:      int x-Koordinate des Objektes
                        int y-Koordinate des Objektes
        return values:  -
        '''
        return self.rect[0], self.rect[1]

    def setPosition(self, x, y):
        '''
        gibt position des Objektes aus
        Parameter:      -
        return values:  int x-Koordinate des Objektes
                        int y-Koordinate des Objektes
        '''
        self.rect = pygame.Rect(x, y, self.rect[2], self.rect[3])
    
    def getXPos(self):
        '''
        gibt x-Koordinate des Objektes aus
        Parameter:      -
        return values:  int x-Koordinate des Objektes
        '''
        return self.rect[0]
    
    def getYPos(self):
        '''
        gibt y-Koordinate des Objektes aus
        Parameter:      -
        return values:  int y-Koordinate speed des Objektes
        '''
        return self.rect[1]

        
    def getSpeed(self):
        '''
        gibt Geschwindigkeit des Objektes aus
        Parameter:      -
        return values:  float speed des Objektes
        '''
        return self.speed
    
    def setSpeed(self, speed):
        '''
        setzt die Geschwindigkeit des Objektes
        Parameter:      float speed des Objektes
        return values:  -
        '''
        self.speed = speed
