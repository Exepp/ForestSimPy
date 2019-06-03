from Animal import *


class Wolf(Animal):
    def __init__(this, world):
        Animal.__init__(this, world, "W")
        this.initiative = 5
        this.str = 7
