from threading import RLock
import threading
from time import sleep
#from game import Game
from thread import start_new_thread

class GameLogic:
    def __init__(self, playerCount):#, players):
        self.players = [] #players
        self.playerCount = playerCount
        self.playerConnectedCount = 0
        self.sendMethods = []
        self.playerPositions = ["12", "2"]
        self.gameStarted = False
        print('Waiting for all players to connect')

##    def waitForPlayers(self):
    def sendToPlayer(self, ip, data):
        self.sendMethods[self.players.index(ip)](data)
    
    def addActivePlayer(self, ip, method):
        self.players.append(ip)
        self.sendMethods.append(method)
        self.playerConnectedCount += 1
        print('Player' + str(ip) + 'connected, ' + str(self.playerConnectedCount) + '/' + str(self.playerCount) + ' connected')
        if self.playerCount==self.playerConnectedCount:
            print('All players connected, starting game')
            self.startGame()

    def startGame(self):
        #for player in self.players:
          #  self.sendToPlayer(player, 'GAMESTARTING')
        self.gameStarted = True
##        self.onTick()
##        t = threading.Thread(target = self.onTick)
##        t.daemon = True
        start_new_thread(self.onTick,())
        
    def onTick(self):
        while 1:
            sleep(3.0)
            line = "p"
            for pos in self.playerPositions:
                line = line + "_" + str(pos)
            print(line + " POSITIONS")
            for player in self.players:
                self.sendToPlayer(player, line)

    def shoot(self, clickedPos, aktPos, ip):
        print("TEST 1")
        shot = str(clickedPos) + "_" + str(aktPos) + "_" + str(ip)
        for player in self.players:
            self.sendToPlayer(player, "s_" + shot)

    def updatePlayerPosition(self, newPosition, ip):
        index = self.players.index(ip)
        self.playerPositions[index] = newPosition
        
##      regeln wir in der Lobby
##    def getAllPlayerNames(self):
##        line = ""
##        for player in self.game.players:
##            line = line + player.name + " "
##        return line
    

