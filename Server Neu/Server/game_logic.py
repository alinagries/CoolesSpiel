''' TODO Gamelogic '''             
from threading import RLock

a=RLock()
b=RLock()
b.acquire()

def hi():
    b.acquire()
    print "negro"

def neg():
    a.acquire()
    print "AA"
    hi()
    print "BB"
