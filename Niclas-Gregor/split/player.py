#Autor/en:  Niclas, Gregor
#Datum:     ????
#Version:   1.0

import pygame

RED = (255, 0, 0)
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
 
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super(Player,self).__init__()
 
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        '''
        updated Den Playerbewegungen beim (knopfdruck events)
        -wird evtl. ueberschrieben-
        Parameter:      -
        return Value:   -
        '''
        screen_width = 700
        screen_height = 400
        speed = 5
        """ Update the player's position. """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.move_ip(0, -speed)
        if keys[pygame.K_s]:
            self.rect.move_ip(0, speed)
        if keys[pygame.K_a]:
            self.rect.move_ip(-speed, 0)
        if keys[pygame.K_d]:
            self.rect.move_ip(speed, 0)
        self.rect.clamp_ip(screen.get_rect())
