from Animaux import *
class Serpent(Animaux):

    def __init__(self, name, categorie,tete, force, defence, hp, chance_crit, endurance, sang_froid):
        super().__init__(name, categorie,tete, force, defence, hp, chance_crit, endurance)
        self._sang_froid = sang_froid

   

    def get_sang_froid():
        return sang_froid

    def set_sang_froid(sang_froid):
        self._sang_froid = sang_froid


