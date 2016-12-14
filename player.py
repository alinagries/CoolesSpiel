# -*- coding: cp1252 -*-
#Datum :    07-14.12.16
#Autor/en:  Alina, Lucas V.
#Version:   1.0

from entity import Entity
from weapon import Weapon
'''
Ein Player ist ein Objekt, das einen Namen/Erkennung (Nick), Position, Hp, Geschwindigkeit und eine Waffe hat.
er braucht eine Referenz zu einem game ueber den Server oder Client 
'''

class Player(Entity):
    def __init__(self, nick, rect = ((0, 0), (3, 1)), hitPoints = 20, speed = 1, direction = (1, 1)):
        Entity.__init__(self, rect, direction, speed)
        self.game = 0
        self.nick = nick
        self.hp = hitPoints
        self.weapon = self.secondaryWeapon()
    
    def shoot(self):
        position = self.rect[0], self.rect[1] #(Int, Int)
        weapon = self.weapon
        bullet = weapon.createBullet(position)
        if weapon.ammo == 0:
            self.weapon = self.secondaryWeapon()
        return bullet#Bullet oder None
        #bullet kann auch den Wert None haben, falls die bullet nicht erzeugt werden durfte Beispielsweise, da nur
        #eine begrenzte anzahl von schuessen pro Sekunde erlaubt ist und diese dadurch ueberschritten werden wuerde
        
    def secondaryWeapon(self): #Weapon() -> Objekt
        self.weapon = Weapon()
        
    def equipWeapon(self, weapon):#objekt aus der Klasse Weapon oder einer Oberklasse
        self.weapon = weapon()
        
    def getNick(self): #String
        return self.nick
    
    def setNick(self, nick): #String
        self.nick = nick
        
    def getHitpoints(self): #Int
        return self.hp
    
    def setHitpoints(self, hp): #Int
        self.hp = hp
    
    def getWeapon(self): #Objekt aus einer Weapon Klasse
        return self.weapon
    
    def setWeapon(self, weapon): #Objekt aus einer Weapon Klasse
        self.weapon = weapon
        
