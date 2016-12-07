import pygame

class Border():

    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def getBorderedImage(self, surface):
        if isinstance(surface, pygame.Surface) and not self.isEmptyBorder():
            size        = self.getBounds(surface.get_rect())
            bordered  = pygame.Surface((size.width, size.height), 0, surface)
            bordered.fill((0, 0, 0), size)
            bordered.blit(surface, (self.width, self.height))
            return bordered
        return surface

    def getBounds(self, rect):
        if isinstance(rect, pygame.Rect):
            return rect.inflate(self.width * 2, self.height * 2)
        return rect

    def isEmptyBorder(self):
        return (self.width + self.height) == 0
