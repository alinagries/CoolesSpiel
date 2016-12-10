# -*- coding: cp1252 -*-
#Datum :    07.12.16
#Autor/en:  Lucas V.
#Version:   1.0

from entity import Entity
import math

'''
Ein Bullet ist eine Kugel mit einer Position, Bewegungsrichtung, Geschwindigkeit und Schaden.
Ein Bullet wird immer von einer Waffe erzeugt
'''
 
class Bullet(Entity):
    def __init__(self, rect = ((0, 0), (2, 5)), direction = (0, 0), speed = 1, damage = 2):
        self = super.__init__(rect, direction, speed)
        self.dmg = damage
        self.__pixelLength = 10
 
    def move(self):
        '''
        Ziel: der Schuss soll nach 10p berechnet werden
        Position = (x, y)
        direction = (n, m)
        |direction| = direction in Pixel
        r * |direction| = pixelLength --> r = pixelLength / |direction| --> r * |direction| kann alle 10 pixel berechnet werden
        DANACH kann man weiterrechnen
        r * (direction) = neue Position
        neueXPos += r * direction[0]
        neueYPos += r * direction[1]
        '''
        x = self.position[0]
        y = self.position[1]
        directionX = self.direction[0]
        directionY = self.direction[1]
        r = self.__pixelLength / math.hypot(directionX, directionY)
        
        newXPosition = x + r * directionX
        newYPosition = y + r * directionY
        
        self.position[0] = int(newXPosition)
        self.position[1] = int(newYPosition)
        
    def getDamge(self):
        return self.dmg
    
#    def setDamge(self, dmg):
#        self.dmg = dmg
