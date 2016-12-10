# -*- coding: cp1252 -*-

import textwidget
import pygame


class Button(textwidget.TextWidget):

    """
    Clickable buttons
    """

    def __init__(self, x, y, width, height, text = "", font = textwidget.defaultFont, callback = None):
        """
        Initialisation of an Button

        parameters:     int x-coordinate of the Button (left)
                        int y-coordinate of the Button (top)
                        int width of the Button
                        int height of the Button
                        string text of the Button
                        pygame.font.Font font of the Button
                        function callback function to be called when Button is pressed
                return values:  -
                """
        textwidget.TextWidget.__init__(self, x, y, width, height, text, font)
        self._callback = callback

    def setValidation(self, callback):
        if callable(callback):
            self._callback = callback
        return self

    def getValidation(self):
        return self._callback

    def update(self, *args):
        """
        Handles the clicking of the Button and calls the function given in the constructor.

        parameters: tuple arguments for the update (first argument should be an instance pygame.event.Event)
        return values: -
        """
        if len(args) > 0:
            event = args[0]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    try:
                        self._callback()
                    except:
                        pass

        textwidget.TextWidget.update(self, *args)

    def _getAppearance(self, *args):
        """
        Blits the text to the Button's Surface and returns the result.

        private function

        parameters:     tuple arguments for the update (first argument should be an instance pygame.event.Event)
        return values:  pygame.Surface the underlying Widget's appearance
        """
        surface = textwidget.TextWidget._getAppearance(self, *args)
        center = surface.get_rect().center
        size = self._font.size(self._text)
        coords = (center[0] - size[0] / 2, center[1] - size[1] / 2)
        surface.blit(self._font.render(str(self._text), 1, (0, 0, 0)), coords) # Unsauber, aber es funktioniert!
        return surface
