from threading import RLock
import threading
from game import Game


a=RLock()
b=RLock()
b.acquire()


class GameLogic:
    def __init__(self, players):
        #self.game = Game()
        self.players = players
        self.playerPositions = []

    def onTick(self):
        while 1:
            line = "p"
            for pos in self.playerPositions:
                line = line + "_" + str(pos)
            for player in self.players:
                player.send(positions)

    def shoot(self, clickedPos, aktPos):
        shot = str(clickedPos) + "_" + str(aktPos)
        for player in self.players:
            player.send("s_" + shot)

    def updatePlayerPosition(self, nick, newPosition):
        index = self.players.index(nick)
        self.playerPositions[index] = newPosition
        
##      regeln wir in der Lobby
##    def getAllPlayerNames(self):
##        line = ""
##        for player in self.game.players:
##            line = line + player.name + " "
##        return line


class GameListener:
    def __init__(self):



    def listen(self):
        
        
    

