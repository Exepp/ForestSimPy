from Plant import *


class Grass(Plant):
    def __init__(this, world):
        Plant.__init__(this, world, "v", 10)
