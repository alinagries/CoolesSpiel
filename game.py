# -*- coding: cp1252 -*-
#Datum :    07-09.12.16
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
- PlayerObjekte mit
    - nick, position, Blickrichtung, hp, speed und weapon
    - Aktive schuesse (Position, Vektor ueber addShot)
    - Map (Waende, damit der Schuess nur bis zur Wand fliegt)
'''

class Game():
    #Startet das Spiel, gibt Startpositionen durch
    #achtet DURCHGEHEND wo die lebenden Spieler sind
    #Bei einem Schuss, wird geprueft ob und wer getroffen wurde, (bei einer toetung wird er ausm Spiel genommen)
    #Beendet das Spiel, sobald nur noch ein Spieler lebt
    
    def __init__(self):
        self.players = [] #liste mit Objekten(Players)
        self.activeShots = [] #liste aus objekten(shots)

        while 1:
            self.updateAllPlayers()
            self.updateAllShots()
            if len(players) == 0:
                self.endGame()
     
    def updateAllPlayers(self):
        for player in self.alivePlayers:
            self.getPlayerMovement(player)
            zeige das den clients z.T. kp wie #absichtlich kein Kommentar, damit das beim probieren sofort gefunden wird!
    
    def updateAllShots(self):
        for bullet in self.aktiveShots:
            bullet.move()
            self.__handleCollision(bullet)
            
            
    def getPlayerMovement(self, player):
        #returnt x,y Koordinate (Tuple) und Blickrichtung (Int, Int)
        position = self.getPlayerPosition(player)
        direction = self.getPlayerDirection(player)#Blickrichtung
        return position, direction

    def getPlayerPosition(self, player):
        #returnt die x,y Koordinaten vom Player als Tuple (Int, Int)
        return player.getPosition()
        
    def getPlayerDirection(self, player):
        #returnt die Blickrichtung vom Player, als Tuple (Int, Int)
        return player.getDirection()


    def addShot(self, bullet):
        self.activeShots.append(bullet)
            
    def __handleCollision(self, bullet):
        #hole die Positionen der Shots & prueft fuer jede Kugel ob sie in einer Wand, oder einem Spieler ist
        #falls ja, nimm den shot raus beim Spiler wird hp abgezogen & ueberpruefung ob er Tod ist
        bulletPos = bullet.getPosition()
        if bulletPos in self.wallCoordinates:# <-- wallcoords muessen erst iwie geholt werden
            self.activeShots.remove(bullet)
        for i in range(len(self.players)):
            if bulletPos == players[i].getPosition():# <-- playerumfang fehlt noch sonst muesste man einen
                self.playerIsHit(players[i], bullet) # bestimmten Pixel treffen
            self.playerIsHit()
            self.activeShots.remove(bullet)
    
    def playerIsHit(self, player, bullet):
        newHp = player.getHitpoints() - bullet.getDamge()
        player.setHitpoints(newHp)
        if newHp <= 0:
            self.players.remove(player)

    def alivePlayers(self):
        alivePlayers = []
        for alivePlayer in self.players:
            if aliveplayer.getHitpoints > 0:
                alivePlayers.append(alivePlayer)
        return alivePlayers
    
    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, player):
        self.players.remove(player)

    def endGame(self):
        print 'das Spiel ist zuende und gewonnen hat: ' + str(players[0]), + '!'
