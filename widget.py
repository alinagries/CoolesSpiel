import pygame.sprite
import pygame
import border as brd

defaultBorder       = brd.Border(0, 0)
defaultForeground   = (255, 255, 255, 0)
defaultBackground   = (0, 0, 0, 0)
disabeledOverlay    = (150, 150, 150, 150)

class Widget(pygame.sprite.DirtySprite):
    
    def __init__(self, x, y, width, height):
        pygame.sprite.DirtySprite.__init__(self)
        self.__originalImage    = pygame.Surface((width, height))
        self.__border           = defaultBorder
        self.image              = self.__originalImage.copy()
        self.rect               = self.image.get_rect().move(x, y)
        self.__active           = True
        self.__foreground       = defaultForeground
        self.__background       = defaultBackground

    def markDirty(self):
        if not self.isDirtyForever():
            self.dirty = 1

    def markDirtyForever(self):
        self.dirty = 2

    def markClean(self):
        self.dirty = 0

    def isDirty(self):
        return self.dirty == 1

    def isDirtyForever(self):
        return self.dirty == 2

    def setActive(self, active):
        self.__active = bool(active)
        self.markDirty()
        return self

    def isActive(self):
        return self.__active

    def setBounds(self, width, height):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, width, height)
        self.markDirty()
        return self

    def getBounds(self):
        return self.rect

    def setBorder(self, border):
        if isinstance(border, brd.Border):
            self.__border = border
            self.markDirty()
        return self

    def getBorder(self):
        return self.__border

    def setForeground(self, color):
        self.__foreground = color
        return self

    def setBackground(self, color):
        self.__background = color
        return self

    def getForeground(self):
        return self.__foreground

    def getBackground(self):
        return self.__background

    def update(self, *args):
        self.__updateOriginalImage(*args)
        self.image = self.__border.getBorderedImage(self.__originalImage.copy())
        self.rect = pygame.Rect(self.rect.x, self.rect.y,
                                self.image.get_width(), self.image.get_height())

    def __updateOriginalImage(self, *args):
        self.__originalImage.fill(self.__background)
        if not self.isActive():
            self.__originalImage.blend(disabeledOverlay,(0,0))
