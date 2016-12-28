# -*- coding: cp1252 -*-
#Datum :    07-14.12.16
#Autor/en:  Lucas V., Till
#Version:   1.0

from decimal import Decimal
from bullet import Bullet
import time

 
class Weapon():
    def __init__(self, firerate = 0.2, bulletspeed = 1, damage = 2, ammo = Decimal("Infinity")):
        '''
        Initialisation von Weapon
        Parameter:      Float firerate, schuss nach seckunde * Firerate erlaubt
                        Float bulletspeed, Schussgeschwindigkeit (1 = Standart) (und leider auch Praezision)
                            ab bulletspeed < 0.2 gibt es vermehrt Bugs, teilweise auch bei > 0.2
                        Float damage, Anzahl des Schadens einer Bullet
                        int/Decimal("Infinity") ammo, Munition der Waffe
        return values:  -
        '''
        
        self.firerate = firerate
        self.bulletspeed = bulletspeed
        self.dmg = damage
        self.ammo = ammo
        self.lastShotTime = -self.firerate


    def createBullet(self, position, eventPos, playernick):#eventPos = Zielposition
        '''
        Falls eine Kugel geschossen werden darf (einzige Grund warum das nicht
        gehen sollte, ist seobald die Schussgeschwindigkeit ueberschritten wird)
        dann wird die ammo um 1 verringert und eine Bullet erzeugt
        Parameter:      Tuple (int, int) position, der neuen Bullet
                        Tuples (int, int) Zielposition der neuen Bullet
        return values:  Bullet oder None (nur wenn schuss nicht erlaubt)
        '''
        if self.shotAllowed():
            self.ammo -= 1
            bullet = Bullet(position[0], position[1], eventPos, self.bulletspeed, self.dmg, playernick)
            return bullet
        else: #steht nur fuer Tests hier
            print 'shot not Allowed'
    
    def shotAllowed(self):
        '''
        ueberprueft ob ein Schuss gemacht werden darf
        Parameter:      -
        return values:  Boolean
        '''
        if time.clock() - (self.lastShotTime + self.firerate) >= 0 and self.ammo:
            self.lastShotTime = time.clock()
            return True

##################### Getters und Setters, die momentan nirgends gebraucht werden, aber dazu gehoeren #####################
            
    def getFirerate(self):
        '''
        gibt die feuerrate der Waffe aus
        Parameter:      -
        return values:  Float, feuerrate der Waffe
        '''
        return self.firerate
    
    def setFirerate(self, firerate):
        '''
        setzt die feuerrate der Waffe
        Parameter:      Float, feuerrate der Waffe
        return values:  -
        '''
        self.lastShotTime = -firerate
        self.firerate = firerate
        
    def getBulletspeed(self):
        '''
        gibt die Geschwindigkeit der Bullets, der Waffe
        Parameter:      -
        return values:  Float, Geschwindigkeit der Bullet, der Waffe
        '''
        return self.bulletspeed
    
    def setBulletspeed(self, bulletspeed):
        '''
        setzt die Geschwindigkeit der Bullet, die von der Waffe geschossen wird
        Parameter:      Float, feuerrate der Waffe
        return values:  -
        '''
        self.bulletspeed = bulletspeed
        
    def getDamage(self):
        '''
        gibt den Schaden der Waffe aus
        Parameter:      -
        return values:  Float, Schaden der Waffe
        '''
        return self.dmg
    
    def setDamage(self, dmg):
        '''
        setzt den Schaden der Waffe
        Parameter:      Float, Schaden der Waffe
        return values:  -
        '''
        self.dmg = dmg
    
    def getAmmo(self):
        '''
        gibt die Munition der Waffe aus
        Parameter:      -
        return values:  Int/Decimal("Infinity"), Munition der Waffe
        '''
        return self.ammo
    
    def setAmmo(self, ammo):
        '''
        setzt die Munition der Waffe
        Parameter:      Int/Decimal("Infinity"), Munition der Waffe
        return values:  -
        '''
        self.ammo = ammo
