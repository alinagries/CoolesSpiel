from myloginserver import *
from myrequesthandler import MyRequestHandler
from socket import *

def start(port=5000):
    server = MyLoginServer(('localhost',port),MyRequestHandler)
    try:
        print "Server started, waiting for connections."
        server.serve_forever()
    finally:
        server.shutdown()
        server.server_close()
        server = None
        print "Shut down!"
start(80)
