# -*- coding: cp1252 -*-

import positionmap

def createByImage(path = "map.png"):
    """
    Erstellen einer GameMap durch eine Bilddatei
    Pixel mit den RGB-Werten 0 (schwarz) werden als invalide Positionen interpretiert

    Parameter:      string Pfadangabe zu der Bilddatei
    Rückgabewerte:  GameMap das Ergebnis
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
    Erstellen einer GameMap durch eine Bildfläche
    Pixel mit dem RGB-Wert 0 (schwarz) werden als invalide Positionen interpretiert

    Parameter:      pygame.Surface die Bildfläche im beschriebenen Format
    Rückgabewerte:  GameMap das Ergebnis
    """
    return positionmap.createBySurface(surface)

def createByList(l = []):
    """
    Erstellen einer GameMap durch eine Liste mit Strings
    die Breite der Listeneinträge und die Länge der Liste entsprechen der Breite und Höhe der GameMap
    Alle Zeichen außer Leerzeichen werden als invalid interpretiert
    
    Parameter:      list Liste mit Strings im beschriebenen Format
    Rückgabewerte:  GameMap das Ergebnis
    """
    return positionmap.createByList(l)

def scale(m, scale = 1):
    """
    Skalieren einer GameMap durch ein Skalar
    
    Parameter:      GameMap die zu skalierende GameMap
                    int das Skalar oder tuple jeweils ein Wert für beide Dimensionen
    Rückgabewerte:  GameMap das Ergebnis
    """
    return positionmap.scale(m, scale)

class GameMap(positionmap.PositionMap):

    """
    Klasse für eine GameMap mit validen und nicht-validen Positionen, sowie besonderen Positionen
    """

    def __init__(self):
        """
        Initialisation einer GameMap

        Parameter:      -
        Rückgabewerte:  -
        """
        positionmap.PositionMap.__init__(self)
