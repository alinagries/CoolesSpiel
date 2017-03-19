## Ergaenzt am 12.12.16 von L.H.

from threading import *
import SocketServer
from lobby_master import LobbyMaster




class MyMasterServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    allow_reuse_adress = 0
    def __init__(self,server_address,request_handler_Class):
        SocketServer.TCPServer.__init__(self,server_address,request_handler_Class)
        self.login = LobbyMaster()


