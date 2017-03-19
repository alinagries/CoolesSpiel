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
import ast
 
'''erstelle das Fenster'''

 
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
        self.screenWidth = self.mymap.getWidth()
        self.screenHeight = self.mymap.getHeight()
        self.screen = pygame.display.set_mode([self.screenWidth, self.screenHeight])
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
        self.player1 = Player()
        self.player1.nick = self.c.ipAtServer
        self.playerList = []
        self.player1.rect.x = 20
        self.player1.rect.y = 20
        self.allPlayers.add(self.player1)
        self.clock = pygame.time.Clock()
        self.screen.blit(self.background, [0,0])
        self.__drawAllSprites()
        pygame.display.flip()
        
        self.__startGame()
         
 
    def setPlayerlist(self, x):
        self.playerList = x
        for botnick in self.playerList:
            self.createBot(botnick)
        self.checkAllBots()
         
         
    def __startGame(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        startet das Spiel und achtet durchgehend, welche Spieler noch leben, bewegt die Schuesse,
        achtet auf Kollisionen und zeigt die Spielerpoitionen
        Beendet das Spiel sobald das Fenster geschlossen wurde
        Parameter:      -
        return values:  -
        '''
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
 
    def __deleteAllBots(self):
        '''
        loescht alle Bots
        Parameter:      -
        return values:  -
        '''
        removeBots = []
        for bot in self.allBots:
            removeBots.append(bot)
        for removeBot in removeBots:
            self.allBots.remove(removeBot)
 
    def createWeapons(self):
        '''
        soll eine Liste mit positionen bekommen und daraus rechtecke machen, die gezeichnet werden
        '''
        pass
 
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
            if bot.nick == ip and bot.room == self.player1.room:
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
        for playerCoord in allPlayerCoords:
            self.moveBot(playerCoord, self.playerList[allPlayerCoords.index(playerCoord)])


    def changeRoom(self, data):
        print 'changeRoom'
        nick = data[0]
        newRoom = data[1]
        newPosition = self.convertStringsToPositions([data[2]])
        newPos = newPosition[0]
        
        for bot in self.allBots:
            if str(self.player1.nick) == nick:
                self.player1.setRoom(newRoom)
                self.player1.rect.center = newPos
                self.changeBackround(newRoom)
            if str(bot.nick) == nick:
                bot.room = newRoom
        self.checkAllBots()

    def checkAllBots(self):
        self.drawBots.empty()
        for bot in self.allBots:
            if bot.room == self.player1.room:
                self.drawBots.add(bot)
                
        
                
    def changeBackround(self, newRoom):
        self.myRoom  = self.rooms[int(newRoom)]
        self.mymap   = self.myRoom.col

        mapPath = newRoom + ".png" 
##
##        self.screen = pygame.display.set_mode([self.mymap.getWidth(), self.mymap.getWidth()])
##        #pygame.key.set_repeat(1,10)
##        self.background = pygame.image.load(mapPath).convert()
##

        self.background = self.myRoom.getBg().convert()
        #self.allWeapons.empty()
        #self.allDoors.empty()
        self.allBullets.empty()
        print 'nach changeRoom'
    
     
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
        #self.allWeapons.draw(self.screen)
 
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
            elif not self.mymap.isPositionValid(bulletposition[0], bulletposition[1]):
                removeBullets.append(bullet)
            elif bulletposition[0] > self.mymap.getWidth() or bulletposition[1] > self.mymap.getHeight():
                removeBullets.append(bullet)
            elif bulletposition[0] < 0 or bulletposition[1] < 0:
                removeBullets.append(bullet)
            else:
                for player in self.allBots:
                    if player.rect.collidepoint(bulletposition) and player.nick != bullet.playernick:
                        hitPlayer = True
                        removeBullets.append(bullet)
##                      #das wird nur beim Server berechnet!
##                      player.isHit(bullet.damage)
##                      if player.hp <= 0:
##                      removePlayers.append(player)
                 
        for bullet in removeBullets:
            self.removeBullet(bullet)
##        for player in removePlayers:
##            self.removePlayer(player)
 
    def removeBullet(self, bullet):
        '''
        entfernt ein Bulletobjekt aus der Bulletgruppe
        Parameter:      Bulletobjekt
        return values:  -
        '''
        #print 'bullets:', self.allBullets.sprites()
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
