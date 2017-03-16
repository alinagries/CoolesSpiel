#Autor/en:  Lucas V., Niclas, Gregor
#Version:   2.4

import pygame
import math

BLACK = (0, 0, 0)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, xPosition, yPosition, eventPosition, speed = 1, damage = 2, playernick = "whoCares"):
        """
        Initialisierung der Klasse Bullet
        Parameter:      int xPosition, die xPosition der Bullet
                        int yPosition, die yPosition der Bullet
                        Tuple (int, int), dei Zielposition der Bullet
                        float speed, die geschwindigkeit der Bullet
                        float damage, der Schaden der Bullet
        return value:   -
        """
        super(Bullet, self).__init__()# Call the parent class (Sprite) constructor
        self.playernick = playernick

        self.direction = (0,0)
        self.updateDirection((eventPosition[0] - xPosition, eventPosition[1] - yPosition))

        self.image = pygame.Surface([2, 4])
       
        rotation = math.acos(self.direction[1]/(math.sqrt(1)*math.sqrt(self.direction[0]**2+self.direction[1]**2)))
        self.image = pygame.transform.rotate(self.image, math.degrees(rotation))
        
        self.rect = self.image.get_rect()
        self.rect.x = xPosition
        self.rect.y = yPosition
        self.__realXPosition = xPosition
        self.__realYPosition = yPosition
        self.adjustedDirection = (0, 0)
        self.speed = 5 * speed
        self.damage = damage
        self.bulletFligthPositions = []

    def updateDirection(self, direction):
        '''
        updatet die Flugrichtung der Bullet
        Parameter:      -
        return values:  -
        '''
        self.direction = direction

    def lenDirection(self):
        '''
        errechnet die laenge des Vektors mit hypot
        Parameter:      -
        return values:  -
        '''
        return math.hypot(self.direction[0], self.direction[1])

        
    def adjustDirection(self):
        '''
        Gleicht den Vektor an, sodass die Kugel nicht schneller wird, wenn das Event weiter vom Spieler entfernt ist.
        Paramter : -
        Rueckgabewerte: (x,y) (angepasster Vektor)
        '''
        length = self.lenDirection()
        try:
            x = (self.direction[0] / length) #5 Geschwindigkeit des Schusses
            y = (self.direction[1] / length)
            self.adjustedDirection = ((self.speed * x ), ((self.speed * y)))
            
        except:
            print 'ein except in adjustDirection, bullet.py, duerfte eigentlich nie auftreten!'
            self.adjustedDirection = self.direction
        #print self.adjustedDirection

    def update(self):
        '''
        Bewegt die Kugel, benutzt dabei den Vektor, der mit adjustVektor angepasst wurde.
        Falls die Bullet gegen eine Wand fliegt wird diese removt
        Paramter :      -
        Rueckgabewerte: -
        '''
        
        if self.adjustedDirection == (0, 0):
            self.adjustDirection()
        self.getBulletFlightPositions()          
        self.__realXPosition += self.adjustedDirection[0]
        self.__realYPosition += self.adjustedDirection[1]
        self.rect.x = int(self.__realXPosition)
        self.rect.y = int(self.__realYPosition)
        
    def getBulletFlightPositions(self, precision = 5): #kerim
        '''
        stelt sicher, dass kein Tunneleffekt auftritt
        Parameter:      int, precision, alle soviele pixel werden die Punkte der Linien berechnet
        return values:  -
        '''
        lineList = []   
        xDirection = self.adjustedDirection[0] / self.speed
        yDirection = self.adjustedDirection[1] / self.speed
        
        #   1 - - 2   1 - 4 sind die Eckpunkte der Rect der Bullet, 5 ist der Mittelpunkt
        #   |  5  |   von denen gehen Parallele Linien in richtung Direction ab
        #   3 - - 4   (positionen der Punkte, die eine Linie bilden)
        #             3 und 4 Linien sind die genauste Darstellung,
        #     ab 2 Diagonalen wird es leicht ungenauer, aber mit  1/3 oder 2/4 quasi dieselbe genauigkeit und es wird eine Fallunterscheidung benoetigt
        #     im notfall auch mit nur eine Diagonalen, die muss dann aber von Punkt 5 ausgehen
        # Eine Liste mit den Positionen wird erstellt, die zur abpruefung dienen ob irgendetwas getroffen wird, damit es keinen Tunneleffeckt gibt
        # precision darf maximal so gross sein wie das kleinste Objekt, mit dem es Kollidieren kann. Und je groesser precision destso ungenauer der
        #schuss, wenn er an einer Wandecke vorbei fliegt

        #Die bullet fliegt nach rechts oben oder Links unten (nach rechts wird x immer hoeher, nach unten wird y immer hoeher)
        if xDirection > 0 and yDirection < 0 or xDirection < 0  and yDirection > 0:
            for i in range(0, self.speed, precision):
                lineList.append( (int( (i+1) * xDirection + self.rect[0] ), int((i+1) * yDirection + self.rect[1]) ) )                              #1.Eckpunkt
                lineList.append( (int( (i+1) * xDirection + self.rect[0] + self.rect[2]), int((i+1) * yDirection + self.rect[1] + self.rect[3]) ) ) #4.Eckpunkt
        else: # bullet fliegt Richtung rechts unten oder links oben
            for i in range(0, self.speed, precision):        
                lineList.append( (int( (i+1) * xDirection + self.rect[0] ), int((i+1) * yDirection + self.rect[1] + self.rect[3]) ) )               #2.Eckpunkt
                lineList.append( (int( (i+1) * xDirection + self.rect[0] + self.rect[2] ), int((i+1) * yDirection + self.rect[1]) ) )               #3.Eckpunkt

        #falls die rechnung viel zu lange dauern sollte:
        #for i in range(0, self.speed, precision):
        #    lineList.append( (int( (i+1) * xDirection + self.rect[0] + self.rect[2]/2), int((i+1) * yDirection + self.rect[1] + self.rect[3]/2) ) ) #5. Mittelpunkt
            
        self.bulletFligthPositions = lineList
        
        

##################### Getters und Setters, die momentan nirgends gebraucht werden, aber dazu gehoeren #####################

    def getDamage(self):
        '''
        gibt dem den Schaden der Bullet aus
        Parameter:      -
        return values:  Float, damage der Bullet
        '''
        return self.damage
    
    def setDamage(self, damage):
        '''
        setzt den Schaden des Objektes Bullet
        Parameter:      Float damage
        return values:  -
        '''
        self.damage = damage

    def getDirection(self):
        '''
        gibt dem die Richtung der Bullet aus
        Parameter:      -
        return values:  Tuple (Int, Int), Richtung in x und y
        '''
        return self.direction
    
