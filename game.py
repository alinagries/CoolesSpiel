# -*- coding: cp1252 -*-
#Datum :    07-14.12.16
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

'''
Todo:
 -DC und reconnect einbauen (bsp. nach 10 sec dc wird sein hp auf 0 gesetzt und ist auch in der naechsten runde 0,
    bis er sich reconnected, dann kann er ab einer neuen Runde weiterspielen)
 -dauernde Kommunikation mitm Client (ich glaub Alina arbeitet grad dadran)
 -Den Server, mit den IPs verwalten/einrichten oder wie auch immer das heisst (ich glaub Alina arbeitet dadran)
 -generell ob die Kommentare stimmen
 -Ovidiu fragen, was er noch alles hier haben will
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
            if len(players) == 1:
                self.endGame()
     
    def updateAllPlayers(self):
        for player in self.players:
            if player.hitpoints > 0:
                self.getPlayerMovement(player)
                #An die Clients weitergeben
                #Waffen direction muss auch geholt werden, fuer die Grafik & an Clients geschickt werden
    
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

        bulletRect = bullet.getRect() # <-- Position mit umfang!
        if bulletRect in self.wallCoordinates:# <-- wallcoords/Objekte werden gebraucht & abgleich mit denen, kp pb das so funktioniert
            self.activeShots.remove(bullet)
        for i in range(len(self.players)):
            if bulletRect == players[i].getRect():#abbleich mit den Rectzeugs (pygame.rect dokumentation)
                self.playerIsHit(players[i], bullet) 
            self.playerIsHit()
            self.activeShots.remove(bullet)
    
    def playerIsHit(self, player, bullet):
        newHp = player.getHitpoints() - bullet.getDamge()
        player.setHitpoints(newHp)
    
    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, player):
        self.players.remove(player)

    def endGame(self):
        print 'das Spiel ist zuende und gewonnen hat: ' + str(players[0]), + '!'
