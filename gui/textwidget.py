# -*- coding: cp1252 -*-

import widget
import pygame
import pygame.font as fnt

fnt.init()
defaultFont = fnt.Font(None, 18)

class TextWidget(widget.Widget):
    def __init__(self, x, y, width, height, text = "", font = defaultFont):
        widget.Widget.__init__(self, x, y, width, height)
        self._text = text
        self._font = font
        
    def setText(self, text):
        self._text = str(text)
        self.markDirty()
        return self

    def getText(self):
        return self._text

    def setFont(self, font):
        if isinstance(font, fnt.Font):
            self._font = font
            self.markDirty()
        return self

    def getFont(self):
        return self._font
