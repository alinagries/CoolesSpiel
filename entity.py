# -*- coding: cp1252 -*-
#Datum :    09/10.12.16
#Autor/en:  Lucas V.
#Version:   1.0

import pygame

'''
Player und Bullet erben von der Klasse
'''


class Entity():
    def __init__(self, rect = ((0, 0), (0, 0)), direction = (0, 0), speed = 1):
        self.rect = pygame.Rect(rect) #rect bekommt ((left, top), (width, height))# Koordianten und Umfang
        self.position = rect[0]
        self.direction = direction
        self.speed = speed

    def getRect(self):
        return self.rect
    
    def setRect(self, (xCoord, yCoord), (width, height)):
        self.rect = (xCoord, yCoord), (width, height)
 
    def getPosition(self):
        return self.rect[0]
    
    def setPosition(self, x, y):
        self.rect[0] = x, y
    
    def getXPos(self):
        return self.rect[0][0]
    
    def getYPos(self):
        return self.rect[0][1]

    def getDirection(self):
        return self.direction
    
#    def setDirection(self, x, y):
#        self.direction = x, y
        
    def getSpeed(self):
        return self.speed
    
#    def setSpeed(self, speed):
#        self.speed = speed
