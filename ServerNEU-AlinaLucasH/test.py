from client import Client

class hehe:
    def __init__(self):
        self.shot = ""
        self.positions = ""
        
    def shoot(self, a):
        self.shot = a

    def updatePlayers(self, a):
        self.positions = a

f = hehe()
c = Client(f)

