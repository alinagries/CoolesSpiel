
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
        
    def handle(self): #Platzhalter, muss noch abgesprochen werden
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
##            if line.upper().startswith("/UPDATEPLAYER"):
##                self.sendToClient(self.server.game.updatePosition(line.split[1]))
            if linde.upper().startswith("/PLAYERPOSITION"): #playerposition: Nickname, Position
                self.server.game.updatePlayerPositions(line.split()[1:])
            if line.upper().startswith("/SHOOT"): #schuss: Schussrichtung Spielername
                self.server.game.shoot(line.split[1],line.split[2])
            if line.upper().startswith("/ALLPLAYERS"): #AlleSpieler: lobby_name??
                self.sendToClient(self.server.game.getAllPlayersName())
            if line.upper().startswith("/GETWEAPON"): #GibWaffe Nickname
                self.sendToClient(self.server.game.getPlayersWeapon(line.split[1]))
)

    def sendToClient(self, data):
        print "sendAnswer aus",self.client_address
        self.wfile.write(data)
