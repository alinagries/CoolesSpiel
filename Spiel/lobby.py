## 08.12.16 L.H.

#from gameRequestServer import GameRequestServer
from time import sleep

class Lobby:
    def __init__(self, master, owner, name):
        self.master = master
        self.owner = owner
        self.name = name
        self.players = []

    def join(self, player):
        self.players.append(player)
        if len(self.players) == 2:
            self.startGame()

    def leave(self, player):
        self.players.remove(player)
        if player is self.owner:
            if not self.players:
                self.master.delete_lobby(self)
            else:
                self.owner = self.players[0]

    def startGame(self):
        self.master.send(self.owner, 'sg.' + str(len(self.players)))
        sleep(3.0)
        for player in self.players:
            self.master.send(player, 'gd.' + str((self.owner[0], 5010)))

    def interact(self, interaction, arguments):
        '''Fuer Einstellungen, Ownerrechte, Start usw.'''
        if interaction == 'START':
            gameServer = MyGameServer(('localhost', 5005), GameRequestHandler)
            for player in self.players:
                self.master.send(player, ('localhost', 5005))
                self.master.server.game.giveServer(gameServer)
        
