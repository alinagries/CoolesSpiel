# -*- coding: utf-8 -*-
#Datum :    22/23.12.16
#Autor/en: Kai K.
#Version:   1.0

import gamemap
import cPickle as Pickle
import pygame.image
import os.path

class Room:

    """
    Klasse die einzelne Räume und ihre Attribute, sowie Funktionen zum generieren, laden und speichern bereitstellt.

    """
    def __init__(self, name):
        """
        Initialisierung eines Raums

        Parameter:      -
        Rückgabewerte:  -
        """
        self.name = name
        self.col = gamemap.GameMap()
        self.bg = pygame.Surface
        self.objects = []
        self.doors = []

        if os.path.exists(name + ".rpkg"):
            self.loadFromRpkg(name + ".rpkg")
        else:
            self.generateRoomFromSource(name)

    def getCol(self):
        """
        Zurückgabe der Gamemap

        Parameter:      -
        Rückgabewerte:  Gamemap Gamemap des Raums
        """
        return self.col

    def getBg(self):
        """
        Zurückgabe des Hintergrundbilds

        Parameter:      -
        Rückgabewerte:  pygame.Surface Hintergrundbild des Raums
        """
        return self.bg

    def getObjects(self):
        """
        Zurückgabe der Objekte des Raums

        Parameter:      -
        Rückgabewerte:  list Objekte des Raums
        """
        return self.objects

    def getDoors(self):
        """
        Zurückgabe der Türen des Raums

        Parameter:      -
        Rückgabewerte:  list Türen des Raums
        """
        return self.doors

    def generateRoomFromSource(self, name):
        """
        Generieren des Raums aus Quelldateien

        Parameter:      str Name des Raums
        Rückgabewerte:  -
        """
        self.name = name
        self.col = gamemap.createByImage(name + "col.png")
        print name + "col.png"
        self.bg = pygame.image.load(name + ".png").convert()
        self.saveToRpkg()

    def saveToRpkg(self):
        """
        Speichern des Raums

        Parameter:      -
        Rückgabewerte:  -
        """
        room = (self.name, self.col, pygame.image.tostring(self.bg, "RGB"), self.bg.get_size(), self.objects, self.doors)
        try:
            Pickle.dump(room, open(self.name + ".rpkg", "wb"), 2)
        except Exception as e:
            print e

    def loadFromRpkg(self, path):
        """
        Laden des Raums

        Parameter:      str Dateiname/Pfad des zuladenen Raums
        Rückgabewerte:  -
        """
        try:
            room = Pickle.load(open(path, "rb"))
        except Exception as e:
            print e
        self.name = room[0]
        self.col = room[1]
        self.bg = pygame.image.fromstring(room[2], room[3], "RGB").convert()
        self.objects = room[4]
        self.doors = room[5]


