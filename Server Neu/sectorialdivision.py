# -*- coding: cp1252 -*-
#Datum :    11.12.16
#Autor/en:  Lucas V.
#Version:   1.0

import math
from sector import Sector

class SectorialDivision():
    def __init__(self, playgroundsize = (350, 450)):
        '''
        Initialisation von SectorialDivision
        erstellt Sektorobjekte mit einer Position, breite, hoehe und fuegt diese
        zur Liste self.sectors
        Parameter:      playgroundsize
                            int, width der Map
                            int, height der Map
        return values:  -
        '''
        self.sectors = []
        self.sectorWidth = 100  #nur eine Beispielgroesse
        self.sectorHeight = 100 #nur eine Beispielgroesse
        self.sectorsize = self.sectorWidth, self.sectorHeight
        self.__setSectors(playgroundsize)
             
        
    def __setSectors(self, playgroundsize):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        ruft Funktionen auf, die, die Menge der benoetigten Sectoren, sowie ihre Position und hoehe bestimmen
        und fuegt sie der Liste self.sectors Hinzu
        Parameter:      playgroundsize
                            int, width der Map
                            int, height der Map
        return values:  -
        '''
        amount = self.__getSectorAmount(playgroundsize)
        self.__setSectorsize(playgroundsize, amount)
        positions = self.__setSectorPositions(amount)
        self.__addSectors(positions)
        
    def __getSectorAmount(self, playgroundsize, memory = 1):
        '''
        Private Funktion - nicht ausserhalb der bestimmt die breite und hoehe eines Sektors
        Parameter:      playgroundsize
                            int, width der Map
                            int, height der Mapfloat amountgedacht.
        return values:  int, anzahl der benoetigten Sektoren, damit das Spielfeld ausgefuellt wird
        '''
        if playgroundsize > self.sectorsize:
            newPlaygroundsize = playgroundsize[0] / 2, playgroundsize[1] / 2
            memory = self.__getSectorAmount(newPlaygroundsize, memory * 4)
        return memory
            
    def __setSectorsize(self, playgroundsize, amount):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        bestimmt die breite und hoehe eines Sektors ueber self.width und self.height
        Parameter:      playgroundsize
                            int, width der Map
                            int, height der Map
                        float amount (float fuer den Fall, dass amount == 1 ist, sonst reicht int),
                        zur groessenbestimmung der Sektoren
        return values:  -
        '''
        height = playgroundsize[0] / float(amount / 2)
        width = playgroundsize[1] / float(amount / 2)
        self.sectorHeight = height
        self.sectorWidth = width
        self.sectorsize = self.sectorHeight, self.sectorWidth
    
    def __setSectorPositions(self, amount):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        Bestimmt die positionen der Sektoren
        Parameter:      int amount, zur Positionbestimmung
        return values:  Liste mit positions, Tuple (int, int), um spaeter Sektorobjekte zu
                        erstellen und denen eine Position zuweisen zu koennen
        '''
        positions = []
        for i in range(int(math.sqrt(amount))):
            for j in range(int(math.sqrt(amount))):
                xPosition = j * self.sectorHeight
                yPosition = i * self.sectorWidth
                positions.append((xPosition, yPosition))
        return positions
                
    def __addSectors(self, positions):
        '''
        Private Funktion - nicht ausserhalb der Klasse benutzen!
        erstellt Sektorobjekte mit rect
        Parameter:      int amount, zur Positionbestimmung
        return values:  Liste mit positions, Tuple (int, int), um spaeter Sektorobjekte zu
                        erstellen und denen eine Position zuweisen zu koennen
        '''
        for i in range(len(positions)):
            sector = Sector((positions[i][0], positions[i][1], self.sectorWidth, self.sectorHeight))
            self.sectors.append(sector)

            
