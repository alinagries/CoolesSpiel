import math


class Bullet():
    def __init__(self, position = (0, 0), direction = (0, 0), speed = 0, damage = 2):
        self.position = position
        self.direction = direction
        self.speed = speed
        self.dmg = damage
        self.__pixelLength = 10
 
    def move(self):
        '''
        Ziel: alle 10p soll der Schuss berechnet werden
        Position = (x, y)
        direction = (n, m)
        |direction| = direction in Pixel
        r * |direction| = pixelLength --> r = pixelLength / |direction| --> r * |direction| kann alle 10 pixel berechnet werden
        DANACH kann man weiterrechnen
        r * (direction) = neue Position
        neueXPos += r * direction[0]
        neueYPos += r * direction[1]
        Kugel wird verschoben, wenn Spieler oder Wand getroffen wird, wird die Kugel entfernt
        '''
        x = self.position[0]
        y = self.position[1]
        directionX = self.direction[0]
        directionY = self.direction[1]
        r = self.__pixelLength / math.sqrt( math.pow(directionX, 2) + math.pow(directionY, 2))
        
        newXPosition = x + r * directionX
        newYPosition = y + r * directionY
        
        self.position[0] = newXPosition
        self.position[1] = newYPosition
        
    def getPosition(self):
        return self.position
    
    def setPosition(self, x, y):
        self.position = x, y
        
    def getDirection(self):
        return self.direction
    
#    def setDirection(self, x, y):
#        self.direction = x, y
        
    def getSpeed(self):
        return self.speed
    
#    def setSpeed(self, speed):
#        self.speed = speed
        
    def getDamge(self):
        return self.dmg
    
#    def setDamge(self, dmg):
#        self.dmg = dmg
