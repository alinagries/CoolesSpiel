
from threading import *
from Queue import Queue
import SocketServer

class GameRequestHandler(SocketServer.StreamRequestHandler):
    def __init__(self, request, client_address, server):
        self.ip = client_address
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
        
    def setup(self):
        SocketServer.StreamRequestHandler.setup(self)
        self.server.game.addActivePlayer(self.ip, self.sendToClient)
        print "%s:%d connected" % self.client_address
        
    def finish(self):
        self.server.game.removePlayer(self.ip)
        SocketServer.StreamRequestHandler.finish(self)
        print "%s:%d disconnected" % self.client_address
        
    def handle(self): #Platzhalter, muss noch abgesprochen werden
        while 1:
            print("hadnlin")
            line = self.rfile.readline()
            print line
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
            if line.upper().startswith("/UPDATEPOS"): #playerposition: Nickname, Position
                self.server.game.updatePlayerPosition(line.split()[1], self.ip)
            if line.upper().startswith("/SHOOT"): #schuss: Schussrichtung Spielername
                print("TEST 0")
                self.server.game.shoot(line.split()[1],line.split()[2],self.ip)
##            if line.upper().startswith("/ALLPLAYERS"): #AlleSpieler: lobby_name??
##                self.sendToClient(self.server.game.getAllPlayersName())
##            if line.upper().startswith("/GETWEAPON"): #GibWaffe Nickname
##                self.sendToClient(self.server.game.getPlayersWeapon(line.split[1]))
            else:
                continue


    def sendToClient(self, data):
        print "sendAnswer aus",self.client_address
        self.wfile.write(data)
