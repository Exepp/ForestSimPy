import pygame
from Animal import *


class Human(Animal):
    DefaultStr = 5
    AbilityExh = 5
    AbilityPowerUp = 5

    def __init__(this, world):
        Animal.__init__(this, world, "H")
        this.initiative = 4
        this.str = Human.DefaultStr
        this.powerUp = -Human.AbilityExh
        this.nextTickDirection = Vec2(0, 0)

    def tick(this):
        if this.powerUp > -Human.AbilityExh:
            this.powerUp -= 1
        if (this.powerUp >= 0):
            this.str = Human.DefaultStr + this.powerUp

        if this.nextTickDirection != Vec2(0, 0):
            nextPos = Vec2(this.pos.x + this.nextTickDirection.x, this.pos.y + this.nextTickDirection.y)
            if (
                    nextPos.x >= 0 and nextPos.x < this.world.getSize().x and nextPos.y >= 0 and nextPos.y < this.world.getSize().y):
                this.attack(nextPos)
            this.nextTickDirection = Vec2(0, 0)

    def onEvent(this, event):
        if event.type != pygame.KEYDOWN:
            return

        code = event.key
        DirVec = [Vec2(0, -1), Vec2(0, 1), Vec2(1, 0), Vec2(-1, 0)]
        if code >= 273 and code <= 276:
            this.nextTickDirection = DirVec[code - 273]
        elif code == 115:
            if (this.powerUp <= -Human.AbilityExh):
                this.powerUp = Human.AbilityPowerUp
                this.world.addComment("Czlowiek uzyl specjalnej umiejetnosci!")

    def save(this, file):
        Animal.save(this, file)
        file.write("%d\n" % this.powerUp)

    def load(this, file):
        Animal.load(this, file)
        this.powerUp = int(file.readline())