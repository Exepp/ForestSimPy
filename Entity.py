import pygame
from Vec2 import Vec2
import pickle


class Entity:
    def __init__(this, world, displayChar):
        this.DisplayChar = displayChar
        this.world = world
        this.pos = Vec2(0, 0)
        this.initiative = 0
        this.age = 0
        this.str = 0

    def defendFrom(this, entity):
        return False

    def save(this, file):
        file.write(type(this).__name__ + "\n")
        file.write("%d\n" % this.pos.x)
        file.write("%d\n" % this.pos.y)
        file.write("%d\n" % this.age)
        file.write("%d\n" % this.str)

    def load(this, file):
        this.age = int(file.readline())
        this.str = int(file.readline())


    def getColor(this):
        g = abs(hash(("Green" + type(this).__name__ + this.DisplayChar))) % 255
        r = abs(hash(("Red" + type(this).__name__ + this.DisplayChar))) % 255
        b = abs(hash(("Blue" + type(this).__name__ + this.DisplayChar))) % 255
        return pygame.Color(r, g, b)

    def setPosition(this, pos):
        this.pos = Vec2(pos.x, pos.y)

    def setStrength(this, str):
        this.str = str

    def addAge(this):
        this.age += 1

    def getPosition(this):
        return this.pos

    def getInitiative(this):
        return this.initiative

    def getStrength(this):
        return this.str

    def getAge(this):
        return this.age
