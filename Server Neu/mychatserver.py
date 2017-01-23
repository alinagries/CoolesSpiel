## Ergaenzt am 12.12.16 von L.H.

from threading import *
import SocketServer
from lobby_master import LobbyMaster
from game_logic import GameLogic

class MyGameServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_address = 1
    def __init__(self,server_address,request_handler_Class):
        SocketServer.TCPServer.__init__(self,server_address,request_handler_Class)
        self.game = GameLogic()

class MyLoginServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_adress = 1
    def __init__(self,server_address,request_handler_Class):
        SocketServer.TCPServer.__init__(self,server_address,request_handler_Class)
        self.login = login()
