import room
import roommap
import door
import weapon

def createRoommap(parent):
    room0 = room.Room("0", parent)
    room1 = room.Room("1", parent)

    door0 = door.Door(230, 50, room1, 500, 240)
    room0.setDoors([door0])

    door1 = door.Door(220, 400, room0, 300, 300)
    room1.setDoors([door1])

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

    room0.setEquippables([weapon1, weapon2, weapon3, weapon4])
    room1.setEquippables([weapon1, weapon3])

    roommap1 = roommap.RoomMap("std")
    roommap1.setStartRoom(room0)
    roommap1.setRooms([room0, room1])

    print 'door0', door0.rect.center, 'room', door0.room.getName()
    print 'door1', door1.rect.center, 'room', door1.room.getName()


    return roommap1

