# -*- coding: utf-8 -*-
#Datum :    22/23.12.16
#Autor/en: Kai K. ,Till,  kerim
#Version:   1.0

from player import Player
from bot import Bot
from bullet import Bullet
from weapon import Weapon
from client import Client
import gamemap
import cPickle as Pickle
import pygame.image
import os.path
import createRoommap
import pygame
import random
import math


class Room:

    """
    Klasse die einzelne Räume und ihre Attribute, sowie Funktionen zum generieren, laden und speichern bereitstellt.

    """
    def __init__(self, name):
        """
        Initialisierung eines Raums

        Parameter:      str Name des Raums
        Rückgabewerte:  -
        """
        
        self.name = name
        self.col = gamemap.GameMap()
        self.bg = pygame.Surface
        self.doors = []
        self.equippables = []

        print 'room __Init__ wird aufgerufen!'

        if os.path.exists(name + ".rpkg"):
            self.loadFromRpkg(name + ".rpkg")
        else:
            self.generateRoomFromSource(name)

        self.allBots    = pygame.sprite.Group()
        self.allBullets = pygame.sprite.Group()
        self.playerList = []#darf hier sein
        
    def addBot(self, bot):
        self.allBots.add(bot)
    
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
        bot.room = self.name
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
                bot.rect.center = coord

    def shoot(self, destination, ip):
        '''
        gibt die Position eines Spielers
        Parameter:      eventPositions, liste mit Koordinaten der Zielpositionen der Bullets bsp.: ["default", "203_100", "013_000",...]
        return values:  -
        '''
        unterstrich = False
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
                            self.playerDied(player.nick)
            
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

    def removeBot(self, bot):
        '''
        nimmt einen Spieler aus der Playergruppe heraus
        Parameter:      Spielerobjekt
        return values:  -
        '''
        print 'player:', bot.nick, 'wird aus dem Spiel entfernt'
        self.allBots.remove(bot)
        
    
    def update(self):
        self.allBullets.update()
        self.__eventuallyEnterDoor()
        for bullet in self.allBullets:
            self.__handleCollision(bullet)
            
    def __eventuallyEnterDoor(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        ueberprueft ob der Spieler auf einer Door steht
        Parameter:      -
        return values:  -
        '''
        for bot in self.allBots:
            for door in self.getDoors():
                if bot.rect.colliderect(door.rect):
                    print 'door:', door
                    room = door.getRoom()
                    self.changeRoom(room.getName(), door.getExitpoint(), bot)
                    self.removeBot()
                    
    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName

    def getCol(self):
        """
        Zurückgabe der Gamemap

        Parameter:      -
        Rückgabewerte:  Gamemap Gamemap des Raums
        """
        return self.col

    def getBg(self):
        """
        Zurückgabe des Hintergrundbilds

        Parameter:      -
        Rückgabewerte:  pygame.Surface Hintergrundbild des Raums
        """
        return self.bg

    def getObjects(self):
        """
        Zurückgabe der Objekte des Raums

        Parameter:      -
        Rückgabewerte:  list Objekte des Raums
        """
        return self.objects

    def getDoors(self):
        """
        Zurückgabe der Türen des Raums

        Parameter:      -
        Rückgabewerte:  list Türen des Raums
        """
        return self.doors

    def setDoors(self, doors):
        """
        Setzen der Türen des Raums

        Parameter:      list Türen des Raums
        Rückgabewerte:  -
        """
        self.doors = doors

    def getEquippables(self):
        """
        Zurückgabe der benutzbaren Gegenstände des Raums

        Parameter:      -
        Rückgabewerte:  list benutzbare Gegenstände des Raums
        """
        return self.equippables

    def setEquippables(self, equip):
        """
        Zurückgabe der benutzbaren Gegenstände des Raums

        Parameter:      list benutzbare Gegenstände des Raums
        Rückgabewerte:  -
        """
        self.equippables = equip

    def generateRoomFromSource(self, name):
        """
        Generieren des Raums aus Quelldateien

        Parameter:      str Name des Raums
        Rückgabewerte:  -
        """
        self.name = name
        self.col = gamemap.createByImage(name + "col.png")
        print self.col
        #self.bg = pygame.image.load(name + ".png").convert()
        self.saveToRpkg()

    def saveToRpkg(self):
        """
        Speichern des Raums

        Parameter:      -
        Rückgabewerte:  -
        """
        print 'die fkt saveToRpkg wird aufgerufen!'
        #room = (self.name, self.col, pygame.image.tostring(self.bg, "RGB"), self.bg.get_size(), self.equippables, self.doors)
        room = (self.name, self.col, "placeholder", "placeholder", self.equippables, self.doors)
        print "room nach save", room
        try:
            Pickle.dump(room, open(self.name + ".rpkg", "wb"), 2)
        except Exception as e:
            print e
        

    def loadFromRpkg(self, path):
        """
        Laden des Raums

        Parameter:      str Dateiname/Pfad des zuladenen Raums
        Rückgabewerte:  -
        """
        try:
            room = Pickle.load(open(path, "rb"))
        except Exception as e:
            print e
        self.name = room[0]
        self.col = room[1]
        #self.bg = pygame.image.fromstring(room[2], room[3], "RGB").convert()
        self.equippables = room[4]
        self.doors = room[5]
        


        


