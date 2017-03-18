# -*- coding: cp1252 -*-
#Datum :    07-14.12.16
#Autor/en:  Kerim, Till, Lucas V.
#Version:   1.0
from random import randint

from player import Player
from bot import Bot
from bullet import Bullet
from weapon import Weapon
from client import Client
import gamemap
import pygame
import math
import threading

##WHITE = (255, 255, 255)
##
##'''erstelle das Fenster'''
mapPath = "map.png"
mymap = gamemap.createByImage(mapPath)
##
##screenWidth = mymap.getWidth()
##screenHeight = mymap.getHeight()
##screen = pygame.display.set_mode([screenWidth, screenHeight])
##pygame.key.set_repeat(1,10)
##background = pygame.image.load(mapPath).convert()

class Game(threading.Thread):    
    def __init__(self, parent):
        '''
        Initialisation vom Game
        Achtet durchgehend, welche Spieler noch leben, bewegt die Schuesse,
        achtet auf Kollisionen und zeigt die Spielerpositionen
        Beendet das Spiel sobald nur noch ein Spieler am leben ist
        Parameter:      -
        return values:  -
        '''
        threading.Thread.__init__(self)
        self.deamon = True
        self.parent = parent

        self.done = False
        self.allPlayers = pygame.sprite.Group()
        self.allBots    = pygame.sprite.Group()
        self.allBullets = pygame.sprite.Group()
        self.allWeapons = pygame.sprite.Group()

        self.playerList = []
        
        self.clock = pygame.time.Clock()
        

    def setPlayerlist(self, x):
        self.playerList = x
        for botnick in self.playerList:
            self.createBot(botnick)
        self.start()
        
    def run(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        startet das Spiel und achtet durchgehend, welche Spieler noch leben, bewegt die Schuesse,
        achtet auf Kollisionen und zeigt die Spielerpoitionen
        Beendet das Spiel sobald das Fenster geschlossen wurde
        Parameter:      -
        return values:  -
        '''
        
        while not self.done:
            self.allBullets.update()
            for bullet in self.allBullets:
                self.__handleCollision(bullet)
             # --- Limit to 20 frames per second
            self.clock.tick(60)

        pygame.quit()

    def createBot(self, name, coord = [30,30]):
        '''
        bekommt eine Position eines Spielers und zeichnet diesen
        Parameter:      coord, bsp ("034", "100")
        return values:  -
        '''
        bot = Bot()
        bot.nick = name
        bot.rect.centerx = coord[0]
        bot.rect.centery = coord[1]
        self.allBots.add(bot)

    def moveBot(self, newCoord, name):
        unterstrich = False
        xCoord = ""
        yCoord = ""
        for i in range(len(newCoord)):
            if newCoord[i] == '_':
                unterstrich = True
            elif not unterstrich:
                xCoord += newCoord[i]
            else:
                yCoord += newCoord[i]
        coord = int(xCoord), int(yCoord)

        for bot in self.allBots:
            if bot.nick == name:
                bot.rect.centerx = coord[0]
                bot.rect.centery = coord[1]



    def shoot(self, destination, ip):
        '''
        gibt die Position eines Spielers
        Parameter:      eventPositions, liste mit Koordinaten der Zielpositionen der Bullets bsp.: ["default", "203_100", "013_000",...]
        return values:  -
        '''
        unterstrich = False
        xCoord = ""
        yCoord = ""
        for i in range(len(destination)):
            if destination[i] == '_':
                unterstrich = True
            elif not unterstrich:
                xCoord += destination[i]
            else:
                yCoord += destination[i]
        destination = int(xCoord), int(yCoord)
        for bot in self.allBots:
            if bot.nick == ip:
                bullet = bot.shot(destination)
                if bullet == None:
                    print 'bullet ist in game.py == None'
                self.allBullets.add(bullet)
                print("Recieved a shot")


    def updatePlayers(self, playerCoordinates):# muss nochz fuer schuesse und waffen gemacht werden
        '''
        zeichnet alle Spieler als Bots
        Parameter:      playerCoordinates, liste mit Koordinaten der Spieler als Strings bsp.: ["100_80", "27_90",...]
        return values:  -
        '''

        for playerCoord in playerCoordinates:
            self.moveBot(playerCoord, self.playerList[playerCoordinates.index(playerCoord)])
                

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
        bulletPos = bullet.bulletFligthPositions
        hitPlayer = False

    
        for bulletposition in bulletPos:
            if hitPlayer:
                pass
            elif not mymap.isPositionValid(bulletposition[0], bulletposition[1]):
                removeBullets.append(bullet)
            elif bulletposition[0] > mymap.getWidth() or bulletposition[1] > mymap.getHeight():
                removeBullets.append(bullet)
            elif bulletposition[0] < 0 or bulletposition[1] < 0:
                removeBullets.append(bullet)
            else:
                for player in self.allBots:
                    if player.rect.collidepoint(bulletposition) and player.nick != bullet.playernick:
                        hitPlayer = True
                        removeBullets.append(bullet)
                        player.isHit(bullet.damage)
                        if player.hp <= 0:
                            removePlayers.append(player)
                            self.parent.playerDied(player.nick)
            
        for bullet in removeBullets:
            self.removeBullet(bullet)
        for player in removePlayers:
            self.removeBot(player)

    def removeBullet(self, bullet):
        '''
        entfernt ein Bulletobjekt aus der Bulletgruppe
        Parameter:      Bulletobjekt
        return values:  -
        '''
        #print 'bullets:', self.allBullets.sprites()
        self.allBullets.remove(bullet)

    def removeBot(self, player):
        '''
        nimmt einen Spieler aus der Playergruppe heraus
        Parameter:      Spielerobjekt
        return values:  -
        '''
        print 'player:', player.nick, 'wird aus dem Spiel entfernt'
        self.allBots.remove(player)
