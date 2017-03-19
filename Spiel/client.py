from threading import *
from time import clock
from socket import *
import struct
import ast


class Client(Thread):
    def __init__(self, parent):
        Thread.__init__(self)
        self.deamon = True
        self.parent = parent
    
        MCAST_GRP = '224.1.1.1'
        MCAST_PORT = 5000
        self.sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind(('', MCAST_PORT))  # use MCAST_GRP instead of '' to listen only to MCAST_GRP, not all groups on MCAST_PORT
        mreq = struct.pack("4sl", inet_aton(MCAST_GRP), INADDR_ANY)
        self.sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)


        self.SERVER_PORT = 5000
        self.SERVER_HOST = "localhost"
        self.socket = socket( AF_INET, SOCK_STREAM)
        self.socket.connect( (self.SERVER_HOST, self.SERVER_PORT) )
        self.ipAtServer = self.socket.recv(1024)
        
        self.start()

    def run(self):
        while True:
            data = self.sock.recv(1024)
            #print(data)
            
            if data.startswith('p'):
                data = data[3:-1]
                data.replace(" ", "")
                data.replace("'", "")
                self.parent.updatePlayers(data.split(','))
            elif data.startswith('s'):
                self.parent.shoot(data[2:].split(';')[0], ast.literal_eval(data[2:].split(';')[1]))
            elif data.startswith('n'):
                self.parent.setPlayerlist(ast.literal_eval(data[2:]))
            elif data.startswith('d'):
                self.parent.playerDied(data[2:])
            elif data.startswith('r'):
                self.parent.changeRoom(data[2:].split("|"))
            else:
                print('Client recieved bad data "{0}"'.format(data))

            
    def sendShot(self, eventPosition):
        convertedShot = self.convertPositionToString(eventPosition)
        #print("sending shot " + convertedShot)
        self.socket.send('/SHOOT '+ convertedShot + '\n')
        
    def sendPos(self, pos):
        convertedPosition = self.convertPositionToString(pos)
        self.socket.send('/UPDATEPOS ' + convertedPosition + '\n')

    def convertPositionToString(self, position):
        '''
        bekommt eine Position eines Spieler und wandelt diese um
        bsp.: (12,7) -> "012_007"
        Parameter:      position
        return values:  convertedPosition, 7 Zeichen langer String der Position
        '''
        xPos = position[0]
        yPos = position[1]
        convertedPosition = str(xPos).zfill(3) + '_' + str(yPos).zfill(3)
        return convertedPosition
