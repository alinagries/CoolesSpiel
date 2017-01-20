# -*- coding: cp1252 -*-
#Datum :    07-14.12.16
#Autor/en:  Kerim, Till, Lucas V.
#Version:   1.0

from player import Player
from bot import Bot
from bullet import Bullet
from weapon import Weapon
import gamemap
import pygame
import random
import math

WHITE = (255, 255, 255)

'''erstelle das Fenster'''
mapPath = "map.png"
mymap = gamemap.createByImage(mapPath)

screenWidth = mymap.getWidth()
screenHeight = mymap.getHeight()
screen = pygame.display.set_mode([screenWidth, screenHeight])
pygame.key.set_repeat(1,10)
background = pygame.image.load(mapPath).convert()

class Game():    
    def __init__(self):
        '''
        Initialisation vom Game
        Achtet durchgehend, welche Spieler noch leben, bewegt die Schuesse,
        achtet auf Kollisionen und zeigt die Spielerpositionen
        Beendet das Spiel sobald nur noch ein Spieler am leben ist
        Parameter:      -
        return values:  -
        '''
        print 'Es gibt Bugs bei den Schuessen, wenn die zu schnell fliegen, sie koennen dann z.T. durch Spieler und Waende fliegen, ohne sie zu treffen, da die Schuesse nur fuer positionen berechnet werden und die Strecke dazwischen nicht ueberprueft wird'
        self.done = False
        self.allPlayers = pygame.sprite.Group()
        self.allBullets = pygame.sprite.Group()
        self.allWeapons = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.player1 = Player()
        self.bot1 = Bot()
        self.createSomeStuff()
        self.__startGame()
        
    def __startGame(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        startet das Spiel und achtet durchgehend, welche Spieler noch leben, bewegt die Schuesse,
        achtet auf Kollisionen und zeigt die Spielerpositionen
        Beendet das Spiel sobald das Fenster geschlossen wurde
        Parameter:      -
        return values:  -
        '''
        while not self.done:
            self.__eventProcessing()
            self.__updateAllSprites()
            self.__eventuallyEquipWeapon()
            for bullet in self.allBullets:
                self.__handleCollision(bullet)    
                
            screen.blit(background, [0,0])
            self.__drawAllSprites()
            pygame.display.flip()
         
            # --- Limit to 20 frames per second
            self.clock.tick(60)

        self.__endGame()
        pygame.quit()
        
    def createSomeStuff(self):
        '''erstellt ein paar Spieler und Waffen und plaziert diese'''
        self.allPlayers.add(self.player1)
        self.allPlayers.add(self.bot1)
        #bug wenn die Schussgeschwindigkeit zu schnell ist, dann ist die bullet nur an z.B.2
        #Positionen trifft nicht unbedingt eine Wand oder spieler
        
        weapon1 = Weapon(1, 4, 10, 3)
        weapon2 = Weapon(2, 2, 5, 5)
        weapon3 = Weapon(.2, 15, 20, 10000)
        weapon4 = Weapon(1, 3, 7, 6)
        
        self.allWeapons.add(weapon1)
        self.allWeapons.add(weapon2)
        self.allWeapons.add(weapon3)
        self.allWeapons.add(weapon4)
        
        weapon1.rect.y = 240
        weapon1.rect.x = 220
        weapon3.rect.x = 300
        weapon3.rect.y = 300
        weapon2.rect.x = 90
        weapon2.rect.y = 180
        weapon4.rect.x = 150
        weapon4.rect.y = 80
        self.player1.rect.y = 440
        self.player1.rect.x = 20
        self.bot1.rect.y = 20
        self.bot1.rect.x = 25

    def __eventProcessing(self):
        '''
        fuehrt bei einem event die entsprechende Aktion aus
        bewegen oder schießen
        Parameter:      -
        return values:  -
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.player1.update(mymap)
                self.bot1.update(mymap)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bullet = self.player1.shoot(self.player1.rect.centerx, self.player1.rect.centery, event.pos)
                if not bullet == None:
                    self.addBullet(bullet)
            
                
    def __updateAllSprites(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        updatet die Sprites
        Parameter:      -
        return values:  -
        '''
        self.allPlayers.update(mymap)
        self.allBullets.update()
        self.allWeapons.update()
                    
    def __drawAllSprites(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        zeichnet die Sprites
        Parameter:      -
        return values:  -
        '''
        self.allPlayers.draw(screen)
        self.allBullets.draw(screen)
        self.allWeapons.draw(screen)

    def __eventuallyEquipWeapon(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        ueberprueft ob der Spieler auf einer Weapon steht
        Parameter:      -
        return values:  -
        '''
        removeWeapon = []
        for player in self.allPlayers:
            for weapon in self.allWeapons:
                if player.rect.colliderect(weapon.rect):
                    player.equipWeapon(weapon)
                    removeWeapon.append(weapon)
        for weapon in removeWeapon:
            self.removeWeapon(weapon)
        
    def __handleCollision(self, bullet):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        ueberprueft ob ein Bulletobjekt in einem Mapobjekt oder einem Spieler, zieht einem Spieler Hitpoints ab
        und entfernt die Bullet bei einer Kollision
        Parameter:      Bulletobjekt
        return values:  -
        '''
        removeBullets = []
        removePlayers = []
        if not mymap.isRectValid(bullet.rect):
            removeBullets.append(bullet)
        elif bullet.rect.x > mymap.getWidth() or bullet.rect.y > mymap.getHeight():
            removeBullets.append(bullet)
        elif bullet.rect.x < 0 or bullet.rect.y < 0:
            removeBullets.append(bullet)
        else:
            for player in self.allPlayers:
                if bullet.rect.colliderect(player.rect) and player.nick != bullet.playernick:
                    removeBullets.append(bullet)
                    player.isHit(bullet.damage)
                    if player.hp <= 0:
                        removePlayers.append(player)
        
        for bullet in removeBullets:
            self.removeBullet(bullet)
        for player in removePlayers:
            self.removePlayer(player)
            
    def __getPlayerPosition(self, player):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        gibt die Position eines Spielers
        Parameter:      Spielerobjekt
        return values:  Tuple (int, int), position eines Spielers
        '''
        return player.getPosition()

    def addBullet(self, bullet):
        '''
        fuegt ein Bulletobjekt der Bulletgruppe liste hinzu
        Parameter:      Bulletobjekt
        return values:  -
        '''
        self.allBullets.add(bullet)

    def removeBullet(self, bullet):
        '''
        entfernt ein Bulletobjekt aus der Bulletgruppe
        Parameter:      Bulletobjekt
        return values:  -
        '''
        self.allBullets.remove(bullet)

        
    def addPlayer(self, player):
        '''
        fuegt einen Spieler der Playergruppe hinzu
        Parameter:      Spielerobjekt
        return values:  -
        '''
        self.allPlayers.add(player)

    def removePlayer(self, player):
        '''
        nimmt einen Spieler aus der Playergruppe heraus
        Parameter:      Spielerobjekt
        return values:  -
        '''
        self.allPlayers.remove(player)

    def addWeapon(self, weapon):
        '''
        fuegt eine Waffe der Waffengruppe hinzu
        Parameter:      Waffenobjekt
        return values:  -
        '''
        self.allWeapons.add(weapon)

    def removeWeapon(self, weapon):
        '''
        nimmt eine Waffe aus der Waffengruppe heraus
        Parameter:      Waffenobjekt
        return values:  -
        '''
        self.allWeapons.remove(weapon)

    def __endGame(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        Spielende, nur noch ein Spieler lebt
        Punkteverteilung sollte hier kommen
        Parameter:      -
        return values:  -
        '''
        print 'das Spiel ist zuende'

if __name__ == "__main__":
    Game()
