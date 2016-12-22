import pygame
import random
import math

#Ein Struktur entnommen aus: http://programarcadegames.com/python_examples/show_file.php?file=bullets.py
from player1and2 import Player1
from player1and2 import Player2


'''Ein paar Farben'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

'''erstelle das Fenster'''
pygame.init()
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
'''Bullet & Sprite Listen'''
allSprites = pygame.sprite.Group()
allBullets = pygame.sprite.Group()
 
'''erstellt 2 Spieler'''
player1 = Player1()
allSprites.add(player)
player2 = Player2()
allSprites.add(player2)
 
 
clock = pygame.time.Clock()

score = 0
player.rect.y = 370
 
# -------- Main Program Loop -----------
'''Schleife, bis das Fenster geschlossen wird'''
done = False
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            player1.update()
            player2.update()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the left mouse button
            bullet1 = Bullet()
            bullet2 = Bullet()
            #neu
            
            eventPosition = event.pos 
            bullet1XPosition = player1.rect.centerx
            bullet1YPosition = player1.rect.centery
            bullet2XPosition = player2.rect.centerx
            bullet2YPosition = player2.rect.centery
            speed = 0.1
            vector = ((eventPosition[0]- bullet1XPosition)*speed , (eventPosition[1] - bullet1YPosition)*speed)
            bullet1.updateVector(vector)
            vector2 = ((eventPosition[0]- bullet2XPosition)*speed , (eventPosition[1]- bullet2YPosition)*speed)
            bullet2.updateVector(vector2)
            
            # Set the bullet so it is where the player is
            bullet1.rect.x = player1.rect.x
            bullet1.rect.y = player1.rect.y
            bullet2.rect.x = player2.rect.x
            bullet2.rect.y = player2.rect.y
            
            # Add the bullet to the lists
            allSprites.add(bullet1)
            allBullets.add(bullet1)
            allSprites.add(bullet2)
            allBullets.add(bullet2)

        '''das laueft nur waehrend events, is bloed gemacht! muss ueberarbeitet werden!'''
        if player.rect.colliderect(player2.rect):
            print "1 hit 2"
            player.rect.move(10, 10)
        if player2.rect.colliderect(player.rect):
            print "2 hit 1"
            player2.rect.move(50, 50)
             
    # --- Game logic
 
    # Call the update() method on all the sprites
    allSprites.update()
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Draw all the spites
    allSprites.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)
 
pygame.quit()
