# -*- coding: cp1252 -*-

import pygame

class Border():

    """
    Underlying class for Borders;
    intended for use together with pygame.Surface
    """

    def __init__(self, width, height):
        """
        Initialisation of a Border

        parameters:     int width of the Border on the left and right sides
                        int height of the Border on the top and bottom sides
        return values:  -
        """
        self.width  = width
        self.height = height

    def getBorderedImage(self, surface):
        """
        Draw the Border and return the bordered result

        parameters:     pygame.Surface the image to be bordered
        return values:  pygame.Surface the bordered result
        """
        if isinstance(surface, pygame.Surface) and not self.isEmptyBorder():
            size        = self.getBounds(surface.get_rect())
            bordered    = pygame.Surface(size.size, 0, surface)
            bordered.fill((0, 0, 0))
            bordered.blit(surface, (self.width, self.height))
            return bordered
        return surface

    def getBounds(self, rect):
        """
        Return the adjusted bounds so that they fit the Border

        parameters:     pygame.Rect the original bounds
        return values:  pygame.Rect the adjusted bounds
        """
        if isinstance(rect, pygame.Rect):
            return rect.inflate(self.width * 2, self.height * 2)
        return rect

    def isEmptyBorder(self):
        """
        Return if the Border is empty and therefore of zero size

        parameters:     -
        return values:  boolean is the Border empty
        """
        return (self.width + self.height) == 0
