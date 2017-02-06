# -*- coding: cp1252 -*-

import pygame

def createByImage(path = "map.png"):
    """
    Erstellen einer PositionMap durch eine Bilddatei
    Pixel mit den RGB-Werten 0 (schwarz) werden als invalide Positionen interpretiert

    Parameter:      string Pfadangabe zu der Bilddatei
    Rückgabewerte:  PositionMap das Ergebnis
    """
    try:
        mapdata = pygame.image.load(path)
    except:
        m = PositionMap()
        m.setWidth(1)
        m.setHeight(1)
        return m
    return createBySurface(mapdata)

def createBySurface(surface):
    """
    Erstellen einer PositionMap durch eine Bildfläche
    Pixel mit dem RGB-Wert 0 (schwarz) werden als invalide Positionen interpretiert

    Parameter:      pygame.Surface die Bildfläche im beschriebenen Format
    Rückgabewerte:  PositionMap das Ergebnis
    """
    m       = PositionMap()
    size    = surface.get_size()
    black   = surface.map_rgb((0, 0, 0))
    surface = pygame.PixelArray(surface)
    m.setWidth(size[0])
    m.setHeight(size[1])
    for x in xrange(size[0]):
        for y in xrange(size[1]):
            try:
                if surface[x][y] == black:
                    m._invalidPositions.add((x, y))
            except:
                pass
    return m

def createByList(l = []):
    """
    Erstellen einer PositionMap durch eine Liste mit Strings
    die Breite der Listeneinträge und die Länge der Liste entsprechen der Breite und Höhe der PositionMap
    Alle Zeichen außer Leerzeichen werden als invalid interpretiert
    
    Parameter:      list Liste mit Strings im beschriebenen Format
    Rückgabewerte:  PositionMap das Ergebnis
    """
    m       = PositionMap()
    invalid = []
    w       = 0
    if not l:
        m.setWidth(1)
        m.setHeight(1)
        return m
    for y in xrange(len(l)):
        ln = str(l[y])
        for x in xrange(len(ln)):
            if ln[x] != " ":
                invalid.append((x, y))
        if len(ln) > w:
            w = len(ln)
    m.setWidth(w)
    m.setHeight(len(l))
    for pos in invalid:
        m._invalidPositions.add(pos)
    return m

def scale(m, scale = 1):
    """
    Skalieren einer PositionMap durch ein Skalar
    
    Parameter:      PositionMap die zu skalierende PositionMap
                    int das Skalar oder tuple jeweils ein Wert für beide Dimensionen
    Rückgabewerte:  PositionMap das Ergebnis
    """
    if isinstance(scale, tuple):
        scaleX = abs(scale[0])
        scaleY = abs(scale[1])
    else:
        scaleX = abs(scale)
        scaleY = abs(scale)
    resolution = (int(m.getWidth() * scaleX), int(m.getHeight() * scaleY))
    return createBySurface(pygame.transform.scale(m.toSurface(), resolution))


class PositionMap:

    """
    Klasse für eine PositionMap mit validen und nicht-validen Positionen
    """

    def __init__(self):
        """
        Initialisation einer PositionMap

        Parameter:      -
        Rückgabewerte:  -
        """
        self._width     = 0
        self._height    = 0
        self._invalidPositions = set()
    
    def getWidth(self):
        """
        Zurückgeben der Breite der PositionMap

        Parameter:      -
        Rückgabewerte:  int Breite der PositionMap
        """
        return self._width

    def getHeight(self):
        """
        Zurückgeben der Höhe der PositionMap

        Parameter:      -
        Rückgabewerte:  int Höhe der PositionMap
        """
        return self._height

    def getLengthInvalidPositions(self):
        """
        Zurückgeben der Anzahl an invaliden Positionen der PositionMap

        Parameter:      -
        Rückgabewerte:  int Anzahl an invaliden Positionen der PositionMap
        """
        return len(self._invalidPositions)

    def setWidth(self, width):
        """
        Setzen der Breite der PositionMap, falls sie nicht gesetzt wurde

        Parameter:      int Breite der PositionMap
        Rückgabewerte:  -
        """
        if not self._width:
            self._width = int(width)

    def setHeight(self, height):
        """
        Setzen der Höhe der PositionMap, falls sie nicht gesetzt wurde

        Parameter:      int Höhe der PositionMap
        Rückgabewerte:  -
        """
        if not self._height:
            self._height = int(height)

    def isPositionValid(self, x, y):
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
        return not (x, y) in self._invalidPositions
    
    def isRectValid(self, rect):
        """
        Zurückgeben ob ein Bereich der PositionMap begehbar ist bzw. ob der Bereich vollkommen valide ist

        Parameter:      pygame.Rect der zu überprüfende Bereich
        Rückgabewerte:  bool ob Bereich der PositionMap begehbar ist
        """
        for x in xrange(rect.width):
            for y in xrange(rect.height):
                if not self.isPositionValid(x + rect.x, y + rect.y):
                    return False
        return True

    def toSurface(self):
        """
        Zurückgeben einer Bildfläche, die die PositionMap repräsentiert
        invalide Positionen werden als Pixel mit den RGB-Werten 0 (schwarz) dargestellt
        valide Positionen wrden als Pixel mit den RGB-Werten 255 (weiß) dargestellt

        Parameter:      -
        Rückgabewerte:  pygame.Surface das Ergebnis
        """
        surface = pygame.Surface((self.getWidth(), self.getHeight()), 0, 32)
        surface.fill((255, 255, 255))
        black   = surface.map_rgb((0, 0, 0))
        mapdata = pygame.PixelArray(surface)
        for pos in self._invalidPositions:
            try:
                mapdata[pos[0]][pos[1]] = black
            except:
                pass
        return surface
