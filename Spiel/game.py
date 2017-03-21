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
import createRoommap
import gamemap
import pygame
import math
import threading


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
        self.allWeapons = pygame.sprite.Group()
        self.playerList = []
        self.allPlayers = [] #tuple mit IPs und rauemen
        roommap = createRoommap.createRoommap(self)
        self.rooms = roommap.getRooms()
        
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
            for room in self.rooms:
                room.update()

             # --- Limit to 20 frames per second
            self.clock.tick(60)

        pygame.quit()
    def showDoors(self, doorPositions):
        '''
        wird von room aufgerufen, ein bot hat eine Tur betreten und geht in einen anderen Raum
        Parameter:      RoomName, (Int, 0-9,)
                        newPosition (Tuple aus 2 INTs)
                        bot, ein botobjekt
        return values:  -
        '''
        self.parent.showDoors(doorPositions)
        
    
    def changeRoom(self, roomName, newPosition, bot):
        '''
        wird von room aufgerufen, ein bot hat eine Tur betreten und geht in einen anderen Raum
        Parameter:      RoomName, (Int, 0-9,)
                        newPosition (Tuple aus 2 INTs)
                        bot, ein botobjekt
        return values:  -
        '''
        #print 'playerPos:', bot.rect.center
        bot.rect.centerx = newPosition[0]
        bot.rect.centery = newPosition[1]
        bot.setRoom(roomName)
        position = str(newPosition[0]) + "_" + str(newPosition[1])
        for i in range(len(self.allPlayers)):
            if bot.nick == self.allPlayers[i][0]:
                self.allPlayers[i] = (bot.nick, int(roomName))
        self.rooms[int(roomName)].addBot(bot)
        self.parent.changeRoom(bot.nick, roomName, position)
        
    def createBot(self, name, room = 0, coord = [30,30]):
        '''
        bekommt eine Position eines Spielers und zeichnet diesen
        Parameter:      coord, bsp ("034", "100")
        return values:  -
        '''
        self.allPlayers.append((name, room))
        self.rooms[room].createBot(name)

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

        
        for ipAndRoom in self.allPlayers:
            if ip == ipAndRoom[0]:#[(IP, "0"), (IP, "1"),..]
                self.rooms[ipAndRoom[1]].shoot(destination, ip)#nach der IP wird zwar doppelt geguckt, ist uns aber erstmal egal


    def updatePlayers(self, playerCoordinates):# muss nochz fuer schuesse und waffen gemacht werden
        '''
        zeichnet alle Spieler als Bots
        Parameter:      playerCoordinates, liste mit Koordinaten der Spieler als Strings bsp.: ["100_80", "27_90",...]
        return values:  -
        '''
        for playerCoord in playerCoordinates:
            for botName in self.allPlayers:
                try:
                    if self.playerList[playerCoordinates.index(playerCoord)] == botName[0]:
                        self.rooms[botName[1]].updatePlayer(playerCoord, botName[0])
                except:
                    print playerCoord, 'ist nicht in', playerCoordinates

    def setRandomWeapons(self, positions):
        newPositions = self.convertStringsToPositions(positions)
        for weaponPosition in newPositions:
            weapon = self.setRandomWeapon(weaponPosition)
        
    def setRandomWeapon(self, position):
        intFirerate     = randint(1, 10)
        floatFirerate   = 0.1 * intFirerate
        bulletspeed     = randint(1, 3)
        damage          = randint(1, 5)
        ammo            = randint(4, 8)
        room            = 0
        newWeapon = Weapon(floatFirerate, bulletspeed, damage, ammo, room)
        newWeapon.rect.center = position
        self.rooms[room].addWeapon(newWeapon)
        self.parent.sendStartWeapon(position, (floatFirerate, bulletspeed, damage, ammo))

    def convertStringsToPositions(self, listWithStrings):
        '''
        bekommt eine Liste mit den Positionen der Spieler als String und wandelt diese um
        bsp.: ["012_007", "130_097",...] ->  [(12,7), (130, 97),...]
        Parameter:      ListWithStrings
        return values:  listWithPositions, umgewandelte liste aus Positionen
        '''
        listWithPositions = []
        for playerCoord in range(len(listWithStrings)):
            for coord in listWithStrings[playerCoord]:
                xCoord = ""
                yCoord = ""
                unterstrich = False
                for i in range(len(listWithStrings[playerCoord])):
                    try:
                        int(listWithStrings[playerCoord][i])
                        if unterstrich:
                            yCoord += listWithStrings[playerCoord][i]
                        else:
                            xCoord += listWithStrings[playerCoord][i]
                        if listWithStrings[playerCoord][i] == "_":
                            unterstrich = True
                    except:
                        if listWithStrings[playerCoord][i] == "_":
                            unterstrich = True
            listWithPositions.append((int(xCoord), int(yCoord)))
        return listWithPositions

                    
    def equipedWeapon(self, weaponPos, nickname, room):
        self.parent.updateWeapon(weaponPos, nickname, room)

    def changeWeapon(self, oldPosition, newPosition, room):
        self.rooms[int(room)].changeWeapon(oldPosition, newPosition)

    def playerDied(self, playerNick):
        self.parent.playerDied(playerNick)
                                
        
                
