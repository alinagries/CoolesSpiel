from threading import *
from time import clock
from socket import *
import struct
import ast

import os
import sys


class Client(Thread):
    def __init__(self, parent):
        Thread.__init__(self)
        self.deamon = True
        self.parent = parent

        self.SERVER_PORT = 5000
        self.SERVER_HOST = "localhost"
        self.socket = socket( AF_INET, SOCK_STREAM)
        self.socket.connect( (self.SERVER_HOST, self.SERVER_PORT) )
        
        self.start()

    def run(self):
        while True:
            data = self.socket.recv(1024)
            #print(data)
            if not data:
                continue
            
            if data.startswith('sn'):
                data = data[3:]
                self.parent.setAllLobbys(ast.literal_eval(data))
            elif data.startswith('sg'):
                data = data[3:]
                t = Thread(target = lambda: os.system("gameServer_starten.py " + data + ' ' + str(5010) ))
                t.daemon = True
                t.start()
            elif data.startswith('gd'):
                data = data[3:]
                os.system("gameClient.py")

            else:
                print('Client recieved bad data "{0}"'.format(data))

            
    def getAllLobbys(self):
        self.socket.send('/GETLOBBYS' + "\n")

    def getIPByName(self, name):
        self.socket.send('/GETIPBYN ' + name + "\n")

    def registrateAsLobby(self, lobbyName):
        self.socket.send('/MAKELOBBY ' + lobbyName + "\n")

    def joinLobby(self, lobbyName):
        print lobbyName, "nichthallo"
        self.socket.send('/JOINLOBBY ' + lobbyName + "\n")

    def leaveLobby(self):
        pass

    def interactWithLobby(self, interaction, lobby):
        pass








        
        
