# -*- coding: cp1252 -*-
#Datum :    07-14.12.16
#Autor/en:  Kerim, Till, Lucas V.
#Version:   1.0

import math

class Game():    
    def __init__(self):
        '''
        Initialisation vom Game
        Achtet durchgehend, welche Spieler noch leben, bewegt die Schuesse,
        achtet auf Kollisionen und zeigt die Spielerpositionen
        Beendet das Spiel sobald nur noch ein Spieler am leben ist
        Parameter:      rect
                            int mit der distanz nach links
                            int mit der disanz nach oben
                            int width von dem Objekt
                            int heigth von dem Objekt
                        Float speed von der Bullet (Bewegungsgeschwindigkeit)
                        Float damage von der Bullet
        return values:  -
        '''
        self.players = [] #liste mit Objekten(Players)
        self.activeShots = [] #liste aus objekten(shots)

        while 1:
            self.updateAllPlayers()
            self.updateAllShots()
            if len(players) == 1:
                self.endGame()
     
    def updateAllPlayers(self):
        '''
        updatet die Spielerpositionen
        Parameter:      -
        return values:  -
        '''
        for player in self.players:
            if player.hitpoints > 0:
                self.getPlayerPosition(player)
                
                
    def updateAllShots(self):
        '''
        updatet die Bullets
        Parameter:      -
        return values:  -
        '''
        for bullet in self.aktiveShots:
            bullet.move()
            self.__handleCollision(bullet)
            
            
    def getPlayerPosition(self, player):
        '''
        gibt die Position eines Spielers
        Parameter:      Spielerobjekt
        return values:  Tuple (int, int), position eines Spielers
        '''
        return player.getPosition()

    def addShot(self, bullet):
        '''
        fuegt ein Bulletobjekt der activeShots liste hinzu
        Parameter:      Bulletobjekt
        return values:  -
        '''
        self.activeShots.append(bullet)
            
    def __handleCollision(self, bullet):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        ueberprueft ob ein Bulletobjekt in einem Mapobjekt oder einem Spieler, zieht einem Spieler Hitpoints ab
        und entfernt die Bullet bei einer Kollision
        Parameter:      Bulletobjekt
        return values:  -
        '''
        bulletRect = bullet.getRect() # <-- Position mit umfang!
        if bulletRect in self.wallCoordinates:# <-- wallcoords/Objekte werden gebraucht & abgleich mit denen, kp ob das so funktioniert
            self.activeShots.remove(bullet)
        for i in range(len(self.players)):
            if bulletRect == players[i].getRect(): #abbleich mit den Rectzeugs (pygame.rect dokumentation)
                self.playerIsHit(players[i], bullet) 
            self.playerIsHit()
            self.activeShots.remove(bullet)
    
    def playerIsHit(self, player, bullet):
        '''
        zieht einem Spielerobjekt, das von einem Bulletobjekt getroffen wurde
        Hitpoints ab
        Parameter:      Spielerobjekt, getroffener Spieler
                        Bulletobjekt, Bullet, die den Spieler getroffen hat
        return values:  -
        '''
        newHp = player.getHitpoints() - bullet.getDamge()
        player.setHitpoints(newHp)
    
    def addPlayer(self, player):
        '''
        fuegt einen Spieler der playerliste hinzu
        Parameter:      Spielerobjekt
        return values:  -
        '''
        self.players.append(player)

    def removePlayer(self, player):
        '''
        nimmt einen Spieler aus der playerliste heraus
        Parameter:      Spielerobjekt
        return values:  -
        '''
        self.players.remove(player)

    def endGame(self):
        '''
        Spielende, nur noch ein Spieler lebt
        Punkteverteilung sollte hier kommen
        Parameter:      -
        return values:  -
        '''
        print 'das Spiel ist zuende und gewonnen hat: ' + str(players[0]), + '!'
