# -*- coding: cp1252 -*-
#Datum:     04.01.2017
#Autor:     Kerim Merodivc
#Version:   2.0

"""
Dieses Skript ist eine GUI für das Login - Fenster, geschrieben in Python mit Pygame.
Man kann kann einem self.raum joinen und ein self.raum hosten.
Desweiteren gibt es ein Entry, wo man den Spielerself.namen eingeben kann.

"""

import sys

import random, math, pygame
from pygame.locals import *
import os, sys
from clientMaster import *


import border
import button
import entry
import label
import listbox
import imagebox, widget, textwidget



pygame.init()

screen = pygame.display.set_mode((400,200),0,32)
pygame.mouse.set_visible(1)
pygame.key.set_repeat(1,50)
caption = "Cooles Spiel"
pygame.display.set_caption(caption)

background = pygame.Surface((400,200))
background.fill((199,199,199))


WTaste = pygame.image.load("WTaste.png").convert_alpha()
ATaste = pygame.image.load("ATaste.png").convert_alpha()
STaste = pygame.image.load("STaste.png").convert_alpha()
DTaste = pygame.image.load("DTaste.png").convert_alpha()
LogoSchrift = pygame.image.load("LogoSchrift.png").convert_alpha()
Logo = pygame.image.load("Logo.png").convert_alpha()
LeftClick = pygame.image.load("Left_Click.png").convert_alpha()
Zurueck = pygame.image.load("Zurueck.png").convert_alpha()



class GUI():    
    def __init__(self):
        self.c = Client(self)
        self.lobbyNames = []
        self.name = ""
        self.raum = []
        self.c.getAllLobbys()

    def setAllLobbys(self, lobbyNames):
        self.lobbyNames = lobbyNames

    def main_login(self):

        self.name_global = ""+str(self.name)

        bo = border.RoundedBorder((5,5),(5,5),(87, 87, 87), 10)
        bo2 = border.RoundedBorder((1,1),(1,1),(87, 87, 87), 2)
        bo3= border.ColoredBorder(1, 1, (87, 87, 87))

        b1 = button.Button(50, 75, 100, 50, "Join Room", callback = self.join_room).setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo)
        b2 = button.Button(250, 75, 100, 50, "Host Server", callback = self.host_server).setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo)
        b3 = button.Button(375, 3, 20, 20, "?", callback = self.help_bu).setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo2)
        b4 = button.Button(347, 3, 20, 20, "!", callback = self.info_bu).setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo2)

        e = entry.Entry(150, 165, 100, 15,"").setBackground((199, 199, 199)).setForeground((87, 87, 87)).setBorder(bo3).setValidation(self.max_len)
        l = label.Label(70, 145, 265, 10, "Geben Sie hier iheren self.namen ein:").setBackground((199, 199, 199)).setForeground((87, 87, 87))

        Box1 = imagebox.Imagebox(150, 15, 100, 50, Logo).setBackground((199, 199, 199)).setForeground((0, 0, 0))
        group = pygame.sprite.LayeredDirty([b1,b2,b3,b4,e,l, Box1])
        
        group.update()
        group.draw(screen,background)
        
        going = True
        
        while going:
            #Handle Input Events#
            for event in pygame.event.get():
                if event.type == QUIT:
                    going = False
                group.update(event)
            self.name = e.getText()
            group.draw(screen, background)
            pygame.display.update()
            pygame.time.wait(100)
            e.getText()
        pygame.quit()
        sys.exit()


    def main_login2(self):

        bo = border.RoundedBorder((5,5),(5,5),(87, 87, 87), 10)
        bo2 = border.RoundedBorder((1,1),(1,1),(87, 87, 87), 2)
        bo3 = border.RoundedBorder((5, 5), (5, 5), (87, 87, 87), 4)

        b1 = button.Button(50, 75, 100, 50, "Join Room", callback = self.join_room).setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo)
        b2 = button.Button(250, 75, 100, 50, "Host Server", callback = self.host_server).setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo)
        b3 = button.Button(375, 3, 20, 20, "?", callback = self.help_bu).setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo2)
        b4 = button.Button(347, 3, 20, 20, "!", callback = self.info_bu).setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo2)
        b5 = button.Button(150, 175, 100, 10, "self.namen ändern !", callback = self.main_login).setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo3)

        l = label.Label(150, 150, 100, 15,"self.name:"+str(self.name)).setBackground((199, 199, 199)).setForeground((87, 87, 87))
        Box1 = imagebox.Imagebox(150, 15, 100, 50, Logo).setBackground((199, 199, 199)).setForeground((0, 0, 0))

        group = pygame.sprite.LayeredDirty([b1,b2,b3,b4,b5,l,Box1])

        self.update(group)


    def join_room(self):
        self.c.getAllLobbys()
        if len(self.name) == 0 :
            self.message_box()
        else:
            bo = border.RoundedBorder((5,5),(5,5),(87,87,87),5)
            bo2 = border.RoundedBorder((1,1),(1,1),(87, 87, 87), 2)
            bo3 = border.ColoredBorder(1, 1, (87, 87, 87))
            b = button.Button(20,20,50,10,"Zurück", callback=self.back).setBackground((87,87,87)).setForeground((255,255,255)).setBorder(bo)
            b2 = button.Button(265,20,50,10,"Suche", callback=self.suche).setBackground((87,87,87)).setForeground((255,255,255)).setBorder(bo)
            b3 = button.Button(265,50,50,10,"Join", callback = lambda: self.join(lb)).setBackground((87,87,87)).setForeground((255,255,255)).setBorder(bo)
            es = entry.Entry(150,18,100,15, "").setBackground((199,199,199)).setForeground((87,87,87)).setBorder(bo2).setValidation(self.max_len)
            l = label.Label(280, 185, 135, 10, "Name:"+str(self.name)).setBackground((199, 199, 199)).setForeground((87, 87, 87))
            l2 = label.Label(95, 22, 50, 10, "Suche:").setBackground((199, 199, 199)).setForeground((87, 87, 87))
            lb = listbox.Listbox(100, 40, 150, 150, editable=True).setBackground((199, 199, 199)).setForeground((87, 87, 87)).setBorder(bo3)
            
            
            group = pygame.sprite.LayeredDirty([b,b2, b3,es,l,l2,lb])
            for i in self.lobbyNames:
                lb.insert(0, i)
            self.update(group)



    def host_server(self):

        if len(self.name) == 0:
            self.message_box()
        else:
            bo = border.RoundedBorder((5, 5), (5, 5), (87, 87, 87), 5)
            bo2= border.ColoredBorder(1, 1, (87, 87, 87))

            b = button.Button(20, 20, 50, 10, "Zurück", callback=self.back).setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo)
            b2 = button.Button(150, 165, 100, 15, "Spiel starten", callback=self.lobby_start).setBackground((87, 87, 87)).setForeground((255, 255, 255)).setBorder(bo)

            l = label.Label(27, 95, 135, 10, "Spieleranzahl:").setBackground((199, 199, 199)).setForeground((87, 87, 87))
            l2 = label.Label(19, 60, 135, 10, "Raumname:").setBackground((199,199,199)).setForeground((87,87,87))

            self.servername = entry.Entry(160,57,100,15, "").setBackground((199,199,199)).setForeground((87,87,87)).setBorder(bo2).setValidation(self.max_len)
            self.spieleranzahl = entry.Entry(160, 92, 100, 15, "").setBackground((199, 199, 199)).setForeground((87, 87, 87)).setBorder(bo2).setValidation(self.onlynumb)


            group = pygame.sprite.LayeredDirty([b,b2,l,l2,self.servername,self.spieleranzahl])


            self.update(group)



    def message_box(self):

        bo = border.RoundedBorder((5, 5), (5, 5), (87, 87, 87), 5)
        l = label.Label(75, 80, 250, 10, "Bitte geben sie zuerst ihren Namen ein !").setBackground((199, 199, 199)).setForeground((87, 87, 87))
        b = button.Button(170,115,50,15, "OK", callback=self.main_login).setBackground((87,87,87)).setForeground((255,255,255)).setBorder(bo)


        group = pygame.sprite.LayeredDirty([l,b])

        self.update(group)



    def info_bu(self):
        print ("G")
        Text = "Dieses Spiel wurde Designed vom Informatik Lk"
        bo = border.RoundedBorder((2, 2), (2, 2), (87, 87, 87), 3)
        b1 = button.Button(10, 10, 50, 15, callback=self.back).setBackground((199, 199, 199)).setForeground(
            (0, 0, 0)).setBorder(bo).setIcon(Zurueck)

        l1 = listbox.Listbox(100, 90, 200, 100).setBackground((199, 199, 199)).setForeground((87, 87, 87)).setBorder(bo)
        l1.insert(0, "Dieses Spiel wurde Designed")
        l1.insert(0, "vom Informatik Lk")
        l1.insert(0, "(Alina Gries, Gregor Rose,")
        l1.insert(0, "Kai Kriegel, Kerim Merdovic,")
        l1.insert(0, "Lucas Hoschar, Lucas Voelz,")
        l1.insert(0, "Niclas Affeld, Ovidiu Tatar,")
        l1.insert(0, "Till Koersmeier, Lukas Meyer)")

        Box1 = imagebox.Imagebox(120, 5, 150, 75, Logo).setBackground((199, 199, 199)).setForeground((0, 0, 0))

        group = pygame.sprite.LayeredDirty([l1, Box1, b1])
        print group.sprites()
        self.update(group)


    def waitingForLobbyToStart(self):
        l = label.Label(27, 95, 135, 10, "Warte auf Spielstart").setBackground((199, 199, 199)).setForeground((87, 87, 87))
        group = pygame.sprite.LayeredDirty([l])
        self.update(group)
        

    def help_bu(self):

        bo = border.RoundedBorder((5, 5), (5, 5), (87, 87, 87), 5)
        b1 = button.Button(10, 10, 50, 15, callback=self.back).setBackground((199, 199, 199)).setForeground(
            (0, 0, 0)).setBorder(bo).setIcon(Zurueck)
        l2 = label.Label(240, 55, 125, 30, "Schießen").setBackground((193, 205, 205)).setForeground((0, 0, 0))
        l3 = label.Label(55, 55, 125, 30, "Laufen").setBackground((193, 205, 205)).setForeground((0, 0, 0))
        Box1 = imagebox.Imagebox(90, 85, 50, 48, WTaste).setBackground((193, 205, 205)).setForeground((0, 0, 0))
        Box2 = imagebox.Imagebox(35, 138, 50, 48, ATaste).setBackground((193, 205, 205)).setForeground((0, 0, 0))
        
        Box3 = imagebox.Imagebox(90, 138, 50, 48, STaste).setBackground((193, 205, 205)).setForeground((0, 0, 0))
        Box4 = imagebox.Imagebox(145, 138, 50, 48, DTaste).setBackground((193, 205, 205)).setForeground((0, 0, 0))
        Box5 = imagebox.Imagebox(275, 95, 50, 70, LeftClick).setBackground((193, 205, 205)).setForeground((0, 0, 0))
        Box6 = imagebox.Imagebox(115, 5, 125, 50, LogoSchrift).setBackground((193, 205, 205)).setForeground((0, 0, 0))

        group = pygame.sprite.LayeredDirty([b1, l2, l3, Box1, Box2, Box3, Box4, Box5, Box6])

        self.update(group)


    def update(self, group):
        group.update()
        group.draw(screen, background)
        going = True
        while going:
            # Handle Input Events#
            for event in pygame.event.get():
                if event.type == QUIT:
                    going = False
                group.update(event)
            group.draw(screen, background)
            pygame.display.update()
            pygame.time.wait(100)
        pygame.quit()
        sys.exit()

    def lobby_start(self):
        lobbyname = self.servername.getText()
        #anzahl = self.spieleranzahl.getText()
        self.c.registrateAsLobby(lobbyname)
        self.waitingForLobbyToStart()


    def getRaum(self):
        return self.raum

    def back(self):
        self.main_login2()

    def max_len(self, newtext, oldtext, widget):
        if len(newtext) <= 8:
            return True
        else:
            return False

    def onlynumb(self, newtext, oldtext, widget):
        return not newtext or newtext.isdigit()

    def getName(self):
        return self.name

    def getSpieleranzahl(self):
        return self.spieleranzahl

    def getServerName():
        return serverself.name

    def addRect(self):
        self.rect = pygame.draw.rect(self.screen, (black), (175, 75, 200, 100), 2)
        pygame.display.update()

    def suche():
        suche = es.getText()
        vergl = lb.getList()
        if suche == "":
            self.join_room()
        else:
            for i in vergl:
                if suche == i:
                    lb.delete(0,len(vergl))
                    lb.insert(0, i)

    def join(self, lb):
        index = lb.getSelection()[0]
        text =  lb.getText().replace("'","").replace(' ','').split(',')
        selection = text[index]
        self.c.joinLobby(selection)
        self.waitingForLobbyToStart()



if __name__ == "__main__":
    gui = GUI()
    gui.main_login()
