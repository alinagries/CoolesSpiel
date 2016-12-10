# -*- coding: cp1252 -*-
#Datum :    07.12.16
#Autor/en:  Alina, Lucas V.
#Version:   1.0

from entity import Entity
from bullet import Bullet
from weapon import Weapon
import pygame
'''
Ein Player ist ein Objekt, das einen Namen/Erkennung (Nick), Position, Blickrichtung, Hp, Geschwindigkeit und eine Waffe hat.
er braucht eine Referenz zu einem game ueber den Server oder Client 
'''

class Player(Entity):
    def __init__(self, nick, rect = ((0, 0), (3, 1)), direction = (0, 0), hitPoints = 20, speed = 1):
        self = super.__init__(rect, direction, speed)
        self.game = 0
        self.nick = nick
        self.hp = hitPoints
        self.weapon = self.secondaryWeapon()
    
    def shoot(self, weapon):
        position = self.rect[0]
        bullet = weapon.createBullet(position) #bullet ist eine Kugel mit Position, Groeße, Richtung, Geschwindigkeit und Schaden 
        return bullet #dem game muss noch gesagt werden, dass geschossen wurde
    
    def secondaryWeapon(self):
        self.weapon = Weapon.__init__()
        
    def getNick(self):
        return self.nick
    
    def setNick(self, nick):
        self.nick = nick
        
    def getHitpoints(self):
        return self.hp
    
    def setHitPoints(self, hp):
        self.hp = hp
    
    def getWeapon(self):
        return self.weapon
    
    def setWeapon(self, weapon):
        self.weapon = weapon
        
