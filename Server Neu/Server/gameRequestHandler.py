## Ergaenzt am 08.12.16 von L.H.

from threading import *
from Queue import Queue
import SocketServer

class GameRequestHandler(SocketServer.StreamRequestHandler):
    def __init__(self, request, client_address, server):
        self.ip = client_address
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
        
    def setup(self):
        self.server.game.addActivePlayer(self.ip, self.sendToClient)
        SocketServer.StreamRequestHandler.setup(self)
        print "%s:%d connected" % self.client_address
        
    def finish(self):
        self.server.game.removePlayer(self.ip)
        SocketServer.StreamRequestHandler.finish(self)
        print "%s:%d disconnected" % self.client_address
        
    def handle(self):
        while 1:
            line = self.rfile.readline()
            if not line:
                break
            line = line.strip()
            if line.upper().startswith("/QUIT"):
                self.finish()
            if line.upper().startswith("/LOGIN"):
                """Falls wir mal Usernames einfuehren"""
                #self.IP = line.split()[1]
                #self.server.login.requestLogin(self.IP = line.split()[1])
                continue
            if line.upper().startswith("/MOVE"):
                self.server.game.make_lobby(self.ip, line.strip()[1])
            if line.upper().startswith("/SHOOT"):
                self.server.game.join_lobby(self.ip, line.strip()[1])
            if line.upper().startswith("/LEAVE"):
                self.server.game.join_lobby(self.ip)
            if line.upper().startswith("/MSG"):
                #bald
                pass
                
    def sendToClient(self, data):
        print "sendAnswer aus",self.client_address
        self.wfile.write(data)
