#Autor/en:  Niclas, Gregor
#Datum:     ????
#Version:   1.0

from player import Player
import pygame

GREEN = (0, 255, 0)
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

class Player1(Player):
    def __init__(self):
        '''
        Initialisierung vom Player1
        Parameter:      -
        return values:  -
        '''
        Player.__init__(self)

class Player2(Player):
    def __init__(self):
        '''
        Initialisierung vom Player1
        Parameter:      -
        return values:  -
        '''
        Player.__init__(self)
        self.image.fill(GREEN)

    def update(self):
        screen_width = 700
        screen_height = 400
        speed = 5
        #screen = pygame.display.set_mode([screen_width, screen_height])
        """ Update the player's position. """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -speed)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, speed)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-speed, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(speed, 0)
        self.rect.clamp_ip(screen.get_rect())
