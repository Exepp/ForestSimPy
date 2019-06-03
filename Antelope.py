from Animal import *


class Antelope(Animal):
    def __init__(this, world):
        Animal.__init__(this, world, "A")
        this.initiative = 4
        this.str = 4

    def tick(this):
        freeIdx = []
        minI = Vec2(max(0, this.pos.x - Antelope.MaxMoveDist), max(0, this.pos.y - Antelope.MaxMoveDist))
        maxI = Vec2(min(this.world.getSize().x - 1, this.pos.x + Antelope.MaxMoveDist),
                    min(this.world.getSize().y - 1, this.pos.y + Antelope.MaxMoveDist))

        for i in range(minI.x, maxI.x + 1):
            mPos = Vec2(i, this.pos.y)
            if mPos != this.pos:
                freeIdx.append(mPos)

        for i in range(minI.y, maxI.y + 1):
            mPos = Vec2(this.pos.x, i)
            if mPos != this.pos:
                freeIdx.append(mPos)

        if (len(freeIdx) != 0):
            n = random.randint(0, len(freeIdx) - 1)
            this.attack(freeIdx[n])

    def defendFrom(this, entity):
        return (random.randint(1, 100) <= Antelope.ChanceToRun)

    ChanceToRun = 50
    MaxMoveDist = 2
