# -*- coding: cp1252 -*-

import pygame
import border

class BevelBorder(border.Border):

    """
    Border with two colors, creating a bevel-effect
    """

    def __init__(self, width, height, upper, lower):
        """
        Initialisation of a BevelBorder

        parameters:     int width of the BevelBorder on the left and right sides
                        int height of the BevelBorder on the top and bottom sides
                        tuple of format pygame.Color representing the BevelBorder's upper color
                        tuple of format pygame.Color representing the ColoredBorder's lower color
        return values:  -
        """
        border.Border.__init__(self, width, height)
        self.upper = upper
        self.lower = lower

    def getBorderedImage(self, surface):
        """
        Draw the ColoredBorder and return the bordered result

        parameters:     pygame.Surface the image to be bordered
        return values:  pygame.Surface the bordered result
        """
        if isinstance(surface, pygame.Surface) and not self.isEmptyBorder():
            size        = self.getBounds(surface.get_rect())
            upperhalf   = pygame.Surface(size.size, 0, surface)
            lowerhalf   = pygame.Surface(size.inflate(-self.width, -self.height).size, 0, surface)
            upperhalf.fill(self.upper)
            lowerhalf.fill(self.lower)
            upperhalf.blit(lowerhalf, (self.width, self.height))
            upperhalf.blit(surface, (self.width, self.height))
            return upperhalf
        return surface
