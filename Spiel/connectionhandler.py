# -*- coding: cp1252 -*-

#import gamemap
#import player
import random
#import vector
import threading
from socket import *


class ConnectionHandler:

    """
    Klasse für einen ConnectionHandler der vom Client benutzt wird,
    um mit dem Server zu kommunizieren
    """

    def __init__(self):
        """
        Initialisation eines ConnectionHandler

        Parameter:      -
        Rückgabewerte:  -
        """
        #self.gamemap    = gamemap.Gamemap()
        #self.p1           = player.Player("Spieler 1", (((random.randint(0, 200), random.randint(0, 200)),
        #                                           (30, 30)), (0, 0), 20, 1))
        #self.p2           = player.Player("Spieler 2", (((random.randint(0, 200), random.randint(0, 200)),
        #                                           (30, 30)), (0, 0), 20, 1))
        self.bullets = []
        self.socket = None

    def isGameRunning(self):
        """
        Zurückgeben ob ein client-beteiligtes Spiel am laufen ist

        Parameter:      -
        Rückgabewerte:  bool ob das Spiel am laufen ist
        """
        return self.gamemap
    
    def getGameMap(self):
        """
        Zurückgeben der benutzten GameMap in einem client-beteiligten Spiel

        Parameter:      -
        Rückgabewerte:  gamemap.Gamemap die benutze GameMap
        """
        return self.gamemap

    def getGamePlayers(self):
        """
        Zurückgeben aller Spieler in einem client-beteiligten Spiel

        Parameter:      -
        Rückgabewerte:  list eine Liste von Spielerobjekten (player.Player)
        """
        self.p2.rect.move_ip(random.randint(-2, 2), random.randint(-2, 2))
        return [self.p1, self.p2]

    def getGameBullets(self):
        """
        Zurückgeben aller Geschosse in einem client-beteiligten Spiel

        Parameter:      -
        Rückgabewerte:  list eine Liste von Spielerobjekten (player.Player)
        """
        return self.bullets

    ######## ÄNDERUNG DES AUFRUFES VORBEHALTEN/HÖCHSTWAHRSCHEINLICH: ########

    def move(self, direction):
        """
        Bewegen des eigenen Spielers in der angegebenen Richtung

        Parameter:      tuple ein Richtungsvektor aus zwei Koordinaten
        Rückgabewerte:  -
        """
        v = vector.Vector(direction[0], direction[1]).setLength(self.p1.speed)
        self.p1.rect.move_ip(v.x, v.y)

    ######## GESCHOSSE FLIEGEN NICHT!! ########

    def fire(self, direction):
        """
        Schießen der Waffe des eigenen Spielers

        Parameter:      tuple ein Richtungsvektor aus zwei Koordinaten
        Rückgabewerte:  -
        """
        self.bullets.append(self.p1.shoot(self.p1.weapon))
    
    def login(self):
        pass

    def poll(self):
        while self.socket != None:
            try:
                tag = "msg"
                message = self.socket.recv(1024)
                if message.upper().startswith("BROADCAST:"):
                    tag = "broadcast"
                elif message.upper().startswith("PRIVATE NACHRICHT VON"):
                    tag = "whisper"
                elif message.upper().startswith("DU FLUESTERST"):
                    tag = "whisper"
                print message
            except Exception as ex:
                print "Polling failed! Did the server stop?"
                print "    error message:", str(ex) 
                self.disconnect()
                return

    def send(self, message):
        if self.socket != None:
            try:
                self.socket.send(message + "\r\n")
            except Exception as ex:
                print "Sending failed! Did the server stop?"
                print "    error message:", str(ex)
                self.disconnect()
        else:
            print "Client is not connected to any Server!" 

    def connect(self, ip, port):
        if self.socket == None:
            try:
                self.socket = socket(AF_INET, SOCK_STREAM)
                self.socket.connect((str(ip), port))
                (ip, port) = self.socket.getpeername()
                print "Client conntected to", str(ip) + ":" + str(port) + "!"
                t = threading.Thread(target = self.poll)
                t.daemon = True
                t.start()
            except Exception as ex:
                print "Connection failed! Is there a server open on the given address?"
                print "    error message:", str(ex)
                self.socket = None
        elif (gethostbyname(ip), port) != self.socket.getpeername():
            self.disconnect()
            self.connect(ip, port)
        else:
            print "Client is already connected to the same Server!"

    def disconnect(self):
        if self.socket != None:
            try:
                self.socket.shutdown(SHUT_RDWR)
                self.socket.close()
                self.socket = None
                print "Client disconntected!" 
            except Exception as ex:
                print "Disconnection failed! Was the Client connected before?"
                print "    error message:", str(ex)
