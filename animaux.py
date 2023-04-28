class Animaux:

    def __init__(self, name, type,tete, force, defence, hp, chance_crit,endurance):
        self._name = name
        self._tete = tete
        self._force = force
        self._defence = defence
        self._hp = hp
        self._mort = False
        self._chance_crit = chance_crit
        self._endurance = endurance

    def attaque_basique(animal):
        print("shlaaa ca decoupe")
        vie_perdu=(self._force - animal._defence)*(animal._defence//100)
        animal._hp=animal._hp - vie_perdu
        print(animal.name + " a perdu "+ vie_perdu)


    def set_chance_crit():
        self._chance_crit

    def set_tete(tete_state):
        self.tete=tete_state

    def has_tete():
        return self._tete

    def get_name():
        return self._name

    def get_force():
        return self._force

    def get_defence():
        return self._defence

    def get_hp():
        return self._hp

    def set_mort(mort):
            self._mort = mort

    def isMort():
        return self._mort
