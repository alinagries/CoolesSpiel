# -*- coding: cp1252 -*-
#Datum :    07-14.12.16
#Autor/en:  Kerim, Till, Lucas V.
#Version:   1.0

from player import Player
from bot import Bot
from bullet import Bullet
from weapon import Weapon
from client import Client
import createRoommap
import gamemap
import pygame
import random
import math
import threading

mapPath = "map.png"
mymap = gamemap.createByImage(mapPath)

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
        self.allBots    = pygame.sprite.Group()
        self.allBullets = pygame.sprite.Group()
        self.playerList = []
        
        roommap = createRoommap.createRoommap(self)
        self.rooms = roommap.getRooms()
        #self.rooms[0] ist room 0
        #self.rooms[1] ist room 1
        #....
        
        self.clock = pygame.time.Clock()
    
    
    def changeRoom(self, newRoom, newPosition, bot):
        '''
        wird von room aufgerufen, ein bot hat eine Tuer betreten und geht in einen anderen Raum
        Parameter:      newRoom, (hoffentlich ein Int, KAI FRAGEN!) Nope!, roomobjekt -.-
                        newPosition (Tuple aus 2 INTs)
                        bot, ein botobjekt
        return values:  -
        '''
        bot.rect.center = newPosition
        self.rooms[newRoom].addBot(bot)
        
    
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
                self.rooms[bot.getRoom()].shoot(destination, ip)#nach der IP wird zwar doppelt geguckt, ist uns aber erstmal egal
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
            for bot in self.allBots:
                if self.playerList[playerCoordinates.index(playerCoord)] == bot.nick:
                    self.rooms[bot.getRoom()].updatePlayer(playerCoord)

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
            for room in self.rooms:
                room.update()

             # --- Limit to 20 frames per second
            self.clock.tick(60)

        pygame.quit()
        

