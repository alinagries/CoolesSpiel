from myloginserver import *
from myMasterRequestHandler import MasterRequestHandler
from socket import *

def start(port = 5000):
    server = MyMasterServer(('localhost',port),MasterRequestHandler)
    try:
        print "Server started, waiting for connections."
        server.serve_forever()
    finally:
        server.shutdown()
        server.server_close()
        server = None
        print "Shut down!"
start(5000)
