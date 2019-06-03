import random

from Entity import Entity
from Vec2 import Vec2


class Plant(Entity):
    def __init__(this, world, displayChar, reproduceChance):
        Entity.__init__(this, world, displayChar)
        this.initiative = this.str = 0
        this.ReproduceChance = reproduceChance

    def tick(this):
        freeIdx = []
        minI = Vec2(max(0, this.pos.x - 1), max(0, this.pos.y - 1))
        maxI = Vec2(min(this.world.getSize().x - 1, this.pos.x + 1), min(this.world.getSize().y - 1, this.pos.y + 1))

        for i in range(minI.x, maxI.x + 1):
            mPos = Vec2(i, this.pos.y)
            if mPos != this.pos and not this.world.isOccupied(mPos):
                freeIdx.append(mPos)

        for i in range(minI.y, maxI.y + 1):
            mPos = Vec2(this.pos.x, i)
            if mPos != this.pos and not this.world.isOccupied(mPos):
                freeIdx.append(mPos)

        if (len(freeIdx) != 0):
            n = random.randint(0, len(freeIdx) - 1)
            this.attack(freeIdx[n])

    def attack(this, pos2):
        if (random.randint(1, 100) <= this.ReproduceChance):
            this.world.spawnEntity(pos2, type(this))