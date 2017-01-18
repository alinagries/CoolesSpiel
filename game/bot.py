#Autor/en:  Niclas, Gregor
#Datum:     ????
#Version:   1.0

from screen import Screen
from weapon import Weapon
from player import Player
import pygame

GREEN = (0, 255, 0)
RED = (255, 0, 0)
screensize = Screen().screensize
screenWidth = screensize[0]
screenHeight = screensize[1]
screen = pygame.display.set_mode([screenWidth, screenHeight])

class Bot(Player):
    def __init__(self, nick = 'nick'):
        '''
        Initialisierung vom Player1
        Parameter:      -
        return values:  -
        '''
        Player.__init__(self, nick)
        self.image.fill(RED)

    def update(self,gamemap):
        screen_width = 550
        screen_height = 550
        speed = 5
        #screen = pygame.display.set_mode([screen_width, screen_height])
        """ Update the player's position. """
        keys = pygame.key.get_pressed()
        
        newRect = self.rect
        if keys[pygame.K_UP]:
            newRect = self.rect.move(0, -speed)
        if keys[pygame.K_DOWN]:
            newRect = self.rect.move(0, speed)
        if keys[pygame.K_LEFT]:
            newRect = self.rect.move(-speed, 0)
        if keys[pygame.K_RIGHT]:
            newRect = self.rect.move(speed, 0)
        

        if gamemap.isRectValid(newRect):
            self.rect = newRect
        #self.rect.clamp_ip(screen.get_rect())    
        #if bot.rect.colliderect(bot.rect):
           # self.rect.x = 650
            #self.rect.y = 350
            #player.__init__()
            #player2.__init__()

    def shoot(self, xPos, yPos, eventPos):
        '''
        Wenn moeglich (hoechstens wegen der zu vielen schussversuchen pro
        Sekunde nicht moeglich) wird ein Objekt Bullet erstellt.
        Falls keine Munition mehr vorhanden ist auf Standartwaffe wechseln
        Parameter:      int xPos, die x-Position des Spielers
                        int yPos, die y-Position des Spielers
                        Tuple (int, int), das Ziel des Schusses
        return values:  Boolean ODER None
                            je nachdem ob die Waffe einen schuss abfeuern darf
                            bsp. bei einer Waffengeschwindigkeit von 1 darf nach
                            0.5 Sekunden kein weiterer Schuss abgefeuert werden
        '''
        bullet = None
        position = xPos, yPos
        weapon = self.weapon
        try:
            bullet = weapon.createBullet(position, eventPos, self.nick)#eventPos = Zielposition
        except:
            print 'bullet wird nicht erzeugt'
        if weapon.ammo == 0:
            self.secondaryWeapon()
            
        return bullet
        
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

