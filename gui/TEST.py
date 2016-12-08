#Modules#

import random
import os, sys
import pygame
import widget, border, entry
import button
from pygame.locals import *

pygame.init()

#Setting Display#

screen = pygame.display.set_mode((700,400),0,32)
pygame.mouse.set_visible(1)

background = pygame.Surface((700,350))
background.fill((255,255,255))

def main_menu():
    w = widget.Widget(50, 50, 50, 50).setBackground((255, 0, 0, 0)).setBorder(border.Border(2, 2))
    e = entry.Entry(10, 10, 100, 25).setBackground((0, 120, 255, 0))
    b = button.Button(100, 100, 100, 50, "click").setBackground((255,255,0,0))
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
    sys.exit()

#Automatic Start#

if __name__ == "__main__":
    main_menu()
