# -*- coding: cp1252 -*-
#Modules#

import random, math, pygame
import os, sys
import widget, entry, border, textwidget, listbox
import button
from pygame.locals import *
import label
import imagebox




pygame.init()

screen = pygame.display.set_mode((400,200),0,32)
pygame.mouse.set_visible(1)
pygame.key.set_repeat(1, 50)
pygame.display.set_caption('Cooles Spiel')
background = pygame.Surface((400,200))
background.fill((193, 205, 205))
WTaste = pygame.image.load("WTaste.png").convert_alpha()
ATaste = pygame.image.load("ATaste.png").convert_alpha()
STaste = pygame.image.load("STaste.png").convert_alpha()
DTaste = pygame.image.load("DTaste.png").convert_alpha()
LogoSchrift = pygame.image.load("LogoSchrift.png").convert_alpha()
Logo = pygame.image.load("Logo.png").convert_alpha()
LeftClick = pygame.image.load("Left_Click.png").convert_alpha()
Zurueck = pygame.image.load("Zurueck.png").convert_alpha()
myfont = pygame.font.SysFont("comicsansms", 25)
myfont1 = pygame.font.SysFont("comicsansms", 18)
print pygame.font.get_fonts()

def main_menu():

    bo = border.RoundedBorder((5,5),(5,5),(87,87,87),5)
    b1 = button.Button(120, 85, 150, 50, "Start", callback = buttonStart).setBackground((193, 205, 205)).setForeground((0, 0, 0)).setBorder(bo)
    b2 = button.Button(120, 150, 150, 50, "Steuerung", callback = buttonSteuerung).setBackground((193, 205, 205)).setForeground((0, 0, 0)).setBorder(bo)
    b3 = button.Button(375, 3, 20, 20, "!", callback = buttonInfo).setBackground((193, 205, 205)).setForeground((0, 0, 0)).setBorder(bo)

    Box1 = imagebox.Imagebox(120, 5, 150, 75, Logo).setBackground((193, 205, 205)).setForeground((0, 0, 0))

    group = pygame.sprite.LayeredDirty([b1, b2, b3, Box1])

    group.update()
    group.draw(screen, background)
    going = True
    while going:
        #Handle Input Events#
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            group.update(event)
        group.draw(screen, background)
        pygame.display.update()
        pygame.time.wait(100)
    pygame.quit()
    sys.exit()

    
def buttonStart():
   print "g"
   screen = pygame.display.set_mode((600,400),0,32)
   background = pygame.Surface((600,400))
   pygame.display.set_caption('Cooles Spiel')
   bo = border.RoundedBorder((5,5),(5,5),(87, 87, 87), 10)
   bo2 = border.RoundedBorder((1,1),(1,1),(87, 87, 87), 2)
   bo3= border.ColoredBorder(1, 1, (87, 87, 87))
   b1 = button.Button(50, 75, 100, 50, "Join Room").setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo)
   b2 = button.Button(250, 75, 100, 50, "Host Server").setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo)
   b3 = button.Button(375, 3, 20, 20, "?", callback = buttonHilfe).setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo2)
   b4 = button.Button(347, 3, 20, 20, "!", callback = buttonInfo).setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo2)
   e = entry.Entry(150, 165, 100, 15, "         n a m e").setBackground((199, 199, 199)).setForeground((87, 87, 87)).setBorder(bo3)
   l = label.Label(135, 145, 135, 10, "Enter your name here:").setBackground((199, 199, 199)).setForeground((87, 87, 87))
   l2 = label.Label(135, 35, 135, 10, "Cooles Spiel").setBackground((199, 199, 199)).setForeground((87, 87, 87))

   group = pygame.sprite.LayeredDirty([b1,b2,b3,b4,e,l,l2])

   group.update()
   group.draw(screen, background)
   going = True
   while going:
       #Handle Input Events#
       for event in pygame.event.get():
           if event.type == QUIT:
               going = False
           group.update(event)
       group.draw(screen, background)
       pygame.display.update()
       pygame.time.wait(100)
   pygame.quit()
   sys.exit()

def buttonHilfe ():
    print ("ZWAG B!")

def buttonSteuerung ():
    print ("ZWAG C!")
    bo = border.RoundedBorder((5,5),(5,5),(87,87,87),5)
    b1 = button.Button(10, 10, 50, 25, callback = main_menu).setBackground((193, 205, 205)).setForeground((0, 0, 0)).setBorder(bo).setIcon(Zurueck)

    #l1 = label.Label(112, 5, 175, 50, "Cooles Spiel").setBackground((193, 205, 205, 0)).setForeground((0, 0, 0)).setFont(myfont)
    l2 = label.Label(240, 55, 125, 30, "Schießen").setBackground((193, 205, 205)).setForeground((0, 0, 0)).setFont(myfont1)
    l3 = label.Label(55, 55, 125, 30, "Laufen").setBackground((193, 205, 205)).setForeground((0, 0, 0)).setFont(myfont1)
    Box1 = imagebox.Imagebox(90, 85, 50, 48, WTaste).setBackground((193, 205, 205)).setForeground((0, 0, 0))
    Box2 = imagebox.Imagebox(35, 138, 50, 48, ATaste).setBackground((193, 205, 205)).setForeground((0, 0, 0))
    Box3 = imagebox.Imagebox(90, 138, 50, 48, STaste).setBackground((193, 205, 205)).setForeground((0, 0, 0))
    Box4 = imagebox.Imagebox(145, 138, 50, 48, DTaste).setBackground((193, 205, 205)).setForeground((0, 0, 0))
    Box5 = imagebox.Imagebox(275, 95, 50, 70, LeftClick).setBackground((193, 205, 205)).setForeground((0, 0, 0))
    Box6 = imagebox.Imagebox(115, 5, 125, 50, LogoSchrift).setBackground((193, 205, 205)).setForeground((0, 0, 0))
    #l4 = label.Label(225, 175, 150, 10, "Cooles Spiel").setBackground((0, 0, 0)).setForeground((255, 255, 255))
    #l5 = label.Label(225, 225, 150, 10, "Cooles Spiel").setBackground((0, 0, 0)).setForeground((255, 255, 255))
    #l6 = label.Label(225, 275, 150, 10, "Cooles Spiel").setBackground((0, 0, 0)).setForeground((255, 255, 255))

    group = pygame.sprite.LayeredDirty([l2, l3, Box1, Box2, Box3, Box4, Box5, Box6, b1])
    print group.sprites()
    
    group.update()
    group.draw(screen, background)
    going = True
    while going:
        #Handle Input Events#
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            group.update(event)
        group.draw(screen, background)
        pygame.display.update()
        pygame.time.wait(100)
    pygame.quit()
    sys.exit()

def buttonInfo ():
    print ("G")
    Text = "Dieses Spiel wurde Designed vom Informatik Lk"
    bo = border.RoundedBorder((5,5),(5,5),(87,87,87),5)
    b1 = button.Button(10, 10, 50, 25, callback = main_menu).setBackground((193, 205, 205)).setForeground((0, 0, 0)).setBorder(bo).setIcon(Zurueck)
    
    l1 = listbox.Listbox(100, 90, 200, 100).setBackground((193, 205, 205)).setForeground((0, 0, 0 )).setBorder(bo)
    l1.insert(0,"Dieses Spiel wurde Designed")
    l1.insert(0,"vom Informatik Lk")
    l1.insert(0,"(Alina Gries, Gregor Rose,")
    l1.insert(0,"Kai Kriegel, Kerim Merdovic,")
    l1.insert(0,"Lucas Hoschar, Lucas Voelz,")
    l1.insert(0,"Niclas Affeld, Ovidiu Tatar,")
    l1.insert(0,"Till Koersmeier, Lukas Meyer)")
    
    Box1 = imagebox.Imagebox(120, 5, 150, 75, Logo).setBackground((193, 205, 205)).setForeground((0, 0, 0))

    group = pygame.sprite.LayeredDirty([l1, Box1, b1])
    print group.sprites()
    
    group.update()
    group.draw(screen, background)
    going = True
    while going:
        #Handle Input Events#
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            group.update(event)
        group.draw(screen, background)
        pygame.display.update()
        pygame.time.wait(100)
    pygame.quit()
    sys.exit()

    
def buttonJoin_Room ():
    pass

def buttonHost_Server ():
    pass

    

    
def isNumber(newtext, oldtext, widget):
    return not newtext or newtext.isdigit()

##def addText(self):
##    self.screen.blit(self.font.render('Hello!', True, (255,0,0)), (200, 100))
##    pygame.display.update()

def addRect(self):
    self.rect = pygame.draw.rect(self.screen, (black), (175, 75, 200, 100), 2)
    pygame.display.update()
    

#Automatic Start#

if __name__ == "__main__":
    main = main_menu()

