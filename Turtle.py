from Animal import *


class Turtle(Animal):
    Defence = 4
    MoveChance = 75

    def __init__(this, world):
        Animal.__init__(this, world, "T")
        this.initiative = 1
        this.str = 2

    def tick(this):
        if random.randint(1, 100) <= Turtle.MoveChance:
            Animal.tick(this)

    def defendFrom(this, entity):
        return (entity.getStrength() <= Turtle.Defence)
