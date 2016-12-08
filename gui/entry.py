# -*- coding: cp1252 -*-

import textwidget
import pygame

START   = 0
END     = 'e'
CURRENT = 'c'
INSERT  = CURRENT
CURSOR  = CURRENT

class Entry(textwidget.TextWidget):
    def __init__(self, x, y, width, height, text = "", font = textwidget.defaultFont, validation = (lambda *x: True)):
        textwidget.TextWidget.__init__(self, x, y, width, height, text, font)
        self._validation = validation
        self._cursor = 0

    def setText(self, text):
        if self._validation(text, self._text, self):
            textwidget.TextWidget.setText(self, text)
        return self

    def setValidation(self, validation):
        if isinstance(validation, function):
            self._validation = validation
        return self

    def getValidation(self):
        return self._validation

    def setCursor(self, index):
        self._cursor = self.getActualIndex(index)
        self.markDirty()

    def getCursor(self):
        return self._cursor

    def moveCursor(self, index):
        self.setCursor(min(max(self.getActualIndex(CURSOR) + int(index), 0), len(self._text)))

    def insert(self, index, text):
        index = self.getActualIndex(index)
        self.setText(self._text[:index] + text + self._text[index:])

    def delete(self, startindex, endindex):
        indices = [self.getActualIndex(startindex), self.getActualIndex(endindex)]
        indices.sort()
        startindex, endindex = indices
        self.setText(self._text[:startindex] + self._text[endindex:])

    def getActualIndex(self, index):
        if index == CURRENT:
            return self._cursor
        if index == END:
            return len(self._text)
        return abs(int(index))

    def _indexToX(self, index):
        x       = 0
        metrics = self._font.metrics(self._text)
        if metrics:
            for n in range(min(int(index), len(metrics))):
                x += metrics[n][4]
        return x

    def _xToIndex(self, x):
        index   = 0
        n       = 0
        metrics = self._font.metrics(self._text)
        if metrics:
            for index in range(len(metrics)):
                if n > int(x):
                    break
                n += metrics[index][4]
            else:
                index += 1
            if n - int(x) >= metrics[max(index - 1, 0)][4] / 2:
                index -= 1
        return index

    def update(self, *args):
        if len(args) > 0:
            event = args[0]
            if event.type == pygame.KEYDOWN and self.isFocused():
                if event.key == pygame.K_LEFT:
                    self.moveCursor(-1)
                elif event.key == pygame.K_RIGHT:
                    self.moveCursor(1)
                elif event.key == pygame.K_BACKSPACE:
                    self.delete(self.getActualIndex(CURSOR) - 1, CURSOR)
                    self.moveCursor(-1)
                else:
                    char = event.unicode.encode("ascii", "ignore")
                    if char == " " or not char.isspace():
                        self.insert(CURSOR, char)
                        self.moveCursor(1)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.setCursor(self._xToIndex(event.pos[0] - self.rect.x))
        textwidget.TextWidget.update(self, *args)

    def _updateOriginalImage(self, *args):
        linesize = self._font.get_linesize()
        textwidget.TextWidget._updateOriginalImage(self, *args)
        self._originalImage.blit(self._font.render(str(self._text), 1, self._foreground), (0, (self.rect.height - linesize) / 2))
        if self.isFocused():
            cursor = pygame.Surface((2, linesize))
            cursor.fill(self._foreground)
            self._originalImage.blit(cursor, (self._indexToX(self._cursor), (self.rect.height - linesize) / 2))
