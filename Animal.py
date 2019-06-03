import random

from Entity import Entity
from Vec2 import Vec2


class Animal(Entity):

    def __init__(this, world, displayChar):
        Entity.__init__(this, world, displayChar)

    def tick(this):

        freeIdx = []
        if (this.pos.x - 1 >= 0):
            freeIdx.append(Vec2(this.pos.x - 1, this.pos.y))
        if (this.pos.x + 1 < this.world.getSize().x):
            freeIdx.append(Vec2(this.pos.x + 1, this.pos.y))
        if (this.pos.y - 1 >= 0):
            freeIdx.append(Vec2(this.pos.x, this.pos.y - 1))
        if (this.pos.y + 1 < this.world.getSize().y):
            freeIdx.append(Vec2(this.pos.x, this.pos.y + 1))

        n = random.randint(0, len(freeIdx) - 1)
        this.attack(freeIdx[n])

    def attack(this, pos2):
        ePtr = this.world.getEntityPtr(pos2)
        if (ePtr != None):
            if (this.reproduced(ePtr) or ePtr.defendFrom(this)):
                return
            elif (this.str < ePtr.getStrength()):
                this.world.killEntity(this.pos, type(ePtr))
                return
            else:
                this.world.killEntity(pos2, type(this))
        this.world.swap(this.pos, pos2)

    def reproduced(this, other):
        pos2 = other.getPosition()
        if other.DisplayChar == this.DisplayChar:
            posMin = Vec2(min(this.pos.x, pos2.x), min(this.pos.y, pos2.y))
            posMax = Vec2(max(this.pos.x, pos2.x), max(this.pos.y, pos2.y))
            rmin = Vec2(max(0, posMin.x - 1), max(0, posMin.y - 1))
            rmax = Vec2(min(this.world.getSize().x - 1, posMax.x + 1),
                        min(this.world.getSize().y - 1, posMax.y + 1))

            for i in range(rmin.y, rmax.y + 1):
                for j in range(rmin.x, rmax.x + 1):
                    if this.world.spawnEntity(Vec2(j, i), type(this)):
                        return True
            return True
        return False
