#Autor/en:  Lucas V., Niclas, Gregor
#Version:   2.4

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
                        float speed, die geschwindigkeit der Bullet
                        float damage, der Schaden der Bullet
        return value:   -
        """
        super(Bullet, self).__init__()# Call the parent class (Sprite) constructor
        

        self.direction = (0,0)
        self.updateDirection((eventPosition[0] - xPosition, eventPosition[1] - yPosition))

        self.image = pygame.Surface([2, 4])
        self.playernick = playernick
        self.allowedPosition = True
        
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
        self.allowedPosition = allowedPosition


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
            #print 'except'
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
            
        self.__realXPosition += self.adjustedDirection[0]
        self.__realYPosition += self.adjustedDirection[1]
        self.rect.x = int(self.__realXPosition)
        self.rect.y = int(self.__realYPosition)
        
    
        

##################### Getters und Setters, die momentan nirgends gebraucht werden, aber dazu gehoeren #####################

    def getDamage(self):
        '''
        gibt dem den Schaden der Bullet aus
        Parameter:      -
        return values:  Float, damage der Bullet
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
    

