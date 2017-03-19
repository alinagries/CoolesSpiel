#Autor/en:  Lucas Voelz
#Version:   1.0

from weapon import Weapon
from player import Player
import pygame

RED = (255, 0, 0)

class Bot(Player):
    def __init__(self, nick = "bot"):
        '''
        Initialisierung vom Bot
        Parameter:      -
        return values:  -
        '''
        Player.__init__(self, nick)
        self.image.fill(RED)
##        self.weapon.firerate = 0
##
##    def equipWeapon(self, weapon):
##        self.weapon = weapon
##        self.weapon.firerate = 0
##
##    def secondaryWeapon(self):
##        '''
##        Der Spieler bekommt das Objekt der Standartwaffe zugewiesen
##        Parameter:      -
##        return values:  -
##        '''
##        self.weapon = Weapon()
##        self.weapon.firerate = 0
##        
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
        self.weapon.firerate = 0
        try:
            bullet = weapon.createBullet(position, eventPos, self.nick)#eventPos = Zielposition
        except:
            print 'bullet wird in shot unter player.py nicht erzeugt'
        if weapon.ammo == 0:
            self.secondaryWeapon()
            
        return bullet
        

    def update(self, gamemap):
        '''
        Ueberschreibung vom Update des Bots
        Parameter:      Spielobjekt, gamemap
        return values:  -
        '''
        pass
