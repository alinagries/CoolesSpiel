# -*- coding: cp1252 -*-
#Datum :    07-14.12.16
#Autor/en:  Lucas V.
#Version:   1.0

from entity import Entity
import math

'''
Ein Bullet ist eine Kugel mit einer Position, Bewegungsrichtung, Geschwindigkeit und Schaden.
Ein Bullet wird immer von einer Waffe erzeugt
'''

'''
Todo:
 -eine an und abmeldeautomatik fuer Sektoren (in arbeit)
'''
 
class Bullet(Entity):
    def __init__(self, rect = (0, 0, 1, 2), direction = (1, 1), speed = 1, damage = 2):
        Entity.__init__(self, rect, direction, speed)
        self.dmg = damage
        self.__pixelLength = 10 #Int
        self.__r = self.__pixelLength / math.hypot(direction[0], direction[1]) #Int / (Int^2 + Int^2) 
        #r * |direction| = pixelLength --> r = pixelLength / |direction| --> r * |direction| kann alle 10 pixel (self.__pixelLength) berechnet werden
        ##|direction| = directionlaenge in Pixel        
        
        
    def move(self):
        #setzt die Kugel __r * speed pixel in Vektorrichtung weiter
        x = self.rect[0] #Int
        y = self.rect[1] #Int
        directionX = self.direction[0] #Int
        directionY = self.direction[1] #Int  
        newXPosition = x + self.__r * directionX * self.speed #Int + float * Int * float
        newYPosition = y + self.__r * directionY * self.speed #Int + float * Int * float
        
        self.rect[0] = int(newXPosition)
        self.rect[1] = int(newYPosition)
        
    def getDamage(self):#Int
        return self.dmg
    
#    def setDamage(self, dmg): #Int
#        self.dmg = dmg
