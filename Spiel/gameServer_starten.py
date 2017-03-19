import sys
from gameServer import *
from gameRequestHandler import GameRequestHandler
from socket import *
args = sys.argv
print args, "hallo args"
def start(port = 5000):
    server = MyGameServer(('0.0.0.0',port),GameRequestHandler, int(args[1]))
    try:
        print "Server started, waiting for connections."
        server.serve_forever()
    finally:
        server.shutdown()
        server.server_close()
        server = None
        print "Shut down!"
start(int(args[2]))
