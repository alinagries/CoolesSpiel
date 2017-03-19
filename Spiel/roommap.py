# -*- coding: utf-8 -*-
#Datum :    11.03.2017
#Autor/en: Kai K.
#Version:   1.0

import room

class RoomMap:

    """
    Klasse die einen kompletten Satz von Räumen und Türen darstellt
    """

    def __init__(self, name):
        """
        Initialisierung einer Tür

        Parameter:      str Name der Datei die
        Rückgabewerte:  -
        """
        self.name       = name
        self.rooms      = []
        self.startRoom  = None

    def getStartRoom(self):
        """
        Zurückgabe des startraums

        Parameter:      -
        Rückgabewerte:  room.Room Erster Raum der geladen wird
        """
        return self.startRoom

    def setStartRoom(self, room):
        """
        Setzen des Startraums

        Parameter:      room.Room Erster Raum der geladen wird
        Rückgabewerte:  -
        """
        self.startRoom = room

    def getRooms(self):
        """
        Zurückgabe der Räume

        Parameter:      -
        Rückgabewerte:  list Liste von Räumen
        """
        return self.rooms

    def setRooms(self, rooms):
        """
        Setzen der Räume

        Parameter:      list Liste von Räumen
        Rückgabewerte:  -
        """
        self.rooms = rooms


