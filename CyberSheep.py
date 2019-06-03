from Animal import *
import Hogweed

class CyberSheep(Animal):
    def __init__(this, world):
        Animal.__init__(this, world, "@")
        this.initiative = 4
        this.str = 11

    def tick(this):

        minDist = float("inf")
        minDistIdxs = Vec2(0,0)

        for eArr in this.world.entities:
            for ent in eArr:
                if isinstance(ent, Hogweed.Hogweed):
                    dist = ((ent.pos.x - this.pos.x) ** 2 + (ent.pos.y - this.pos.y) ** 2) ** 0.5
                    if(dist < minDist):
                        minDist = dist
                        minDistIdxs = Vec2(ent.pos.x, ent.pos.y)

        if minDist == float("inf"):
            return Animal.tick(this)

        dir = Vec2(minDistIdxs.x - this.pos.x, minDistIdxs.y - this.pos.y )
        if abs(dir.x) > abs(dir.y):
            dir = Vec2(dir.x / abs(dir.x), 0)
        else:
            dir = Vec2(0, dir.y / abs(dir.y))

        this.attack(Vec2(this.pos.x + int(dir.x), this.pos.y + int(dir.y)))



