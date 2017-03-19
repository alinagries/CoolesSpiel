from myloginserver import *
from gameRequestHandler import GameRequestHandler
from socket import *

def start(port = 5000):
    server = MyGameServer(('localhost',port),GameRequestHandler, 2)
    try:
        print "Server started, waiting for connections."
        server.serve_forever()
    finally:
        server.shutdown()
        server.server_close()
        server = None
        print "Shut down!"
start(5000)
