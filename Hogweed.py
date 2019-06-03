from Plant import *
from Animal import *
import CyberSheep

class Hogweed(Plant):

    def __init__(this, world):
        Plant.__init__(this, world, "#", 10)
        this.str = 10

    def tick(this):
        minI = Vec2(max(0, this.pos.x - 1), max(0, this.pos.y - 1))
        maxI = Vec2(min(this.world.getSize().x - 1, this.pos.x + 1), min(this.world.getSize().y - 1, this.pos.y + 1))

        for i in range(minI.x, maxI.x + 1):
            mPos = Vec2(i, this.pos.y)
            if mPos != this.pos and this.world.isOccupied(mPos) and isinstance(this.world.getEntityPtr(mPos), Animal) and not isinstance(this.world.getEntityPtr(mPos), CyberSheep.CyberSheep):
                this.world.killEntity(mPos, type(this))
        for i in range(minI.y, maxI.y + 1):
            mPos = Vec2(this.pos.x, i)
            if mPos != this.pos and this.world.isOccupied(mPos) and isinstance(this.world.getEntityPtr(mPos), Animal) and not isinstance(this.world.getEntityPtr(mPos), CyberSheep.CyberSheep):
                this.world.killEntity(mPos, type(this))
        Plant.tick(this)


    def defendFrom(this, entity):
        if not isinstance(entity, CyberSheep.CyberSheep):
            this.world.killEntity(entity.getPosition(), type(this))
        return False