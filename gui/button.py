# -*- coding: cp1252 -*-

from __future__ import print_function
import textwidget
import pygame

class Button(textwidget.TextWidget):
    def __init__(self, x, y, width, height, text = "", font = textwidget.defaultFont, func = None):
        textwidget.TextWidget.__init__(self, x, y, width, height, text, font)
        self.func = func

    def update(self, *args):
        if len(args) > 0:
            event = args[0]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.func()

        textwidget.TextWidget.update(self, *args)

    def _updateOriginalImage(self, *args):
        textwidget.TextWidget._updateOriginalImage(self, *args)
        center = self._originalImage.get_rect().center
        size = self._font.size(self._text)
        coords = (center[0]-size[0]/2, center[1]-size[1]/2)
        self._originalImage.blit(self._font.render(str(self._text), 1, (0, 0, 0)), coords) #Unsauber, aber es funktioniert!
