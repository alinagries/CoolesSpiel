# -*- coding: cp1252 -*-

import pygame
import border

class ColoredBorder(border.Border):

    """
    Border with a color
    """

    def __init__(self, width, height, color):
        """
        Initialisation of a ColoredBorder

        parameters:     int width of the ColoredBorder on the left and right sides
                        int height of the ColoredBorder on the top and bottom sides
                        tuple of format pygame.Color representing the ColoredBorder's color
        return values:  -
        """
        border.Border.__init__(self, width, height)
        self.color = color

    def getBorderedImage(self, surface):
        """
        Draw the ColoredBorder and return the bordered result

        parameters:     pygame.Surface the image to be bordered
        return values:  pygame.Surface the bordered result
        """
        if isinstance(surface, pygame.Surface) and not self.isEmptyBorder():
            size        = self.getBounds(surface.get_rect())
            bordered    = pygame.Surface(size.size, 0, surface)
            bordered.fill(self.color)
            bordered.blit(surface, (self.width, self.height))
            return bordered
        return surface
