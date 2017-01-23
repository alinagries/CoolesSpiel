# -*- coding: cp1252 -*-
#Datum :    11.12.16
#Autor/en:  Lucas V.
#Version:   1.0

import pygame

class Sector():
    def __init__(self, rect = (0, 0, 100, 100)):
        '''
        Initialisation von Sector
        Parameter:      rect
                            int mit der distanz nach links
                            int mit der disanz nach oben
                            int width von dem Objekt
                            int heigth von dem Objekt
        return values:  -
        '''
        self.rect = pygame.Rect(rect)
        
        self.objectives = []
        self.players = []
        #self.bullets = [] wird eher nicht gebraucht, sie muessen nur abfragen, was in dem Bereich ist

    def getRect(self):
        '''
        gibt rect (xKoord, yKoord, width, height) aus
        Parameter:      rect
                            int mit der distanz nach links
                            int mit der disanz nach oben
                            int width von dem Objekt
                            int heigth von dem Objekt
        return values:  -
        '''
        return self.rect

    def setRect(self, xKoordinate, yKoordinate, width, height):
        '''
        setzt rect (xKoord, yKoord, width, height)
        Parameter:      -
        return values:  -rect
                            int mit der distanz nach links
                            int mit der disanz nach oben
                            int width von dem Objekt
                            int heigth von dem Objekt
        '''
        self.rect = pygame.Rect(xKoordinate, yKoordinate, width, height)

    def getObjectives(self):
        '''
        gibt die ObjektListe aus
        Parameter:      -
        return values:  Liste von objekten
        '''
        return self.objectives
    
#    def setObjectives(self, objectives): Nutzung der Funktion nicht geplant
#        '''
#        setzt die ObjektListe auf Objekte
#        Parameter:      Objekte
#        return values:  -
#        '''
#        self.objectives = objectives
        
    def getPlayers(self):
        '''
        gibt die Spieler in diesem Sektor aus
        Parameter:      -
        return values:  Liste von Spielerobjekten
        '''
        return self.players
    
#    def setPlayers(self, players): Nutzung der Funktion nicht geplant
#        '''
#        setzt die Spieler auf den wert des Parameters
#        Parameter:      Liste von Spielerobjekten
#        return values:  -
#        '''
#        self.players = players
       
    def addObjective(self, objective):
        '''
        fuegt der Objektliste ein neues Objekt oder rect hinzu,
        ich weiss nicht wie das aussieht
        Parameter:      Objekt (Gegenstaende?) oder Rects(?)
        return values:  -
        '''
        self.objectives.append(objective)
        
#    def removeObjective(self, objective): Nutzung der Funktion ist nicht geplant
#        '''
#        nimmt ein Objekt oder Rect aus der Objektliste heraus weiss nicht wie das aussehen soll
#        Parameter:      Objekt oder Rect
#        return values:  -
#        '''
#        self.objectives.remove(objective)
        
    def addPlayer(self, player):
        '''
        fuegt der Spielerliste einen neuen Spieler hinzu
        Parameter:      Spielerobjekt
        return values:  -
        '''
        self.players.append(player)
    
    def removePlayer(self, player):
        '''
        nimmt einen Spieler aus der Spielerliste heraus
        Parameter:      Spielerobjekt
        return values:  -
        '''
        self.players.remove(player)
        
    def getPosition(self):
        '''
        gibt die Position des Sektors aus
        Parameter:      -
        return values:  int x-Koordinate des Sektors
                        int y-Koordinate des Sektors
        '''
        return self.rect[0], self.rect[1]
    
#    def setPosition(self, newXCoord, newYCoord): Nutzung der Funktionist nicht geplant
#        '''
#        setzt die Position des Sektors
#        Parameter:      int neue x-Koordinate des Sektors
#                        int neue y-Koordinate des Sektors
#        return values:  -
#        '''
#        self.rect = pygame.Rect(newXCoord, newYCoord, self.rect[2], self.rect[3])

    def getSize(self):
        '''
        gibt die groesse des Sektors aus
        Parameter:      -
        return values:  int width des Sektors
                        int height des Sektors
        '''
        return self.rect[2], self.rect[3]
    
#    def setSectorsize(self, newWidth, newHeight):
#        '''
#        setzt die groesse des Sektors
#        Parameter:      int neue breite des Sektors
#                        int neue hoehe des Sektors
#        return values:
#        '''
#        self.sectorsize = newSize
        
