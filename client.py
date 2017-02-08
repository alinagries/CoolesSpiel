from threading import *
from time import *
from socket import *

class Client(Thread):
    def __init__(self,s):
        Thread.__init__(self)
        self.socket = s
        self.aktiv=1
        self.data=""
        self.start()

##        self.SERVER_PORT = 5000 
##        self.SERVER_HOST = "localhost"
##        self.socket=socket( AF_INET, SOCK_STREAM)
##        self.socket.connect( (self.SERVER_HOST, self.SERVER_PORT) )
##        print self.socket

    def run(self):
        while self.aktiv:
            self.data = self.socket.recv(1024)
            #self.data=self.socket.readline()
            if self.data.startswith('s'):
                self.parent.shoot(self.data[2:].split('_'))
            else:
                self.parent.updatePlayers(self.data[2:].split('_'))
            self.notify()
            sleep(1.0)
            
            
    def sendShot(self, ip, shot):
        self.socket.send('/SHOOT '+ shot + " " + ip)
        #print "hallo"
        
    def sendPos(self, ip, pos):
        self.socket.send('/UPDATEPOS '+ pos + " " + ip )

    def stop(self):
        self.aktiv=0
    
    def anmelden(self,obj):
        self.observer.append(obj)

    def abmelden(self,obj):
        try:
            self.observer.delete(obj)
        except:
            pass
        
    def notify(self):
        



    def holeMessage(self):
        return self.data[0:len(self.data)-2]
        
            
