# -*- coding: cp1252 -*-
#Datum :    17.12.16
#Autor/en:  Lucas V.
#Version:   1.0

from entity import Entity
import time

class Trap(Entity):
    def __init__(self, rect = (0, 0, 3, 3), damage = 4, radius = 3, activationTime = 2):
        '''
        Initialisation von Trap
        Parameter:      rect
                            int mit der distanz nach links
                            int mit der disanz nach oben
                            int width von dem Objekt
                            int heigth von dem Objekt
                        float, damage der Trap
                        int, Radius der Trap (am besten eine gerade Zahl, muss aber nicht zwangslaeufig sein)
                        float, zeit in Sekunden, bis die Trap aktiviert wird
        return values:  -
        '''
        Entity.__init__(self, rect, 0)
        self.dmg = damage
        self.radius = radius
        self.activationTime = activationTime
        self.activationMoment = 0
        self.triggerMoment = 0
        self.triggerPositions = []
        self.explotionPositions = []
        
    def place(self, position):
        '''
        plaziert ein Damagegadget im game auf der Map und aktiviert diese
        Parameter:      Tuple (int, int), position
        return values:  -
        '''
        self.setPosition(position[0], position[1])
        self.activation()
        self.__calculateTriggerPositions()
        self.__calculateExplotionPositions()
    
    def trigger(self):
        '''
        zeitpunkt zu dem die Falle ausgeloest wird
        Parameter:      -
        return values:  -
        '''
        self.triggerMoment = time.clock()
        
    def exploded(self):
        '''
        ueberprueft ob die Falle explodiert ist, ob die explosionszeit um ist
        Parameter:      -
        return values:  Boolean, ob die Falle ausgloest werden kann
        '''
        if not self.triggerMoment == 0 and time.clock() - self.triggerMoment >= float(self.activationTime) / 2:
            return True    
    
    def __calculateTriggerPositions(self):
        '''
        errechnet eine List von Postionen, in denen die Trap ausgeloest wird
        Parameter:      -
        return values:  eine List von Tupeln (int, int)
        '''
        position = self.getPosition()
        size = self.getSize()
        length = size[0] + self.radius
        height = size[1] + self.radius
        startPosition = position[0] - self.radius / 2, position[1] - self.radius / 2
        
        triggerPositions = []
        for y in range(length):
            yCoord = startPosition[1] + y
            for x in range(height):
                xCoord = startPosition[0] + x
                triggerPositions.append((xCoord, yCoord))
            
        self.triggerPositions = triggerPositions
    
    def getTriggerPositions(self):
        '''
        uebergibt eine List von Postionen, in denen die Trap ausgeloest wird
        Parameter:      -
        return values:  eine List von Tupeln
        '''
        return self.triggerPositions
        
    def __calculateExplotionPositions(self):
        '''
        errechnet eine List von Postionen, in denen die Trap Schaden macht
        Parameter:      -
        return values:  eine List von Tupeln (int, int)
        '''
        position = self.getPosition()
        size = self.getSize()
        length = size[0] + 2 * self.radius
        height = size[1] + 2 * self.radius
        startPosition = position[0] - self.radius, position[1] - self.radius
        
        explotionPositions = []
        for y in range(length):
            yCoord = startPosition[1] + y
            for x in range(height):
                xCoord = startPosition[0] + x
                explotionPositions.append((xCoord, yCoord))
        self.explotionPositions = explotionPositions        
    
    def getExplotionPositions(self):
        '''
        uebergibt eine List von Postionen, in denen die Trap Schaden macht
        Parameter:      -
        return values:  eine List von Tupeln
        '''
        return self.explotionPositions
        
    def activation(self):
        '''
        activiert die Falle, kann ausgeloest werden, sobald die aktivierungszeit um ist
        Parameter:      -
        return values:  -
        '''
        self.activationMoment = time.clock()
        
    def activated(self):
        '''
        ueberprueft ob die Falle ausgeloest werden kann, ob die aktivierungszeit um ist
        Parameter:      -
        return values:  Boolean, ob die Falle ausgloest werden kann
        '''
        if not self.activationMoment == 0 and time.clock() - self.activationMoment >= self.activationTime:
            return True
        
    def getActivationTime(self):
        '''
        gibt die Aktivierungszeit des Gadgets in Sekunden aus
        Parameter:      -
        return values:  Float, Aktivierungszeit des Gadgets in Sekunden
        '''
        return self.activationTime
    
    def setActivationTime(self, activationTime):
        '''
        setzt die Aktivierungszeit des Gadgets
        Parameter:      Float, Aktivierungszeit des Gadgets
        return values:  -
        '''
        self.activationTime = activationTime
        
    def getRadius(self):
        '''
        gibt den Radius des Gadgets aus
        Parameter:      -
        return values:  Int, Radius des Gadgets
        '''
        return self.radius
    
    def setRadius(self, radius):
        '''
        setzt den Radius des Gadgets
        Parameter:      Int, radius des Gadgets
        return values:  -
        '''
        self.radius = radius
        
    def getDamage(self):
        '''
        gibt den Schaden des Gadgets aus
        Parameter:      -
        return values:  Float, Schaden des Gadgets
        '''
        return self.dmg
    
    def setDamage(self, dmg):
        '''
        setzt den Schaden des Gadgets
        Parameter:      Float, Schaden des Gadgets
        return values:  -
        '''
        self.dmg = dmg
