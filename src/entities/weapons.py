# Contient les caractéristiques des armes.


# une seule arme pour l'instant (arc)

class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range