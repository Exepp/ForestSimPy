import pygame
from Antelope import Antelope
from Belladona import Belladona
from Fox import Fox
from Grass import Grass
from Guarana import Guarana
from Human import Human
from Sheep import Sheep
from SowThisle import SowThisle
from Turtle import Turtle
from Wolf import Wolf
from CyberSheep import CyberSheep
from Hogweed import Hogweed
from World import World
from Vec2 import Vec2

pygame.init()

clock = pygame.time.Clock()

world = World(Vec2(10, 10))
world.spawnEntity(Vec2(0, 0), Human);
world.spawnEntity(Vec2(10, 10), Wolf);
world.spawnEntity(Vec2(10, 11), Wolf);
world.spawnEntity(Vec2(2, 2), Sheep);
world.spawnEntity(Vec2(2, 3), Sheep);
world.spawnEntity(Vec2(19, 7), Fox);
world.spawnEntity(Vec2(18, 6), Fox);
world.spawnEntity(Vec2(6, 19), Turtle);
world.spawnEntity(Vec2(7, 18), Turtle);
world.spawnEntity(Vec2(13, 19), Antelope);
world.spawnEntity(Vec2(14, 18), Antelope);
world.spawnEntity(Vec2(19, 2), Belladona);
world.spawnEntity(Vec2(18, 3), Grass);
world.spawnEntity(Vec2(2, 19), Guarana);
world.spawnEntity(Vec2(3, 18), Hogweed);
world.spawnEntity(Vec2(18, 19), SowThisle);
world.spawnEntity(Vec2(18, 0), CyberSheep);

while not world.input():
    world.draw()
    clock.tick(60)