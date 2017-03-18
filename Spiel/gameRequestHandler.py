import SocketServer
 
class GameRequestHandler(SocketServer.StreamRequestHandler):
    """
    Klasse zur Kommunikation mit einem jeweiligen Client
    """

    def __init__(self, request, client_address, server):
        self.ip = client_address
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)
     
         
    def setup(self):
        """
        Herstellen einer Kommunikation
         
        Parameter:      -
        Rueckgabewerte:  -
        """

        SocketServer.StreamRequestHandler.setup(self)
        self.server.game.addPlayer(self.ip)
        self.sendToClient(self.ip)
        print "%s:%d connected" % self.client_address
         
    def finish(self):
        """
        Beenden einer Kommunikation
         
        Parameter:      -
        Rueckgabewerte:  -
        """
        self.server.game.removePlayer(self)
        SocketServer.StreamRequestHandler.finish(self)
        print "%s:%d disconnected" % self.client_address
         
    def handle(self):
        """
        Behandeln der Anfragen vom Client
         
        Parameter:      -
        Rueckgabewerte:  -
        """
        while True:
            try:
                line = self.rfile.readline()
            except:
                line = None
            if not line:
                break

            line = line.strip()
            cmd = line.upper().split(" ")[0]
            args = line.split(" ")[1:]
            if cmd in ("/QUIT", "/EXIT"):
                break
             
            elif cmd == "/UPDATEPOS": #playerposition: Nickname, Position
                self.server.game.updatePlayerPosition(args[0], self.ip)
            elif cmd == "/SHOOT": #schuss: Schussrichtung Spielernamen
                self.server.game.shoot(args[0], self.ip)
            elif cmd == "/UPDATEW":
                self.server.game.updateWeapon(args[0])
            else:
                print('Server recieved bad data "{0}"'.format(line))

 
##      OPTIONAL
##            if line.upper().startswith("/ALLPLAYERS"): #AlleSpieler: lobby_name??
##                self.sendToClient(self.server.game.getAllPlayersName())
##            if line.upper().startswith("/GETWEAPON"): #GibWaffe Nickname
##                self.sendToClient(self.server.game.getPlayersWeapon(line.split[1]))
##            if cmd == ("/REGISTER", "/LOGIN"):
##                self.IP = line.split()[1]
##                self.server.login.requestLogin(self.IP = line.split()[1])
##                continue
##            if line.upper().startswith("/UPDATEPLAYER"):
##                self.sendToClient(self.server.game.updatePosition(line.split[1]))
                 
        self.finish()
 
 
    def sendToClient(self, data):
        """
        Senden von Daten dem Client
         
        Parameter:      object Daten, die dem Client gesendet werden sollen
        Rueckgabewerte:  -
        """
        self.wfile.write(data)
