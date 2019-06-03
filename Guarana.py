from Plant import *


class Guarana(Plant):
    StrBoost = 3

    def __init__(this, world):
        Plant.__init__(this, world, "G", 10)

    def defendFrom(this, entity):
        entity.setStrength(entity.getStrength() + Guarana.StrBoost)
        return False
