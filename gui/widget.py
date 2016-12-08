# -*- coding: cp1252 -*-

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
        self._originalImage     = pygame.Surface((width, height))
        self._border            = defaultBorder
        self.image              = self._originalImage.copy()
        self.rect               = self.image.get_rect().move(x, y)
        self._focus             = False
        self._active            = True
        self._foreground        = defaultForeground
        self._background        = defaultBackground

    def markDirty(self):
        if not self.isDirtyForever():
            self.dirty = 1

    def markDirtyForever(self):
        self.dirty = 2

    def markClean(self):
        self.dirty = 0

    def isDirty(self):
        return self.dirty >= 1

    def isDirtyForever(self):
        return self.dirty >= 2

    def setFocused(self, focused):
        self._focus = bool(focused)
        self.markDirty()
        return self

    def isFocused(self):
        return self._focus

    def setActive(self, active):
        self._active = bool(active)
        self.markDirty()
        return self

    def isActive(self):
        return self._active

    def setBounds(self, width, height):
        self.rect = pygame.Rect(self.rect.x, self.rect.y, width, height)
        self.markDirty()
        return self

    def getBounds(self):
        return self.rect

    def setBorder(self, border):
        if isinstance(border, brd.Border):
            self._border = border
            self.markDirty()
        return self

    def getBorder(self):
        return self._border

    def setForeground(self, color):
        self._foreground = color
        self.markDirty()
        return self

    def setBackground(self, color):
        self._background = color
        self.markDirty()
        return self

    def getForeground(self):
        return self._foreground

    def getBackground(self):
        return self._background

    def update(self, *args):
        if len(args) > 0:
            event = args[0]
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.setFocused(self.rect.collidepoint(event.pos))
        if self.isDirty():
            self._updateOriginalImage(*args)
            self.image = self._border.getBorderedImage(self._originalImage.copy())
            self.rect = pygame.Rect(self.rect.x, self.rect.y,
                                self.image.get_width(), self.image.get_height())

    def _updateOriginalImage(self, *args):
        self._originalImage.fill(self._background)
        if not self.isActive():
            self._originalImage.blend(disabeledOverlay,(0,0))
