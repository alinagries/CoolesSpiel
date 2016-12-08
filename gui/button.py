# -\*- coding: cp1252 -\*-

from __future__ import print_function
import widget
import pygame
import pygame.font as fnt

fnt.init()
defaultFont = fnt.Font(None, 24)

class Button(widget.Widget):
    def __init__(self, x, y, width, height, text = "", font = defaultFont):
        widget.Widget.__init__(self, x, y, width, height)
        self.text = text
        self.font = font

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




        widget.Widget.update(self, *args)

    def _updateOriginalImage(self, *args):
        widget.Widget._updateOriginalImage(self, *args)
        self._originalImage.blit(self.font.render(str(self.text), 1, (0, 0, 0)), (0, 0))
