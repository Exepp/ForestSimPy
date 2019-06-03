from Animal import *


class Fox(Animal):
    def __init__(this, world):
        Animal.__init__(this, world, "F")
        this.initiative = 7
        this.str = 3

    def tick(this):
        freeIdx = []
        minI = Vec2(max(0, this.pos.x - 1), max(0, this.pos.y - 1))
        maxI = Vec2(min(this.world.getSize().x - 1, this.pos.x + 1), min(this.world.getSize().y - 1, this.pos.y + 1))

        for i in range(minI.x, maxI.x + 1):
            mPos = Vec2(i, this.pos.y)
            if (mPos != this.pos and (not this.world.isOccupied(mPos) or (this.world.getEntityPtr(
                    mPos).getStrength() <= this.str or this.DisplayChar == this.world.getEntityPtr(mPos).DisplayChar))):
                freeIdx.append(mPos)

        for i in range(minI.y, maxI.y + 1):
            mPos = Vec2(this.pos.x, i)
            if (mPos != this.pos and (not this.world.isOccupied(mPos) or (this.world.getEntityPtr(
                    mPos).getStrength() <= this.str or this.DisplayChar == this.world.getEntityPtr(mPos).DisplayChar))):
                freeIdx.append(mPos)

        if (len(freeIdx) != 0):
            n = random.randint(0, len(freeIdx) - 1)
            this.attack(freeIdx[n])
