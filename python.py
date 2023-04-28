from Serpent import *

class python(Serpent):

    def __init__(self, name, categorie,tete, force, defence, hp, chance_crit, endurance, sang_froid):
        super().__init__(sang_froid)
        self._sonette = True


    def attaque_sonette():
         print("ssss ssss attaque sonette !")

         if (self._sonette == True && self._sang_froid > 0):
            vie_perdu=(self._force - serpent._defence)*(serpent._defence//100)
            serpent._hp=serpent._hp - vie_perdu
            print(serpent.name + " a perdu "+ vie_perdu)

        else :
            if (self._sonette == False):
                print("tu n'as plus de sonette, tu passes ton tour !")
            else:
                print("Tu n'as plus de sang froid, recharge le !, tu passes ton tour")


    def set_sonette(sonette):
        self.sonette=sonette

    def has_sonnette:

        return sonette

    