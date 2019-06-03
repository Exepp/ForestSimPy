from Plant import *


class Belladona(Plant):
    def __init__(this, world):
        Plant.__init__(this, world, "B", 10)
        this.str = 99

    def defendFrom(this, entity):
        this.world.killEntity(entity.getPosition(), type(this))
        return False
