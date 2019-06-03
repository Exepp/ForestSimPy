from Animal import *


class Sheep(Animal):
    def __init__(this, world):
        Animal.__init__(this, world, "S")
        this.initiative = 4
        this.str = 4
