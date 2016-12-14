# -*- coding: cp1252 -*-
#Datum :    09-14.12.16
#Autor/en:  Lucas V.
#Version:   1.0

import pygame

'''
Player und Bullet erben von der Klasse
'''


class Entity():
    def __init__(self, rect = (0, 0, 0, 0), direction = (0, 0), speed = 1):
        self.rect = pygame.Rect(rect) #rect bekommt (left, top, width, height)# Koordianten und Umfang
        self.direction = direction
        self.speed = speed

    def getSize(self):
        return self.rect[2], self.rect[3] #(Int, Int)

    def setSize(self, width, height): #(Int, Int)
        self.rect = pygame.Rect(self.rect[0], self.rect[1], width, height)

    def getRect(self): #(Int, Int, Int, Int)
        return self.rect
    
    def setRect(self, xCoord, yCoord, width, height): #(Int, Int, Int, Int)
        self.rect = pygame.Rect(xCoord, yCoord, width, height)
 
    def getPosition(self): #(Int, Int)
        return self.rect[0], self.rect[1]

    def setPosition(self, x, y): #(Int, Int)
        self.rect = pygame.Rect(x, y, self.rect[2], self.rect[3])
    
    def getXPos(self): #Int
        return self.rect[0]
    
    def getYPos(self): #Int
        return self.rect[1]

    def getDirection(self): #(Int, Int)
        return self.direction
    
#    def setDirection(self, x, y): #(Int, Int)
#        self.direction = x, y
        
    def getSpeed(self):#soll Float sein, bisher nur mit Ints benutzt
        return self.speed
    
#    def setSpeed(self, speed): #soll Float sein, wird bisher aber nur mit Int benutzt
#        self.speed = speed
