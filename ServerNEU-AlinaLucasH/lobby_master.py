## 08.12.16 L.H.


from lobby import Lobby
from threading import Lock

class LobbyMaster():
    def __init__(self):
        self.lobbys = []
        self.lobby_names = []
        
        self.clients = []
        self.client_lobby = []
        self.client_methods = []

        self.lobby_lock = Lock()
        self.client_lock = Lock()



    def ifClientExists(self, client):
        if not client in self.clients:
            print Warning('[** client "' + str(client) + '" is not registrated properly **]')
            return 0
        else:
            return 1

    def send(self, client, data):
        index = self.clients.index(client)
        meth = self.client_methods[index]
        meth(data)

    def addClient(self, client, method):
        if not client in self.clients:
            self.client_lock.acquire()
            
            self.clients.append(client)
            self.client_lobby.append(None)
            self.client_methods.append(method)
            
            self.client_lock.release()
        else:
            return Warning('[** Client "' + client + '" already exsits **]')

    def removeClient(self, client):
        if self.ifClientExists(client):
            self.client_lock.acquire()
            index = self.clients.index(client)
            del self.clients[index]
            del self.client_lobby[index]
            del self.client_methods[index]
            self.client_lock.release()

    def get_lobbys(self, client):
        self.send(client, self.lobby_names)
        print self.clients
        print self.lobby_names
        print self.client_lobby

    def make_lobby(self, client, lobby_name):        
        if self.ifClientExists(client):
            if lobby_name in self.lobby_names:
                return Warning('[** lobbyname "' +  lobby_name + '" already exists **]')
            self.lobby_lock.acquire()
            new_lobby = Lobby(self, client, lobby_name)
            self.lobby_names.append(lobby_name)
            self.lobbys.append(new_lobby)
            
            self.lobby_lock.release()
            
            self.join_lobby(client, lobby_name)

    def delete_lobby(self, lobby):
        self.lobby_lock.acquire()
        
        self.lobby_names.remove(lobby.name)
        self.lobbys.remove(lobby)
        del lobby
        
        self.lobby_lock.release()

    def join_lobby(self, client, lobby_name):
        if self.ifClientExists(client):
            
            index = self.clients.index(client)
            if not self.client_lobby[index] == None:
                return Warning('[** client "' + str(client) + '" already joined a lobby **]')
            
            if lobby_name in self.lobby_names:
                self.lobbys[ self.lobby_names.index(lobby_name) ].join(client)
                self.client_lobby[index] = lobby_name
            else:
                return Warning('[** lobbyname "' +  lobby_name + '" does not exist **]')

    def leave_lobby(self, client):
        if self.ifClientExists(client):
            index = self.clients.index(client)
            
            if not self.client_lobby[index] == None:
                lobby = self.lobbys[ self.lobby_names.index( self.client_lobby[index] ) ]
                lobby.leave(client)
                self.client_lobby[index] = None
            else:
                return Warning('[** Client "' + client + '" is not in a lobby **]')


    def lobby_interaction(self, client, interaction, parameters):
        if self.ifClientExists(client):
            index = self.clients.index(client)
            
            if not self.cient_lobby[index] == None:
                lobby = self.lobbys[ self.lobby_names.index( self.client_lobby[index] ) ]
                lobby.interact(interaction, parameters)
            else:
                return Warning('[** Client "' + client + '" is not in a lobby **]')

        
