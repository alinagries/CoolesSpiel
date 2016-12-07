# -\*- coding: cp1252 -\*-

from pygame.sprite import *
from pygame.rect import Rect

class Widget(Sprite):
    """
    Basisklasse für statische Elemente
    """
    def __init__(self):
        Sprite.__init__(self)
        self.__posX = 0
        self.__posY = 0
        self.__height = 64
        self.__width = 64
        self.rect = Rect(self.__posX, self.__posY, self.__width, self.__height)

    def getX(self):
        """
        Holt die x-Position des Widget-Objekts

        parameters: -

        return values: int x-Position
        """
        return self.__posX

    def setX(self, x):
        """
        Setzt die x-Position des Widget-Objekts

        parameters: int x-Position

        return values: -
        """
        self.__posX = x

    def getY(self):
        """
        Holt die y-Position des Widget-Objekts

        parameters: -

        return values: int y-Position
        """
        return self.__posY

    def setY(self, y):
        """
        Setzt die y-Position des Widget-Objekts

        parameters: int y-Position

        return values: -
        """
        self.__posY = y

    def getWidth(self):
        """
        Holt die Breite des Widget-Objekts

        parameters: -

        return values: int y-Position
        """
        return self.__width

    def setWidth(self, w):
        """
        Setzt die Breite des Widget-Objekts

        parameters: int Breite

        return values: -
        """
        self.__width = w

    def getHeight(self):
        """
        Holt die Höhe des Widget-Objekts

        parameters: -

        return values: int Höhe
        """
        return self.__posY

    def setHeight(self, h):
        """
        Setzt die Höhe des Widget-Objekts

        parameters: int Höhe

        return values: -
        """
        self.__height = h
