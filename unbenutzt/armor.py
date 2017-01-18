# -*- coding: cp1252 -*-
#Datum :    18.12.16
#Autor/en:  Lucas V.
#Version:   1.0


class Armor():
    def __init__(self, position = (0, 0), durability = 5, resistance = 1):
        '''
        Initialisation der Ruestung
        wird wahrscheinlich noch ueberarbeitet
        Parameter:      position
                            int, x-Koordinate
                            int, y-Koordinate
        return values:  -
        '''
        self.position = position
        self.durability = durability
        self.resistance = resistance
        
    def use(self):
        '''
        verringert die haltbarkeit der Ruestung um 1
        Parameter:      -
        return values:  -
        '''
        self.durability -= 1
        
    def getDurability(self):
        '''
        Ausgabe der Haltbarkeit der Ruestung
        Parameter:      -
        return values:  int, Haltbarkeit der Ruestung
        '''
        return self.durability
    
    def setDurability(self, newDurablity):
        '''
        setzen der Haltbarkeit der Ruestung
        Parameter:      int, neue Haltbarkeit der Ruestung
        return values:  -
        '''
        self.durability = newDurability
        
    def getResistance(self):
        '''
        Ausgabe der resistenz der Ruestung
        Parameter:      -
        return values:  Float, resistenz der Ruestung
        '''
        return self.resistance
    
    def setResistance(self, newResistance):
        '''
        setzen die Resistenz der Ruestung
        Parameter:      float, neue Resistenz der Ruestung
        return values:  -
        '''
        self.resistance = newResistance
        
    def getPosition(self):
        '''
        Ausgabe der Ruestungsposition (nur beim spawn)
        Parameter:      -
        return values:  Tuple (int, int), position der Ruestung
        '''
        return self.position
    
    def setPosition(self, newXPos, newYPos):
        '''
        setzt die Position der Ruestung (nur beim spawn)
        Parameter:      Tuple (int, int), position der Ruestung
        return values:  -
        '''
        self.position = newXPos, newYPos
