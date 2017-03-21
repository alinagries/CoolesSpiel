# -*- coding: cp1252 -*-
#Datum :    07-14.12.16
#Autor/en:  Lucas V., Till
#Version:   1.0

from decimal import Decimal
from bullet import Bullet
import pygame
import time

BLUE = (0, 0, 255)

class Weapon(pygame.sprite.Sprite):
    def __init__(self, firerate = 0.2, bulletspeed = 1, damage = 2, ammo = Decimal("Infinity"), room = 0):
        '''
        Initialisation von Weapon
        Parameter:      Float firerate, schuss nach seckunde * Firerate erlaubt
                        Float bulletspeed, Schussgeschwindigkeit (1 = Standart)
                        Float damage, Anzahl des Schadens einer Bullet
                        int/Decimal("Infinity") ammo, Munition der Waffe
        return values:  -
        '''
        super(Weapon, self).__init__()
        self.image = pygame.Surface([10, 10])
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)
        
        self.firerate = firerate
        self.bulletspeed = bulletspeed
        self.damage = damage
        self.ammo = ammo
        self.room = room
        self.lastShotTime = -self.firerate
        

    def createBullet(self, position, eventPos, playernick):#eventPos = Zielposition
        '''
        Falls eine Kugel geschossen werden darf (einzige Grund warum das nicht
        gehen sollte, ist seobald die Schussgeschwindigkeit ueberschritten wird)
        dann wird die ammo um 1 verringert und eine Bullet erzeugt
        Parameter:      Tuple (int, int) position, der neuen Bullet
                        Tuple (int, int) Zielposition der neuen Bullet
                        String, Nickname des Spielers, der schiesst
        return values:  Bullet oder None (nur wenn schuss nicht erlaubt)
        '''
        if self.shotAllowed():
            self.ammo -= 1
            bullet = Bullet(position[0], position[1], eventPos, self.bulletspeed, self.damage, playernick)
            return bullet
        else:
            print 'shot not Allowed in createBullet unter weapon.py (firerate)'
    
    def shotAllowed(self):
        '''
        ueberprueft ob ein Schuss gemacht werden darf
        Parameter:      -
        return values:  Boolean
        '''
        if time.clock() - (self.lastShotTime + self.firerate) >= 0 and self.ammo:
            self.lastShotTime = time.clock()
            return True
    
    def createSplitBullet(self, position, angle, ammount, eventPos, playernick):#eventPos = Zielposition
        '''
        Das Selbe wie createBullet, bekommt aber noch Winkel und Anzahl und ruft vSplit auf
        Parameter:      Tuple (int, int) position, der neuen Bullet
                        Int, angle
                        Int, amount
                        Tuple (int, int), eventPos, Ziel der neuen Bullet
                        String, Nickname des Spielers, der schiesst
        return values:  Bullet oder None (nur wenn schuss nicht erlaubt)
        '''
        if self.shotAllowed():
            self.ammo -= 1
            list = vSplit(eventPos, angle, amount)
            a=0
            for k in list:
                bullet += Bullet(position[0], position[1], (list[a],list[a+1]), self.bulletspeed, self.damage, playernick)
                a+=2
            return bullet
        else:
            print 'shot not Allowed in createBullet unter weapon.py'
    
    def vSplit(direction, angle, amount):
        '''
        vSplit dient der Verfielfachung von Vektoren fuer
        Streuschuesse(fuer spezif. Waffen).
 
        vSplit benoetigt einen Vektor(vector), einen Winkel, innerhalb dem die neuen
        Vektoren gestreut werden sollen(angle) und die Anzahl der zu streuenden
        Vektoren(amount)   -> ((x,y),1-180,1-...).
        vSplit gibt die Liste newV aus, in der hintereinander die x & y-Werte der
        Vektoren aufgeführt werden.
        Wird für amount eine ungerade Zahl gewaehlt, so ist der angegebene Vektor Teil
        von newV. Ist amount gerade, so fehlt der Anfangsvektor in der Mitte.
        Parameter:      Tuple (int, int), direction
                        int, angel
                        int, amount
        return Values:  -
        '''
        xDirection = direction[0]
        yDirection = direction[1]
        hz = amount/2
        newV = ()
        ausX = math.hypot(xDirection, yDirection)*(float(angle)/180)
        ausY = math.sqrt(((math.hypot(xDirection, yDirection)**2)) + (ausX)**2)
 
        for f in range(0, amount):
            aktX = (float((f+1))/hz)*ausX
            akktX = aktX
            zt = (math.hypot(xDirection, yDirection))
            aktX = -aktX + xDirection

            #LINKS
            if f <= hz:
                if -aktX > zt:
                    r = -aktX - zt
                    aktX = -zt +r
                aktY = math.sqrt((math.hypot(xDirection, yDirection)**2) - (aktX)**2)
                if yDirection < 0 and -yDirection > akktX:
                    aktY = -aktY
                newV += (aktX, aktY)

            #ggf. MITTE
            elif amount%2:
                newV+=(xDirection, yDirection)

            #RECHTS
            else:
                if aktX > zt:
                    r = aktX - zt
                    aktX = zt + r
                aktY = math.sqrt((math.hypot(xDirection, yxDirection)**2) - (aktX)**2)
                if yDirection < 0 and -yDirection > akktX:
                    aktY = -aktY
                newV+=(aktX, aktY)

        return newV
    

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
        gibt die Geschwindigkeit der Bullets, der Waffe aus
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
        return self.damage
    
    def setDamage(self, damage):
        '''
        setzt den Schaden der Waffe
        Parameter:      Float, Schaden der Waffe
        return values:  -
        '''
        self.damage = damage
    
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
