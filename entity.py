# -*- coding: cp1252 -*-
#Datum :    07.12.16
#Autor/en:  Lucas V.
#Version:   1.0

'''
Player und Bullet erben von der Klasse
'''

class Entity():
    def __init__(self, position = (0, 0), direction = (0, 0), speed = 1):
        self.position = position
        self.direction = direction
        self.speed = speed
 
    def getPosition(self):
        return self.position
    
    def setPosition(self, x, y):
        self.position = x, y
        
    def getDirection(self):
        return self.direction
    
#    def setDirection(self, x, y):
#        self.direction = x, y
        
    def getSpeed(self):
        return self.speed
    
#    def setSpeed(self, speed):
#        self.speed = speed