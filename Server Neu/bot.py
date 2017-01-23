#Autor/en:  Niclas, Gregor
#Datum:     ????
#Version:   1.0

from weapon import Weapon
from player import Player
import pygame

GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Bot(Player):
    def __init__(self, nick = 'nick'):
        '''
        Initialisierung vom Player1
        Parameter:      -
        return values:  -
        '''
        Player.__init__(self, nick)
        self.image.fill(RED)

    def shoot(self, xPosition, yPosition, eventPosition):
        pass

    def update(self,gamemap):
        pass
#        screen_width = 550
#        screen_height = 550
#        speed = 5
#        #screen = pygame.display.set_mode([screen_width, screen_height])
#        """ Update the player's position. """
#        keys = pygame.key.get_pressed()
#        
#        newRect = self.rect
#        if keys[pygame.K_UP]:
#            newRect = self.rect.move(0, -speed)
#        if keys[pygame.K_DOWN]:
#            newRect = self.rect.move(0, speed)
#        if keys[pygame.K_LEFT]:
#            newRect = self.rect.move(-speed, 0)
#        if keys[pygame.K_RIGHT]:
#            newRect = self.rect.move(speed, 0)
        

#        if gamemap.isRectValid(newRect):
#            self.rect = newRect
        #self.rect.clamp_ip(screen.get_rect())    
        #if bot.rect.colliderect(bot.rect):
           # self.rect.x = 650
            #self.rect.y = 350
            #player.__init__()
            #player2.__init__()


        
    def secondaryWeapon(self):
        '''
        Der Spieler bekommt das Objekt der Standartwaffe zugewiesen
        Parameter:      -
        return values:  -
        '''
        self.weapon = Weapon()
        
    def isHit(self, damage):
        '''
        errechnung der Spielerhitpoints nach einem treffer
        Parameter:      Float, damage gegen den Spieler
        return values:  -
        '''
        #resistance = 0
        #for armor in self.armors:
        #    resistance += armor.getResistance()
        #    armor.use()
        #    if armor.durability == 0:
        #        self.removeArmor(armor)
        #remainingDamage = damage - resistance
        #if remainingDamage > 0:
        #    self.hp -= remainingDamage
        self.hp -= damage
        
    def equipWeapon(self, weapon):
        self.weapon = weapon
            
##################### Getters und Setters, die momentan nirgends gebraucht werden, aber dazu gehoeren #####################

    def getNick(self):
        '''
        Ausgabe des Spielernicknames
        Parameter:      -
        return values:  String, nickname des Spielers
        '''
        return self.nick
    
    def setNick(self, nick):
        '''
        setzt den Spielernickname
        Parameter:      String, nickname des Spielers
        return values:  -
        '''
        self.nick = nick
        
    def getHitpoints(self):
        '''
        Ausgabe der Spielerhitpoints
        Parameter:      -
        return values:  Float hitpoints des Spielers
        '''
        return self.hp
    
    def setHitpoints(self, hp):
        '''
        setzt die Spielerhitpoints
        Parameter:      Float, Spielerhitpoints
        return values:  -
        '''
        self.hp = hp
    
    def getWeapon(self):
        '''
        Ausgabe der Waffe des Spielers
        Parameter:      -
        return values:  Objekt, von einer der Klasse Weapon
        '''
        return self.weapon
    
    def setWeapon(self, weapon):
        '''
        Der Spieler bekommt ein Objekt der Klasse Weapon, auf self.weapon
        Parameter:      Objekt der Klasse Weapon
        return values:  -
        '''
        self.weapon = weapon

