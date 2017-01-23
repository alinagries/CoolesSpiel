# -*- coding: cp1252 -*-
#Datum :    22/23.12.16
#Autor/en: Niclas A.,Gregor R.,(Lucas V.)
#Version:   1.0


#Ein Struktur entnommen aus: http://programarcadegames.com/python_examples/show_file.php?file=bullets.py
from player import Player
from bot import Bot
from bullet import Bullet
from weapon import Weapon
import gamemap
import pygame
import random
import math



WHITE = (255, 255, 255)
'''erstelle das Fenster'''
mymap = gamemap.createByImage()
screenWidth = mymap.getWidth()
screenHeight = mymap.getHeight()
screen = pygame.display.set_mode([screenWidth, screenHeight])
background = pygame.image.load("map.png").convert() 

pygame.key.set_repeat(1,100)
 
'''Bullet & Sprite Listen'''
allPlayers = pygame.sprite.Group()
#allSprites = pygame.sprite.Group()
allBullets = pygame.sprite.Group()
allWeapons = pygame.sprite.Group()


'''erstellt 2 Spieler'''
player1 = Player()
allPlayers.add(player1)
#allSprites.add(player1)
bot = Bot()
allPlayers.add(bot)
#allSprites.add(bot)

'''erstellt ein paar blaue Waffen'''
weapon1 = Weapon(1, 4, 10, 3)
weapon2 = Weapon(2, 2, 5, 5)
weapon3 = Weapon(.5, 1, 20, 10)
weapon4 = Weapon(1, 3, 7, 6)

#allSprites.add(weapon1)
allWeapons.add(weapon1)
#allSprites.add(weapon2)
allWeapons.add(weapon2)
#allSprites.add(weapon3)
allWeapons.add(weapon3)
#allSprites.add(weapon4)
allWeapons.add(weapon4)
clock = pygame.time.Clock()

score = 0
weapon1.rect.y = 200
weapon1.rect.x = 150
weapon2.rect.x = 300
weapon3.rect.y = 150
weapon4.rect.x = 50
player1.rect.y = 400
player1.rect.x = 20
bot.rect.y = 20
bot.rect.x = 25


margin = 20 #margin = pixel, die eine Kugel ueber den Spielfeldrand fliegen kann

def updateAllSprites():
    allPlayers.update(mymap)
    allBullets.update(mymap, margin)
    allWeapons.update()

def drawAllSprites():
    allPlayers.draw(screen)
    allBullets.draw(screen)
    allWeapons.draw(screen)
    
 
# -------- Main Program Loop -----------
'''Schleife, bis das Fenster geschlossen wird'''

done = False
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            player1.update(mymap)
            bot.update(mymap)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the left mouse button
            bullet = player1.shoot(player1.rect.centerx, player1.rect.centery, event.pos)
            if not bullet == None:
                allBullets.add(bullet)
            
    # --- Game logic
 
    '''updatet positionen der Sprites und zeichnet diese neu'''
    updateAllSprites()
    
    removeBullets = []
    removePlayers = []
    for bullet in allBullets:
        if bullet.allowedPosition:
            for player in allPlayers:
                if bullet.rect.colliderect(player.rect) and player.nick != bullet.playernick:
                    removeBullets.append(bullet)
                    player.isHit(bullet.damage)
                    if player.hp <= 0:
                        removePlayers.append(player)
        else:
            removeBullets.append(bullet)

    for bullet in removeBullets:
        allBullets.remove(bullet)
    for player in removePlayers:
        allPlayers.remove(player)

    removeWeapons = []
    for player in allPlayers:
        for weapon in allWeapons:
            if player.rect.colliderect(weapon.rect):
                player.equipWeapon(weapon)
                removeWeapons.append(weapon)

    for weapon in removeWeapons:
        allWeapons.remove(weapon)
        
    
    screen.blit(background,[0,0])
    drawAllSprites()
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)

 
pygame.quit()
