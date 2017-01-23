#Autor/en:  Niclas, Gregor
#Datum:     ????
#Version:   1.0

import pygame
import math

BLACK = (0, 0, 0)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, xPosition, yPosition, eventPosition, speed = 1, damage = 2, playernick = 'someone', allowedPosition = True):
        """
        Initialisierung der Klasse Bullet
        Parameter:      int xPosition, die xPosition der Bullet
                        int yPosition, die yPosition der Bullet
                        Tuple (int, int), dei Zielposition der Bullet
                        float speed, die geschwindigkeit der Bullet (leider auch praezision)
                            wenn speed < 0.2 gibt es Bugs
                        float damage, der Schaden der Bullet
        return value:   -
        """
        super(Bullet, self).__init__()# Call the parent class (Sprite) constructor
        
        self.vector=(0,0)
        self.image = pygame.image.load("ball2.png")#pygame.Surface([4, 10])
        self.playernick = playernick
        #self.allowedPosition = True
        self.rect = self.image.get_rect()
        self.rect.x = xPosition
        self.rect.y = yPosition
        self.__realXPosition = xPosition
        self.__realYPosition = yPosition
        self.updateVector((eventPosition[0] - xPosition, eventPosition[1] - yPosition))
        self.adjustedVector = (0, 0)
        self.speed = 5 * speed
        self.damage = damage
        self.allowedPosition = allowedPosition


    def updateVector(self, vec):
        '''
        updatet den Vektor
        Parameter:      -
        return values:  -
        '''
        self.vector = vec

    def lenVector(self):
        '''
        errechnet die laenge des Vektors mit hypot
        Parameter:      -
        return values:  -
        '''
        #print 'len', math.hypot(self.vector[0], self.vector[1])
        return math.hypot(self.vector[0], self.vector[1])

        
    def adjustVector(self):
        '''
        Gleicht den Vektor an, sodass die Kugel nicht schneller wird, wenn sie weiter vom Spieler entfernt ist.
        Paramter : -
        Rueckgabewerte: (x,y) (angepasster Vektor)
        '''
        length = self.lenVector()
        try:
            x = (self.vector[0] / length) #5 Geschwindigkeit des Schusses
            y = (self.vector[1] / length)
            self.adjustedVector = ((self.speed * x ), ((self.speed * y)))
            
        except:
            #print 'except'
            self.adjustedVector = self.vector
        #print self.adjustedVector

    def update(self, gamemap, margin):
        '''
        Bewegt die Kugel, benutzt dabei den Vektor, der mit adjustVektor angepasst wurde.
        Falls die Bullet gegen eine Wand fliegt wird diese removt
        Paramter : -
        Rueckgabewerte: -
        '''
        if self.adjustedVector == (0, 0):
            self.adjustVector()
        self.__realXPosition += self.adjustedVector[0]
        self.__realYPosition += self.adjustedVector[1]
        self.rect.x = int(self.__realXPosition)
        self.rect.y = int(self.__realYPosition)

        if self.rect.x > gamemap.getWidth() + margin or self.rect.y > gamemap.getHeight() + margin:
            self.allowedPosition = False
        elif self.rect.x < 0 - margin or self.rect.y < 0 - margin:
            self.allowedPosition = False
        

##################### Getters und Setters, die momentan nirgends gebraucht werden, aber dazu gehoeren #####################

    def getDamage(self):
        '''
        gibt dem den Schaden der Bullet aus
        Parameter:      -
        return values:  Float damage der Bullet
        '''
        return self.dmg
    
    def setDamage(self, dmg):
        '''
        setzt den Schaden des Objektes Bullet
        Parameter:      Float damage
        return values:  -
        '''
        self.dmg = dmg

    def getDirection(self):
        '''
        gibt dem die Richtung der Bullet aus
        Parameter:      -
        return values:  Tuple (Int, Int), Richtung in x und y
        '''
        return self.direction
    

