# -*- coding: cp1252 -*-

import pygame
import bisect

def createByImage(path = "map.png"):
    m       = GameMap()
    try:
        mapdata = pygame.image.load(path)
    except:
        return m
    size    = mapdata.get_size()
    black   = mapdata.map_rgb((0, 0, 0))
    mapdata = pygame.PixelArray(mapdata)
    m.setWidth(size[0])
    m.setHeight(size[1])
    for x in xrange(size[0]):
        for y in xrange(size[1]):
            if mapdata[x][y] == black:
                m._invalidPositions.add((x, y))
    return m

class GameMap:

    """
    Klasse für eine GameMap mit validen und nicht-validen Positionen
    """

    def __init__(self):
        """
        Initialisation einer Map
        Parameter:      -
        Rückgabewerte:  -
        """
        self._width     = 0
        self._height    = 0
        self._invalidPositions = set()
    
    def getWidth(self):
        """
        Zurückgeben der Breite der GameMap
        Parameter:      -
        Rückgabewerte:  int Breite der GameMap
        """
        return self._width

    def getHeight(self):
        """
        Zurückgeben der Höhe der GameMap
        Parameter:      -
        Rückgabewerte:  int Höhe der GameMap
        """
        return self._height

    def setWidth(self, width):
        """
        Setzen der Breite der GameMap, falls sie nicht gesetzt wurde
        Parameter:      int Breite der GameMap
        Rückgabewerte:  -
        """
        if not self._width:
            self._width = int(width)

    def setHeight(self, height):
        """
        Setzen der Höhe der GameMap, falls sie nicht gesetzt wurde
        Parameter:      int Höhe der GameMap
        Rückgabewerte:  -
        """
        if not self._height:
            self._height = int(height)

    def isPositionValid(self, x, y):
        """
        Zurückgeben ob die GameMap an der angegebenen Position begehbar ist bzw. ob die Position valide ist
        Parameter:      int x-Koordinate der zu überprüfenden Position
                        int y-Koordinate der zu überprüfenden Position
        Rückgabewerte:  bool ob die GameMap an der angegebenen Position begehbar ist
        """
        return not (x, y) in self._invalidPositions
    
    def isRectValid(self, rect):
        """
        Zurückgeben ob ein Bereich der GameMap begehbar ist bzw. ob der Bereich vollkommen valide ist
        Parameter:      pygame.Rect der zu überprüfende Bereich
        Rückgabewerte:  bool ob Bereich der GameMap begehbar ist
        """
        for x in xrange(rect.width):
            for y in xrange(rect.height):
                if not self.isPositionValid(x + rect.x, y + rect.y):
                    return False
        return True

if __name__ == "__main__":
    import pygame, pygame.gfxdraw
    from pygame.locals import *
    import sys, random, time

    pygame.init()

    m       = createByImage()
    screen  = pygame.display.set_mode((m.getWidth(), m.getHeight()), 0, 32)
    black   = pygame.Surface((m.getWidth(), m.getHeight()), 0, 32)
    black.fill((0, 0, 0))

    print len(m._invalidPositions), m.getWidth() * m.getHeight()
    
    for x in xrange(m.getWidth()):
        for y in xrange(m.getHeight()):
            color = (250, 150, 100)
            if m.isPositionValid(x, y):
                pygame.gfxdraw.pixel(screen, x, y, color)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
