# -*- coding: cp1252 -*-
#Datum :    07.12.16
#Autor/en:  Lucas V.
#Version:   1.0

from sectorialdivision import SectorialDivision
from entity import Entity
import math

class Bullet(Entity):
    def __init__(self, rect = (0, 0, 1, 2), speed = 1, damage = 2):
        '''
        Initialisation von Bullet
        Parameter:      rect
                            int mit der distanz nach links
                            int mit der disanz nach oben
                            int width von dem Objekt
                            int heigth von dem Objekt
                        Flaot speed von der Bullet (Bewegungsgeschwindigkeit)
                        Flaot damage von der Bullet
        return values:  -
        '''
        Entity.__init__(self, rect, speed)
        self.dmg = damage
        self.__pixelLength = 10 #Int
        self.__r = self.__pixelLength / math.hypot(direction[0], direction[1]) #Int / (Int^2 + Int^2) 
        #r * |direction| = pixelLength --> r = pixelLength / |direction| --> r * |direction| kann alle 10 pixel (self.__pixelLength) berechnet werden
        ##|direction| = directionlaenge in Pixel        
        
    def move(self):
        '''
        berechnet & setzt die naechste position der Bullet
        Parameter:      -
        return values:  -
        '''
        x = self.rect[0] #Int
        y = self.rect[1] #Int
        directionX = self.direction[0] #Int
        directionY = self.direction[1] #Int  
        newXPosition = x + self.__r * directionX * self.speed #Int + float * Int * float
        newYPosition = y + self.__r * directionY * self.speed #Int + float * Int * float
        
        self.rect[0] = int(newXPosition)
        self.rect[1] = int(newYPosition)
        
##################### Getters und Setters, die momentan nirgends gebraucht werden, aber dazu gehoeren #####################
        
    def getDamage(self):
        '''
        gibt dem den Schaden der Bullet aus
        Parameter:      -
        return values:  Float damage der Bullet
        '''
        return self.dmg
    
    def setDamage(self, dmg):
        '''
        setzt den Schaden des Objektes Bullet
        Parameter:      Float damage
        return values:  -
        '''
        self.dmg = dmg
