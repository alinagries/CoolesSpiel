# -*- coding: cp1252 -*-

from __future__ import print_function
import textwidget
import pygame

class Button(textwidget.TextWidget):
    def __init__(self, x, y, width, height, text = "", font = textwidget.defaultFont):
        textwidget.TextWidget.__init__(self, x, y, width, height, text, font)

    def clicked(self):
        print("Button was clicked") # Will be replaced with actual logic

    def update(self, *args):
        if len(args) > 0:
            event = args[0]
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if mouse[0] > self.rect.topleft[0]:
                    if mouse[1] > self.rect.topleft[1]:
                        if mouse[0] < self.rect.bottomright[0]:
                            if mouse[1] < self.rect.bottomright[1]:
                                self.clicked()




        textwidget.TextWidget.update(self, *args)

    def _updateOriginalImage(self, *args):
        textwidget.TextWidget._updateOriginalImage(self, *args)
        self._originalImage.blit(self._font.render(str(self._text), 1, (0, 0, 0)), (0, 0))
