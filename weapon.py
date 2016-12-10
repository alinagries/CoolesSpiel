# -*- coding: cp1252 -*-
#Datum :    07.12.16
#Autor/en:  Lucas V.
#Version:   1.0

from bullet import Bullet
'''
Weapons besitzen
 -ein Richtung (die kann auch eine andere sein, als die vom player)
 -eine Position (die vom player)
 -eine Feuerrate
 -eine Schussgeschwindigkeit (speed vom bullet)
 -einen Schaden
 -und Munition
 '''
 
 #time muss mit einbezogen werden, damit die firerate irgendeinen Sinn macht
class Weapon():
    def __init__(self, direction = (0, 0), firerate = 1, bulletspeed = 1, damge = 2, ammo = True): # True = unendlich, int = endlich
        self.bulletsize = (2, 5)
        self.direction = direction
        self.firerate = firerate
        self.bulletspeed = bulletSpeed
        self.dmg = damge
        self.ammo = ammo

    def createBullet(self, position):
        bullet = Bullet.__init__((position, self.bulletsize), self.direction, self.bulletSpeed, self.dmg)
        return bullet
    
    
    def getDirection(self):
        return self.direction
    
    def setDirection(self, x, y):
        self.direction = x, y
    
    def getPosition(self):
        return self.position
    
    def setPosition(self, x, y):
        self.position = x, y
        
    def getFirerate(self):
        return self.firerate
    
    def setDirection(self, firerate):
        self.firerate = firerate
        
    def getBulletspeed(self):
        return self.bulletspeed
    
    def setBulletspeed(self, bulletspeed):
        self.bulletspeed = bulletspeed
        
    def getDamage(self):
        return self.dmg
    
    def setDamage(self, dmg):
        self.dmg = dmg
    
    def getAmmo(self):
        return self.ammo
    
    def setAmmo(self, ammo):
        self.ammo = ammo