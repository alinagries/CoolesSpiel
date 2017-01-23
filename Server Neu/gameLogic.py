from threading import RLock
from game import Game


a=RLock()
b=RLock()
b.acquire()


class GameLogic(self, players):
    def __init__(self):
        self.game = Game()
        self.players = players
        #self.setPlayers()
        self.playerPositions = []


    def onTick(self):
        #line = ""
        positions = [line + str(pos) for pos in self.playerPositions]
        for player in self.players:
            player.send(positions)



    def setPlayers(self):
        self.game.setPlayers(self.players)

        
    def updatePlayerPosition(self,data):
        '''
        Wird von gameReqestHandler aufgerufen.
        Updated die Positionen eines Spielers aus der GUI.
        Parameter: data (Eine Liste aus Tupeln, die aus Nickname und Position des Spielers zusmgesetzt sind)
        Rückgabewerte: -
        '''
        nick = data[0]
        pos = data[1]
        for player in self.game.players:
            if player.nick == name:
                player.setPosition(pos)
                self.playerPositions[self.players.index(player)] = pos
                

    def shoot(self, direction, nick):
        '''
        Wird vom gameRequesthandler aufgerufen.
        Parameter: direction (der Kugel)
                   nick (name des Players)
        Rückgabewerte : -
        '''
        for player in self.game.players:
            if player.nick == nick:
                bullet = player.shoot(player.position, direction)
        self.game.addShot(bullet)
        self.game.shoot()


    def getAllPlayerNames(self):
        line = ""
        for player in self.game.players:
            line = line + player.name + " "
        return line


    def getPlayersWeapon(self, nick):
        for player in self.game.players:
            if player.nick == nick:
                return player.weapon.getName()


    def updatePlayer(self, nick):
        for player in self.game.players:
            if player.nick == nick:
                return player.getPosition() + "," + player.getHitPoints()
    

