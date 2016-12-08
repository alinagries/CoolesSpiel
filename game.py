# -*- coding: cp1252 -*-
#Datum :    07.12.16
#Autor/en:  Kerim, Till, Lucas V.
#Version:   1.0

import math

'''
Bitte ergaenzt fehlendes:

Wir machen:
- durchgehende weiterleitung der Positionen der lebenden Spieler an die Clients
- Berechnung der Flugbahnen der Schuesse (momentan alle 10p)
- Benachrichtigung an Spieler, wenn diese getroffen werden
- Spielstart
- Startpositionen der Spieler
- Spielende


Wir brauchen:
- Spielerposition und Blickrichtung
- alle Spieler an/abmelden mit login/logoutPlayers
- lebendeSpieler (an/abmelden in login/logoutAlivePlayers)
- Aktive schuesse (Position, Vektor ueber addShot)
- Map (Waende, damit der Schuess nur bis zur Wand fliegt)
- Raueme (welcher Spieler in welchem Raum ist, am besten auch mit an/abmelden der Spieler)
'''

class Game():
    #Startet das Spiel, gibt Startpositionen durch
    #achtet DURCHGEHEND wo die lebenden Spieler sind, und zeigt diese allen Spielern im selben Raum
    #Bei einem Schuss, wird gemeldet ob und wer getroffen wurde, (bei einer toetung wird dies gemeldet und der Spieler rausgenommen {in der Klasse Spieler})
    #Beendet das Spiel, sobald nur noch ein Spieler lebt
    
    def __init__(self):
        self.players = [] #liste mit IPs/Nicknames
        self.alivePlayers = [] #liste mit IPs/Nicknames
        self.activeShots = [] #liste aus objekten(shots)

        while 1:
            self.updateAllPlayers()
            self.updateAllShots()
     
    def updateAllPlayers(self):
        for player in self.alivePlayers:
            self.getPlayerMovement(player)
    
    def updateAllShots(self):
        for shot in self.aktiveShots:
            self.__calculateFlight(shot)
            
    def getPlayerMovement(self, player):
        #returnt x,y Koordinate (Tuple) und Blickrichtung (Int, Int)
        position = self.getPlayerPosition(player)
        direction = self.getPlayerDirection(player)#Blickrichtung
        return position, direction

    def getPlayerPosition(self, player):
        #returnt die x,y Koordinaten vom Player als Tuple (Int, Int)
        #von wo bekommen wir die?
    
    def getPlayerDirection(self, player):
        #returnt die Blickrichtung vom Player, als Tuple (Int, Int)
        #von wo bekommen wir die?


    def addShot(self, bullet):
        self.activeShots.append(bullet)
            
    def __calculateFlight(self, bullet):
        #hole die Positionen der Shots, und den Vektor
        #bewege die Kugeln & pruefe fuer jede Kugel ob Wand, oder Spieler getroffen wird
        #falls ja, nimm den shot raus, sonst Kugel weiterfliegen lassen
        #wenn ein Spieler getroffen wird, dies auch dem Spieler
        bullet.move()
        bullet.getPosition()
        if bullet.getPosition() in self.wallCoordinates:
            self.activeShots.remove(bullet)
        elif bullet.getPosition() in self.playerCoordinates:
            Player.hit(shot[3])#shot[3] = dmg
            self.activeShots.remove(bullet)

    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, player):
        self.players.remove(player)

    def addAlivePlayer(self, player):
        self.alivePlayers.append(player)

    def removeAlivePlayer(self, player):
        self.alivePlayers.remove(player)

    def updateAllShots(self):
        for shot in self.activeShots:
            self.__calculateFlight(shot)
