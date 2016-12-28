# -*- coding: cp1252 -*-
#Datum :    22/23.12.16
#Autor/en:  Lucas V.
#Version:   1.0

from screen import Screen
import pygame
import random
import math

#Ein Struktur entnommen aus: http://programarcadegames.com/python_examples/show_file.php?file=bullets.py
from player import Player
from bot import Bot
from bullet import Bullet

WHITE = (255, 255, 255)

'''erstelle das Fenster'''
pygame.init()
screensize = Screen().screensize
screenWidth = screensize[0]
screenHeight = screensize[1]
screen = pygame.display.set_mode([screenWidth, screenHeight])
 
'''Bullet & Sprite Listen'''
allPlayers = pygame.sprite.Group()
allSprites = pygame.sprite.Group()
allBullets = pygame.sprite.Group()

'''erstellt 2 Spieler'''
player1 = Player()
allPlayers.add(player1)
allSprites.add(player1)
bot = Bot()
allPlayers.add(bot)
allSprites.add(bot)

clock = pygame.time.Clock()

score = 0
player1.rect.y = 370
 
# -------- Main Program Loop -----------
'''Schleife, bis das Fenster geschlossen wird'''

margin = 20
#margin = pixel, die eine Kugel ueber den Spielfeldrand fliegen kann
done = False
print 'Bugs bei einer Bulletspeed < 0,2'
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            player1.update()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the left mouse button

            bullet = player1.shoot(player1.rect.centerx, player1.rect.centery, event.pos)
            if not bullet == None:
                allSprites.add(bullet)
                allBullets.add(bullet)
            
    # --- Game logic
 
    '''updatet positionen der Sprites und zeichnet diese neu'''
    allSprites.update()

    removeBullets = []
    removePlayers = []
    for bullet in allBullets:
        if bullet.rect[0] > screenWidth + margin or bullet.rect[1] > screenHeight + margin:
            removeBullets.append(bullet)
        elif bullet.rect[0] < -margin or bullet.rect[1] < -margin:
            removeBullets.append(bullet)
        for player in allPlayers:
            if bullet.rect.colliderect(player.rect) and player.nick != bullet.playernick:
                removeBullets.append(bullet)
                player.isHit(bullet.damage)
                if player.hp < 0:
                    removePlayers.append(player)

    for bullet in removeBullets:
        allBullets.remove(bullet)
        allSprites.remove(bullet)
    for player in removePlayers:
        allPlayers.remove(player)
        allSprites.remove(player)
    
    screen.fill(WHITE)
    allSprites.draw(screen)
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)

    
 
pygame.quit()
