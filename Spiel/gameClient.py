# -*- coding: cp1252 -*-
#Datum :    07-14.12.16
#Version:   1.0

from player import Player
from bot import Bot
from bullet import Bullet
from weapon import Weapon
from client import Client
from manager import shaderoverlay
from door import Door
import createRoommap
import gamemap
import pygame
import math
import ast


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
        self.roommap = createRoommap.createRoommap(None)
        self.myRoom  = self.roommap.getStartRoom()
        self.mymap   = self.myRoom.getCol()
        #mapPath = "0.png" 
        self.screen = pygame.display.set_mode([self.mymap.getWidth(), self.mymap.getHeight()])
        pygame.key.set_repeat(1,10)
        self.background = self.myRoom.getBg().convert()
        self.rooms = self.roommap.getRooms()
        
        self.c = Client(self)
        self.done = False
        self.allPlayers = pygame.sprite.Group()
        self.allBots    = pygame.sprite.Group()
        self.drawBots   = pygame.sprite.Group()
        self.allBullets = pygame.sprite.Group()
        self.allWeapons = pygame.sprite.Group()
        self.allDoors0   = pygame.sprite.Group()
        self.allDoors1   = pygame.sprite.Group()
        self.player1 = Player()
        self.player1.nick = self.c.ipAtServer
        self.playerList = []
        self.weaponList = []
        self.player1.rect.x = 20
        self.player1.rect.y = 20
        self.allPlayers.add(self.player1)
        door1 = Door(0,0,'0',0,0)
        door2 = Door(0,0,'0',0,0)
        door1.rect.center = (230,50)
        door2.rect.center = (220,400)
        self.allDoors0.add(door1)
        self.allDoors1.add(door2)
        self.clock = pygame.time.Clock()


        self._shader     = shaderoverlay.ShaderOverlay(positionmap = self.mymap)
        self._shader.addLightsource(self.player1, 400, (255, 245, 240), 220, 40)
        self.shaderScreen = self._shader.getOverlay(self.screen.get_rect())
        self.shaderUpdate = False
        
##        self.screen.blit(self.background, [0,0])
##        self.__drawAllSprites()
##        pygame.display.flip()
##        
        self.__startGame()

        

    def setPlayerlist(self, x):
        self.playerList = x
        for botnick in self.playerList:
            self.createBot(botnick)
        self.checkAllBots()

    def setDoor(self, data):
        position    = int(data[0]), int(data[1])
        newDoor     = Door()
        newDoor.rect.center = position
        self.allDoors.add(newDoor)
        
        
    def setWeapon(self, data):
        position        = int(data[0]), int(data[1])
        firerate        = float(data[2])
        bulletspeed     = int(data[3])
        damage          = int(data[4])
        ammo            = int(data[5])
        newWeapon = Weapon(firerate, bulletspeed, damage, ammo)
        newWeapon.rect.center = position
        self.allWeapons.add(newWeapon)

        

    def equipWeapon(self, data):#"((oldPos),(newPos), (nickname))"
        oldPos      = int(data[0]), int(data[1])
        newPosition = self.convertStringsToPositions([data[2]])
        nickname    = data[3]
        newPos = newPosition[0]
                                                     
        
        if self.player1.nick == nickname:
            for weapon in self.allWeapons:
                if weapon.rect.center == oldPos:
                    self.player1.equipWeapon(weapon)
                    newWeapon = Weapon(weapon.firerate, weapon.bulletspeed, weapon.damage, weapon.ammo)
                    newWeapon.rect.center = newPos
                    self.allWeapons.add(newWeapon)
                    self.allWeapons.remove(weapon)
        else:
            for weapon in self.allWeapons:
                if weapon.rect.center == oldPos:
                    newWeapon = Weapon(weapon.firerate, weapon.bulletspeed, weapon.damage, weapon.ammo)
                    newWeapon.rect.center = newPos
                    self.allWeapons.add(newWeapon)
                    self.allWeapons.remove(weapon)

        
    def __startGame(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        startet das Spiel und achtet durchgehend, welche Spieler noch leben, bewegt die Schuesse,
        achtet auf Kollisionen und zeigt die Spielerpoitionen
        Beendet das Spiel sobald das Fenster geschlossen wurde
        Parameter:      -
        return values:  -
        '''
        i = 0
        while not self.done:
            self.__eventProcessing()
            self.allBullets.update()
            for bullet in self.allBullets:
                self.__handleCollision(bullet)
            self.screen.blit(self.background, [0,0])
            self.__drawAllSprites()
            pygame.display.flip()
             # --- Limit to 20 frames per second
            self.clock.tick(60)

            i += 1
            if i >= 15 and self.shaderUpdate:
                self.shaderScreen = self._shader.getOverlay(self.screen.get_rect())
                i = 0
                self.shaderUpdate = False

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
        coord = int(newCoord[0]), int(newCoord[1])
        for bot in self.allBots:
            if bot.nick == name:
                bot.rect.centerx = coord[0]
                bot.rect.centery = coord[1]

    def playerDied(self, player):
        if player == self.player1.nick:
            print("You Died xDD")
            self.done = True
        
        for bot in self.allBots:
            if str(bot.nick) == str(player):
                self.allBots.remove(bot)
                self.playerList.remove(ast.literal_eval(player))

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
            if bot.nick == ip and int(bot.room) == int(self.player1.room):
                    bullet = bot.shot(destination)
                    self.allBullets.add(bullet)
    
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

    def updatePlayers(self, playerCoordinates):# muss nochz fuer schuesse und waffen gemacht werden
        '''
        zeichnet alle Spieler als Bots
        Parameter:      playerCoordinates, liste mit Koordinaten der Spieler als Strings bsp.: ["100_80", "27_90",...]
        return values:  -
        '''

        allPlayerCoords = self.convertStringsToPositions(playerCoordinates)
        #print 'playerList:', self.playerList
        for playerCoord in allPlayerCoords:
        #    print 'playerCoord:', playerCoord
            try:
                self.moveBot(playerCoord, self.playerList[allPlayerCoords.index(playerCoord)])
            except:
                print 'konnte nicht alle Player updaten!'

    def changeRoom(self, data):
        nick = data[0]
        print type(nick), "TYPE!!"
        newRoom = data[1]
        newPosition = self.convertStringsToPositions([data[2]])
        newPos = newPosition[0]
        print 'NEW POS', newPos
        
        for bot in self.allBots:
            if str(self.player1.nick) == str(nick):
                print "!!!!!!!!!!!!!!!!???????????????????"
                self.player1.setRoom(newRoom)
                self.player1.rect.center = newPos
                print self.player1.rect.center, "PLAYERRECT!!!"
                self.__drawAllSprites()
                self.changeBackround(newRoom)
            if str(bot.nick) == nick:
                bot.room = newRoom
        self.checkAllBots()

    def checkAllBots(self):
        self.drawBots.empty()
        for bot in self.allBots:
            if int(bot.room) == int(self.player1.room):
                self.drawBots.add(bot)

    def changeBackround(self, newRoom):
        self.myRoom  = self.rooms[int(newRoom)]
        self.mymap   = self.myRoom.col

        mapPath = newRoom + ".png" 

        self.background = self.myRoom.getBg().convert()
        #self.allWeapons.empty()
        #self.allDoors.empty()
        self.allBullets.empty()

    
    def __eventProcessing(self):
        '''
        fuehrt bei einem event die entsprechende Aktion aus
        bewegen oder schiessen
        Parameter:      -
        return values:  -
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                self.player1.update(self.mymap)
                self.shaderUpdate = True
                self.sendPos((self.player1.rect.centerx, self.player1.rect.centery))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bullet = self.player1.shot(event.pos)
                if not bullet == None:
                    self.sendShot(event.pos)
                
    def __drawAllSprites(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        zeichnet die Sprites
        Parameter:      -      
        return values:  -
        '''
        
        #self.allPlayers.draw(self.screen)
        self.drawBots.draw(self.screen)
        self.allBullets.draw(self.screen)
        if int(self.player1.room) == 0:
            self.allWeapons.draw(self.screen)
            self.allDoors0.draw(self.screen)
            self.screen.blit(self.shaderScreen, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        #self.allDoors.draw(self.screen)
        else:
            self.allDoors1.draw(self.screen)

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
        if bullet != None:
            bulletPos = bullet.bulletFligthPositions
            hitPlayer = False

        
            for bulletposition in bulletPos:
                if hitPlayer:
                    pass
                elif not self.mymap.isPositionValid(bulletposition[0], bulletposition[1]):
                    removeBullets.append(bullet)
                elif bulletposition[0] > self.mymap.getWidth() or bulletposition[1] > self.mymap.getHeight():
                    removeBullets.append(bullet)
                elif bulletposition[0] < 0 or bulletposition[1] < 0:
                    removeBullets.append(bullet)
                else:
                    for player in self.allPlayers:
                        if player.rect.collidepoint(bulletposition) and player.nick != bullet.playernick:
                            hitPlayer = True
                            #removeBullets.append(bullet)

                
        for bullet in removeBullets:
            self.removeBullet(bullet)
        for player in removePlayers:
            self.removePlayer(player)

    def removeBullet(self, bullet):
        '''
        entfernt ein Bulletobjekt aus der Bulletgruppe
        Parameter:      Bulletobjekt
        return values:  -
        '''
        self.allBullets.remove(bullet)

    def removePlayer(self, player):
        '''
        nimmt einen Spieler aus der Playergruppe heraus
        Parameter:      Spielerobjekt
        return values:  -
        '''
        print 'player:', player.nick, 'wird aus dem Spiel entfernt'
        self.allPlayers.remove(player)
        
    def sendPos(self, position):
        '''
        sendet ueber den Client die X und Y Position des Spielers an den Server
        Parameter:      position, x und y position des Spielers
        return values:  -
        '''
        self.c.sendPos(position)

    def sendShot(self, eventPosition):
        '''
        sendet ueber den Client die Position und das Ziel des Schusses des Spielers an den Server
        Parameter:      playerPosition, Koord des Spielers
                        eventPosition, Koord des Zieles des Schusses
        return values:  -
        '''
        self.c.sendShot(eventPosition)

                
if __name__ == "__main__":
    Game()
