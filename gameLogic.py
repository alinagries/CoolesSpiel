from threading import RLock
import threading
from game import Game


a=RLock()
b=RLock()
b.acquire()


class GameLogic:
    def __init__(self, playerCount):#, players):
        self.players = [] #players
        self.playerCount = playerCount
        self.playerConnectedCount = 0
        self.sendMethods = []
        self.playerPositions = []
        self.gameStarted = False
        print('Waiting for all players to connect')

##    def waitForPlayers(self):
    def sendToPlayer(self, ip, data):
        self.sendMethods[self.players.index(ip)](data)
    
    def addActivePlayer(self, ip, method):
        self.players.append(ip)
        self.sendMethods.append(method)
        self.playerConnectedCount += 1
        print('Player' + str(ip) + 'connected, ' + self.playerConnectedCount + '/' + self.playerCount + 'connected')
        if self.playerCount==self.playerConnectedCount:
            print('All players connected, starting game')
            self.startGame()

    def startGame(self):
        for player in self.players:
            player.sendToPlayer('GAMESTARTING')
        self.gameStarted = True
        t = threading.Thread(target = self.onTick)
        t.daemon = True
        
    def onTick(self):
        while 1:
            line = "p"
            for pos in self.playerPositions:
                line = line + "_" + str(pos)
            for player in self.players:
                player.sendToPlayer(positions)

    def shoot(self, clickedPos, aktPos, ip):
        shot = str(clickedPos) + "_" + str(aktPos) + "_" + ip
        for player in self.players:
            player.sendToPlayer("s_" + shot)

    def updatePlayerPosition(self, newPosition, ip):
        index = self.players.index(ip)
        self.playerPositions[index] = newPosition
        
##      regeln wir in der Lobby
##    def getAllPlayerNames(self):
##        line = ""
##        for player in self.game.players:
##            line = line + player.name + " "
##        return line
    

