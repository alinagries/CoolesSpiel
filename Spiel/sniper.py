from weapon import Weapon

class Sniper(Weapon):
    def __init__(self):
        Weapon.__init__(self, 0.5, 2, 5, 5)
        
