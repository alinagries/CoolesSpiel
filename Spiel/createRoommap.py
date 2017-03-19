import room
import roommap
import door
import weapon

#import pygame
#pygame.init()
#if pygame.display.get_surface() == None:
#    testscreen = pygame.display.set_mode([800,800])

def createRoommap(parent):
    print 'create'
    room1 = room.Room("map3")
    room2 = room.Room("map3")

    door1 = door.Door(700, 400, room2, 440, 220)
    room1.setDoors([door1])

    door2 = door.Door(200, 200, room1, 700, 660)
    room2.setDoors([door2])

    weapon1 = weapon.Weapon(1, 4, 10, 3)
    weapon2 = weapon.Weapon(2, 2, 5, 5)
    weapon3 = weapon.Weapon(.2, 15, 20, 10000)
    weapon4 = weapon.Weapon(1, 3, 7, 6)
    weapon1.rect.y = 240
    weapon1.rect.x = 220
    weapon3.rect.x = 300
    weapon3.rect.y = 300
    weapon2.rect.x = 90
    weapon2.rect.y = 180
    weapon4.rect.x = 150
    weapon4.rect.y = 80

    room1.setEquippables([weapon1, weapon2, weapon3, weapon4])
    room2.setEquippables([weapon1, weapon3])

    roommap1 = roommap.RoomMap("std")
    roommap1.setStartRoom(room2)
    roommap1.setRooms([room1, room2])

    return roommap1

