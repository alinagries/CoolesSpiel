import pygame
import random
import math

#Ein Struktur entnommen aus: http://programarcadegames.com/python_examples/show_file.php?file=bullets.py


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

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
        screen_width = 700
        screen_height = 400
        speed = 5
        #screen = pygame.display.set_mode([screen_width, screen_height])
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

class Player2(pygame.sprite.Sprite):

    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super(Player2,self).__init__()
 
        self.image = pygame.Surface([20, 20])
        self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
    
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



        

class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super(Bullet,self).__init__()
        
        self.vector=(0,0)
        self.image = pygame.image.load("ball2.png")#pygame.Surface([4, 10])
        #self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.vectorlegth = 0

    def updateVector(self, vec):
        self.vector = vec
        self.vectorlength = math.hypot(vec[0], vec[1])

        
    def adjustVector(self):
        '''
        Gleicht den Vektor an, sodass die Kugel nicht schneller wird, wenn sie weiter vom Spieler entfernt ist.
        Paramter : -
        Rückgabewerte: (x,y) (angepasster Vektor)
        '''
        #muss n mal aufgerugen werden, soll, wenn es gegen eine Wand, hinderniss etc. fliegt
        length = self.vectorlength
        try:
            x = (self.vector[0] / (length /10)) #5 Geschwindigkeit des Schusses
            y = (self.vector[1] / (length /10))
            return ((x+(length/100)),(y+(length/100)))
        except:
            return self.vector

        
 
    def update(self):
        '''
        Bewegt die Kugel, benutzt dabei den Vektor, der mit adjustVektor angepasst wurde.
        Paramter : -
        Rückgabewerte: -
        '''
        newVec = self.adjustVector()
        self.rect.y += newVec[1]
        self.rect.x += newVec[0]
        
        #bullet.move_ip(vector)

 
# --- Create the window
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 
# Create a red player block
player = Player()
all_sprites_list.add(player)
player2 = Player2()
all_sprites_list.add(player2)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
player.rect.y = 370
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            player.update()
            player2.update()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
            bullet = Bullet()
            bullet1 = Bullet()
            #neu
            
            pos = event.pos 
            bx=player.rect.centerx
            by=player.rect.centery
            bx1=player2.rect.centerx
            by1=player2.rect.centery
            speed = 0.1
            vector = ((pos[0]- bx)*speed , (pos[1]- by)*speed)
            bullet.updateVector(vector)
            vector2 = ((pos[0]- bx1)*speed , (pos[1]- by1)*speed)
            bullet1.updateVector(vector2)
            
            # Set the bullet so it is where the player is
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y
            bullet1.rect.x = player2.rect.x
            bullet1.rect.y = player2.rect.y
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            all_sprites_list.add(bullet1)
            bullet_list.add(bullet1)

        if player.rect.colliderect(player2.rect):
            print "1 hit 2"
            player.rect.move(10,10)
        if player2.rect.colliderect(player.rect):
            print "2 hit 1"
            player2.rect.move(50,50)





             
    # --- Game logic
 
    # Call the update() method on all the sprites
    all_sprites_list.update()
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 20 frames per second
    clock.tick(60)
 
pygame.quit()
