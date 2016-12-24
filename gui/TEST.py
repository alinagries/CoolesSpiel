# -*- coding: cp1252 -*-
#Modules#

import random
import os, sys
import pygame
import widget, entry, border
import button
from pygame.locals import *

pygame.init()

#Setting Display#

screen = pygame.display.set_mode((700,400),0,32)
pygame.mouse.set_visible(1)
pygame.key.set_repeat(1, 50)

background = pygame.Surface((700,350))
background.fill((255,255,255))

def main_menu():
    w = widget.Widget(50, 50, 50, 50).setBackground((255, 0, 0, 50)).setBorder(border.RoundedBorder((10, 80), (5, 10), (0, 0, 0), 8))
    r = border.CompoundBorder(border.CompoundBorder(border.BevelBorder(2, 2, (30, 90, 150), (30, 190, 50)), border.ColoredBorder(3, 3, (130, 190, 250, 200))), border.ColoredBorder(2, 2, (30, 90, 150, 100)))
    e = entry.Entry(10, 10, 100, 25).setBackground((0, 120, 255)).setBorder(r).setValidation(isNumber)
    b = button.Button(100, 100, 100, 50, "click", callback = button1).setBackground((255, 255, 0)).setForeground((0, 0, 0))
    group = pygame.sprite.LayeredDirty([w, e, b])
    
    going = True
    while going:
        #Handle Input Events#
        mouse_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            group.update(event)
        group.draw(screen, background)
        pygame.display.update()
        pygame.time.wait(100)
    pygame.quit()
    sys.exit()

def button1():
    print("Button b clicked!")

def isNumber(newtext, oldtext, widget):
    return not newtext or newtext.isdigit()

#Automatic Start#

if __name__ == "__main__":
    main_menu()
