# -*- coding: cp1252 -*-
#Datum :    07-14.12.16
#Autor/en:  Lucas V., Till
#Version:   1.0

from decimal import Decimal
from bullet import Bullet
import time

'''
Weapons besitzen
 -ein Richtung (die kann auch eine andere sein, als die vom player)
 -eine Position (die vom player)
 -eine Feuerrate
 -eine Schussgeschwindigkeit (speed vom bullet)
 -einen Schaden
 -und Munition
 '''
 
'''
Todo:
 -Bei Langeweiele
    -max reichweite fuer Waffen einbauen(?) fuer Streuschuesse, Bsp. Flammenwerfer, schrotgewehr oder so
    -weitere Waffen (Streuschuesse) zu machen: z.B. sniper, maschinengewehr, panzerfaust? raketenwerfer? ganz nach geschmack
    -andere gadets, z.B. minen, andere Fallen, oder sowas
        -tarnzeugs (bsp. n paar sec nicht zu sehen, oder man muss naeher an der Person sein um sie zu sehen), Teleporter, etc....
        -sichtfeld erhoehen
        -Waffe upgraden? (feuerrate veringern, schaden erhoehen, ...)
'''
 
class Weapon():
    def __init__(self, direction = (1, 1), firerate = 1, bulletspeed = 1, damage = 2, ammo = Decimal("Infinity")):
        self.bulletsize = (1,3)
        self.direction = direction
        self.firerate = firerate
        self.bulletspeed = bulletspeed
        self.dmg = damage
        self.ammo = ammo
        self.lastShotTime = time.clock()


    def createBullet(self, position): #(Int, Int)
        if self.shotAllowed(): #Boolean
            self.ammo -= 1
            bullet = Bullet((position, self.bulletsize), self.direction, self.bulletspeed, self.dmg)
            return bullet #Objekt
        else:
            print 'shot not Allowed'
    
    def shotAllowed(self): #Boolean
        if time.clock() - (self.lastShotTime + self.firerate) > 0 and self.ammo:
            self.lastShotTime = time.clock()
            return True
            
    def getDirection(self): #(Int, Int)
        return self.direction
    
    def setDirection(self, x, y): #(Int, Int)
        self.direction = x, y
        
    def getFirerate(self): #Float
        return self.firerate
    
    def setFirerate(self, firerate): #Float
        self.firerate = firerate
        
    def getBulletspeed(self): #Float
        return self.bulletspeed
    
    def setBulletspeed(self, bulletspeed): #Float
        self.bulletspeed = bulletspeed
        
    def getDamage(self): #Float/Double
        return self.dmg
    
    def setDamage(self, dmg): #Float oder Double
        self.dmg = dmg
    
    def getAmmo(self): #Int oder Decimal("Infinity")
        return self.ammo
    
    def setAmmo(self, ammo): #Int oder Decimal("Infinity")
        self.ammo = ammo
