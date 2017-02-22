from threading import *
from time import *
from socket import *

class Client(Thread):
    def __init__(self, parent):
        Thread.__init__(self)
        self.parent = parent
        
        self.data=""
        

        self.SERVER_PORT = 5000 
        self.SERVER_HOST = "localhost"
        self.socket=socket( AF_INET, SOCK_STREAM)
        self.socket.connect( (self.SERVER_HOST, self.SERVER_PORT) )
        
        self.aktiv=1
        self.start()

    def run(self):
        while self.aktiv:
            self.data = self.socket.recv(2048)
            print self.data, "DATA"
            if self.data.startswith('s'):
                self.parent.shoot(self.data[2:].split('_'))
            else:
                self.parent.updatePlayers(self.data[2:].split('_'))
            
    def sendShot(self, shot):
        self.socket.send('/SHOOT '+ shot + '\n')
        
    def sendPos(self, pos):
        self.socket.send('/UPDATEPOS ' + pos + '\n')
