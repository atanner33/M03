#create a class called enemy

class Enemy:
    def __init__(self,energy):
        self.energy = energy

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
jason.get_energy()

sally = Enemy(6)
sally.get_energy()