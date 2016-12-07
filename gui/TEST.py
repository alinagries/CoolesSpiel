#Modules#

import random
import os, sys
import pygame
from pygame.locals import *
import widget, border, entry

pygame.init()

#Setting Display#

screen = pygame.display.set_mode((700,400),0,32)
pygame.mouse.set_visible(1)

background = pygame.Surface((700,350))
background.fill((255,255,255))

def main_menu():
    w = widget.Widget(50, 50, 50, 50).setBackground((255, 0, 0, 0)).setBorder(border.Border(2, 2))
    e = entry.Entry(10, 10, 100, 25).setBackground((0, 120, 255, 0))
    going = True
    while going:
        #Handle Input Events#
        mouse_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
        screen.blit(background,(0,0))
        w.update(event)
        screen.blit(w.image, w.rect)
        e.update(event)
        screen.blit(e.image, e.rect)
        pygame.display.update()
        pygame.time.wait(100)
    sys.exit()

#Automatic Start#

if __name__ == "__main__":
    main_menu()
