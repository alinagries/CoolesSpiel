# -*- coding: utf-8 -*-
#Datum :    11.03.2017
#Autor/en: Kai K.
#Version:   1.0

import pygame.sprite


class Door(pygame.sprite.Sprite):

    """
    Klasse die Türen, also die Übergänge zwischen Räumen darstellt.
    """

    def __init__(self, x, y, room, ex, ey):
        """
        Initialisierung einer Tür

        Parameter:      x x-Position der Tür
                        y y-Position der Tür
                        room.Room Raum der geladen werden soll
        Rückgabewerte:  -
        """
        super(Door, self).__init__()
        self.image = pygame.Surface([10, 10])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill((255,255,0))
        self.room = room
        self.exitpoint = (ex, ey)


    def getRoom(self):
        """
        Zurückgabe des raums

        Parameter:      -
        Rückgabewerte:  room.Room Raum zu dem diese Door den Übergang darstellt
        """
        return self.room

    def getExitpoint(self):
        """
        Zurückgabe des Ausgangs im nächsten Raum

        Parameter:      -
        Rückgabewerte:  tuple x-, y-Position des Ausgangs
        """
        return self.exitpoint
