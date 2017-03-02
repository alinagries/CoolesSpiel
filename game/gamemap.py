
# -*- coding: cp1252 -*-

import positionmap
import pygame

def createByImage(path = "map3col.png"):
    """
    Erstellen einer GameMap durch eine Bilddatei
    Pixel mit den RGB-Werten 0 (schwarz) werden als invalide Positionen interpretiert

    Parameter:      string Pfadangabe zu der Bilddatei
    RÃ¼ckgabewerte:  GameMap das Ergebnis
    """
    try:
        mapdata = pygame.image.load(path)
    except:
        m = GameMap()
        m.setWidth(1)
        m.setHeight(1)
        return m
    return createBySurface(mapdata)

def createBySurface(surface):
    """
    Erstellen einer GameMap durch eine BildflÃ¤che
    Pixel mit dem RGB-Wert 0 (schwarz) werden als invalide Positionen interpretiert

    Parameter:      pygame.Surface die Bildflaeche im beschriebenen Format
    RÃ¼ckgabewerte:  GameMap das Ergebnis
    """
    m = GameMap()
    p = positionmap.createBySurface(surface)
    m._invalidPositions = p._invalidPositions
    m.setWidth(p.getWidth())
    m.setHeight(p.getHeight())

    door    = set()
    size    = surface.get_size()
    red     = surface.map_rgb((255, 0, 0))
    surface = pygame.PixelArray(surface)
    m.setWidth(size[0])
    m.setHeight(size[1])
    for x in xrange(size[0]):
        for y in xrange(size[1]):
            try:
                if surface[x][y] == red:
                    door.add((x, y))
            except:
                pass
    m._doorPositions = frozenset(door)
    return m

def createByList(l = []):
    """
    Erstellen einer GameMap durch eine Liste mit Strings
    die Breite der ListeneintrÃ¤ge und die LÃ¤nge der Liste entsprechen der Breite und HÃ¶he der GameMap
    Alle Zeichen auÃŸer Leerzeichen werden als invalid interpretiert
    
    Parameter:      list Liste mit Strings im beschriebenen Format
    RÃ¼ckgabewerte:  GameMap das Ergebnis
    """
    return positionmap.createByList(l)

def scale(m, scale = 1):
    """
    Skalieren einer GameMap durch ein Skalar
    
    Parameter:      GameMap die zu skalierende GameMap
                    int das Skalar oder tuple jeweils ein Wert fÃ¼r beide Dimensionen
    RÃ¼ckgabewerte:  GameMap das Ergebnis
    """
    return positionmap.scale(m, scale)

class GameMap(positionmap.PositionMap):

    """
    Klasse fÃ¼r eine GameMap mit validen und nicht-validen Positionen, sowie besonderen Positionen
    """

    def __init__(self):
        """
        Initialisation einer GameMap

        Parameter:      -
        Ru eckgabewerte:  -
        """
        positionmap.PositionMap.__init__(self)

        self._doorPositions = frozenset()

    def isDoorValid(self, x, y):
        """
        Zurückgeben ob die PositionMap an der angegebenen Position begehbar ist bzw. ob die Position valide ist

        Parameter:      int x-Koordinate der zu überprüfenden Position
                        int y-Koordinate der zu überprüfenden Position
        Rückgabewerte:  bool ob die PositionMap an der angegebenen Position begehbar ist
        """
        if x >= self._width:
            return False
        if y >= self._height:
            return False
        if x < 0:
            return False
        if y < 0:
            return False
        if (x, y) in self._doorPositions:
            print "jo"
            return True

    def isDoorRectValid(self, rect):
        """
        Zurückgeben ob ein Bereich der PositionMap begehbar ist bzw. ob der Bereich vollkommen valide ist

        Parameter:      pygame.Rect der zu überprüfende Bereich
        Rückgabewerte:  bool ob Bereich der PositionMap begehbar ist
        """
        for x in xrange(rect.width):
            for y in xrange(rect.height):
                if self.isDoorValid(x + rect.x, y + rect.y):
                    print "auch"
                    return True
        return False
