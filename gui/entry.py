# -\*- coding: cp1252 -\*-

import widget
import pygame
import pygame.font as fnt

fnt.init()
defaultFont = fnt.Font(None, 24)

class Entry(widget.Widget):
    def __init__(self, x, y, width, height, text = "", font = defaultFont):
        widget.Widget.__init__(self, x, y, width, height)
        self.text = text
        self.font = font

    def update(self, *args):
        if len(args) > 0:
            event = args[0]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        widget.Widget.update(self, args)

    def _updateOriginalImage(self, *args):
        widget.Widget._updateOriginalImage(self, args)
        self._originalImage.blit(self.font.render(str(self.text), 1,(0, 0, 0)), (0, 0))
