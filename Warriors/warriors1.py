class Warrior:
    def __init__(self,health=50,attack=5):
        self.health = health
        self.attack = attack
        is_alive = True

class Knight(Warrior):
    attack = 7

a = Knight()
print(a.attack)