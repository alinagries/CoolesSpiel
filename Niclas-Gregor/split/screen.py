# -*- coding: cp1252 -*-
#Datum :    23.12.16
#Autor/en:  Lucas V.
#Version:   1.0

import pygame

class Screen():
    '''
    Diese Klasse dient nur fuer eine einheitlich gegebene Screenhoehe und breite
    '''
    def __init__(self, screenWidth = 600, screenHeight = 400):
        '''
        initialisierung des Screens
        Parameter:      int screenWidth, breite des Screens
                        int screenHeight, hoehe des Screens
        return values:  -
        '''
        self.screensize = screenWidth, screenHeight
        
    def getScreen(self):
        '''
        ausgabe des Screens
        Parameter:      -
        return values:  Tuple (int, int): breite des Screens, hoehe des Screens
        '''
        return self.screen
    
    def setScreen(self, screenWidth = 700, screenHeight = 400):
        '''
        Setzen der breite und hoehe des Screens
        Parameter:      int screenWidth, breite des Screens
                        int screenHeight, hoehe des Screens
        return values:  -
        '''
        self.screen = screenWidth, screenHeight