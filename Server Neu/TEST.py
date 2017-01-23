# TEST
from connectionhandler import *

s = ConnectionHandler()
s.connect('localhost', 5001)
s.send('/MAKELOBBY hi')
s.send('/JOINLOBBY hi')
s.send('/LOBBYINTERACT START hi')
