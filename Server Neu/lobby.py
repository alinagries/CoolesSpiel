## 08.12.16 L.H.

#from gameRequestServer import GameRequestServer


class Lobby:
    def __init__(self, master, owner, name):
        self.master = master
        self.owner = owner
        self.name = name
        self.players = []

    def join(self, player):
        self.players.append(player)

    def leave(self, player):
        self.players.remove(player)
        if player is self.owner:
            if not self.players:
                self.master.delete_lobby(self)
            else:
                self.owner = self.players[0]

    def interact(self, interaction, arguments):
        '''Fuer Einstellungen, Ownerrechte, Start usw.'''
        if interaction == 'START':
            gameServer = MyGameServer(('localhost', 5005), GameRequestHandler)
            for player in self.players:
                self.master.send(player, ('localhost', 5005))
                self.master.server.game.giveServer(gameServer)
                print self.players
                #self.master.server.game.setplayer(self.players)
        
