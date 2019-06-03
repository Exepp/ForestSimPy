from Plant import *

class SowThisle(Plant):
    ReproduceAttempts = 3

    def __init__(this, world):
        Plant.__init__(this, world, "9", 10)

    def tick(this):
        for i in range (SowThisle.ReproduceAttempts):
            Plant.tick(this)