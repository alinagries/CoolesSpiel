# -*- coding: cp1252 -*-
#Datum :    07-14.12.16
#Autor/en:  Kerim, Till, Lucas V.
#Version:   1.0

#import gamemap
import math
import player

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
        self.traps = []

        while len(players) > 1:
            self.__updateAllPlayers()
            self.__updateAllShots()
            self.__updateAllTraps()
        self.__endGame()

    def setPlayers(self,players):
        for player in players:
            p = Player(players[1])
            self.players.append(p)

##    def updatePlayerposition(self, nick, pos):
##        for player in self.players:
##            if player.nick == name:
##                player.setPosition(pos)
            
    def __updateAllPlayers(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        updatet die Spielerpositionen
        Parameter:      -
        return values:  -
        '''
        for player in self.players:
            if player.hitpoints > 0:
                self.__getPlayerPosition(player)
                
    def __updateAllShots(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        updatet die Positionen der Bullets und bearbeitet Kollisionen
        Parameter:      -
        return values:  -
        '''
        for bullet in self.aktiveShots:
            bullet.move()
            self.__handleCollision(bullet)
        
    def __updateAllTraps(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        ueberprueft ob ein Spieler auf einr trap steht -> auloesung des trap
        Parameter:      -
        return values:  -
        '''
        for trap in self.traps:
            self.__handleTrap(trap)
            
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
        for player in self.players:
            if bulletRect == player.getRect(): #abbleich mit den Rectzeugs (pygame.rect dokumentation)
                player.isHit(bullet.getDamage()) 
                self.activeShots.remove(bullet)
            
    def __handleTrap(self, trap):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        ueberprueft ob ein Trapobjekt bei einem Spieler steht, loest die Trap ggf. aus und richted
        im radius schaden an, Trap wird dann entfernt
        Parameter:      Trapobjekt
        return values:  -
        '''
        if trap.exploded():
            explotionPositions = trap.getExplotionPositions()
            for player in self.players:
                if player.getRect() in explotionPositions():#ich bezweifel, dass das mit getRect funktionieren wird...
                    player.isHit(trap.getDamage())
            self.removeTrap(trap)
        elif trap.activated():
            triggerPositions = trap.getTriggerPositions()
            for player in self.players:
                if player.getRect() in triggerPositions: #ich bezweifel, dass das mit getRect funktionieren wird...
                    trap.trigger()        
            
    def __getPlayerPosition(self, player):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
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
        
    def addTrap(self, trap):
        '''
        fuegt einen trap der Trapliste hinzu
        Parameter:      Spielerobjekt
        return values:  -
        '''
        self.traps.append(trap)
        
    def removeTrap(self, trap):
        '''
        nimmt einen trap aus der trapliste heraus
        Parameter:      trap objekt
        return values:  -
        '''
        self.traps.remove(trap)
    
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

    def __endGame(self):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        Spielende, nur noch ein Spieler lebt
        Punkteverteilung sollte hier kommen
        Parameter:      -
        return values:  -
        '''
        print 'das Spiel ist zuende und gewonnen hat: ' + str(players[0]), + '!'


            

            
