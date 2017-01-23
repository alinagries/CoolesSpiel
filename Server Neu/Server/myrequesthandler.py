## Ergaenzt am 08.12.16 von L.H.

from threading import *
from Queue import Queue
import SocketServer

class MyRequestHandler(SocketServer.StreamRequestHandler):
    def __init__(self, request, client_address, server):
        self.ip = client_address
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
        
    def setup(self):
        self.server.login.addClient(self.ip, self.sendToClient)
        SocketServer.StreamRequestHandler.setup(self)
        print "%s:%d connected" % self.client_address
        
    def finish(self):
        self.server.login.removeClient(self.ip)
        SocketServer.StreamRequestHandler.finish(self)
        print "%s:%d disconnected" % self.client_address
        
    def handle(self):
        while 1:
            print 'handlin'
            line = self.rfile.readline()
            if not line:
                break
            line = line.strip()
            print line
            if line.upper().startswith("/QUIT"):
                self.finish()
            elif line.upper().startswith("/LOGIN"):
                """Falls wir mal Usernames einfuehren"""
                #self.IP = line.split()[1]
                #self.server.login.requestLogin(self.IP = line.split()[1])
                continue
            elif line.upper().startswith("/SHUTDOWN"):
                self.server.shutdown()
            elif line.upper().startswith("/MAKELOBBY"):
                self.server.login.make_lobby(self.ip, line.split()[1])
            elif line.upper().startswith("/JOINLOBBY"):
                self.server.login.join_lobby(self.ip, line.split()[1])
            elif line.upper().startswith("/LEAVELOBBY"):
                self.server.login.leave_lobby(self.ip)
            elif line.upper().startswith("/GETLOBBYS"):
                print '1'
                self.server.login.get_lobbys(self.ip)
                print 'end'
            elif line.upper().startswith("/LOBBYINTERACTION"):
                self.server.login.get_lobbys(self.ip, line.split()[1], line.split()[2])


    def sendToClient(self, data):
        print "sendAnswer aus",self.client_address
        self.wfile.write(data)
