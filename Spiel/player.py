# -*- coding: cp1252 -*-
#Autor/en:  Lucas V., Niclas, Gregor
#Datum:     ????
#Version:   1.0

from weapon import Weapon
import pygame

GREEN = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self, nick = 'Lucas', hitPoints = 20, speed = 2, room = 0):
        """ Set up the player on creation. """
        super(Player,self).__init__()
 
        self.image = pygame.Surface([20, 20])
        self.rect = self.image.get_rect()
        self.room = room
        self.image.fill(GREEN)
        
        self.nick = nick
        self.hp = hitPoints
        self.speed = speed
        self.secondaryWeapon()
 
    def update(self, gamemap):
        '''
        updated die Playerbewegungen beim (knopfdruck events)
        Parameter:      Spielobjekt, gamemap
        return Value:   -
        '''
        keys = pygame.key.get_pressed()
        newRect = self.rect
        if keys[pygame.K_w]:
            newRect = self.rect.move(0, -self.speed)
        if keys[pygame.K_s]:
            newRect = self.rect.move(0, self.speed)
        if keys[pygame.K_a]:
            newRect = self.rect.move(-self.speed, 0)
        if keys[pygame.K_d]:
            newRect = self.rect.move(self.speed, 0)
        if gamemap.isRectValid(newRect):
            self.rect = newRect


    def shot(self, eventPos):
        '''
        Wenn moeglich (hoechstens wegen der zu vielen schussversuchen pro
        Sekunde nicht moeglich) wird ein Objekt Bullet erstellt.
        Falls keine Munition mehr vorhanden ist auf Standartwaffe wechseln
        Parameter:      int xPos, die x-Position des Spielers
                        int yPos, die y-Position des Spielers
                        Tuple (int, int), das Ziel des Schusses
        return values:  Boolean ODER None
                            je nachdem ob die Waffe einen schuss abfeuern darf
                            bsp. bei einer Waffengeschwindigkeit von 1 darf nach
                            0.5 Sekunden kein weiterer Schuss abgefeuert werden
        '''
        bullet = None
        position = self.rect.centerx, self.rect.centery
        weapon = self.weapon
        try:
            bullet = weapon.createBullet(position, eventPos, self.nick)#eventPos = Zielposition
        except:
            print 'bullet wird in shot unter player.py nicht erzeugt'
        if weapon.ammo == 0:
            self.secondaryWeapon()
            
        return bullet
        
    def secondaryWeapon(self):
        '''
        Der Spieler bekommt das Objekt der Standartwaffe zugewiesen
        Parameter:      -
        return values:  -
        '''
        self.weapon = Weapon()
        
    def isHit(self, damage):
        '''
        errechnung der Spielerhitpoints nach einem treffer
        Parameter:      Float, damage gegen den Spieler
        return values:  -
        '''
        self.hp -= damage
        
    def equipWeapon(self, weapon):
        self.weapon = weapon
            
##################### Getters und Setters, die momentan nirgends gebraucht werden, aber dazu gehoeren #####################

    def getNick(self):
        '''
        Ausgabe des Spielernicknames
        Parameter:      -
        return values:  String, nickname des Spielers
        '''
        return self.nick
    
    def setNick(self, nick):
        '''
        setzt den Spielernickname
        Parameter:      String, nickname des Spielers
        return values:  -
        '''
        self.nick = nick
        
    def getHitpoints(self):
        '''
        Ausgabe der Spielerhitpoints
        Parameter:      -
        return values:  Float hitpoints des Spielers
        '''
        return self.hp
    
    def setHitpoints(self, hp):
        '''
        setzt die Spielerhitpoints
        Parameter:      Float, Spielerhitpoints
        return values:  -
        '''
        self.hp = hp
    
    def getWeapon(self):
        '''
        Ausgabe der Waffe des Spielers
        Parameter:      -
        return values:  Objekt, von einer der Klasse Weapon
        '''
        return self.weapon
    
    def setWeapon(self, weapon):
        '''
        Der Spieler bekommt ein Objekt der Klasse Weapon, auf self.weapon
        Parameter:      Objekt der Klasse Weapon
        return values:  -
        '''
        self.weapon = weapon
        
    def getRoom(self):
        '''
        Ausgabe des Raumes des Spielers
        Parameter:      -
        return values:  Int, Raum (0-9)
        '''
        return self.room
    
    def setRoom(self, room):
        '''
        Der Spieler bekommt ein Raum zugewiesen
        Parameter:      Int, Raum (0-9)
        return values:  -
        '''
        self.room = room
        
