import pygame
from Animal import Animal
from Plant import Plant
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
from Vec2 import Vec2

ScreenSize = Vec2(1000, 800)
CellSize = 30
CellDist = CellSize + 5


class World:
    font = None

    def __init__(this, size):
        World.font = pygame.font.Font(None, 15)
        this.screen = pygame.display.set_mode((ScreenSize.x, ScreenSize.y))
        this.reset(size)

    def input(this):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                this.comments.clear()

            for eArr in this.entities:
                for ent in eArr:
                    if isinstance(ent, Human):
                        ent.onEvent(event)

            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_z):
                    this.save()
                elif(event.key == pygame.K_w):
                    this.load()
                else:
                    this.tick()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mPos = Vec2(event.pos[0], event.pos[1])

                animalClasses = Animal.__subclasses__()
                plantClasses = Plant.__subclasses__()

                for i in range(len(animalClasses)):
                    if pygame.Rect(i * CellDist, (this.size.y + 1) * CellDist, CellSize, CellSize).collidepoint(mPos.x, mPos.y):
                        this.chosenClass = animalClasses[i]
                        return False

                plStIdx = len(animalClasses)
                for i in range(plStIdx, plStIdx + len(plantClasses)):
                    if pygame.Rect(i * CellDist, (this.size.y + 1) * CellDist, CellSize, CellSize).collidepoint(mPos.x, mPos.y):
                        this.chosenClass = plantClasses[i - plStIdx]
                        return False

                for i in range(this.size.y):
                    for j in range(this.size.x):
                        idx = Vec2(j, i)
                        if pygame.Rect(j * CellDist, i * CellDist, CellSize, CellSize).collidepoint(mPos.x, mPos.y):
                            this.killEntity(idx)
                            this.spawnEntity(idx, this.chosenClass)



            return False

    def reset(this, size):
        global CellSize, CellDist
        CellSize = (ScreenSize.y - size.y * 5) / (size.y + 3)
        CellDist = CellSize + 5
        this.size = size
        this.entities = []
        this.comments = []
        this.chosenClass = None

        for i in range(size.y):
            this.entities.append([])
            for j in range(size.x):
                this.entities[i].append(None)
        return

    def spawnEntity(this, pos, c):
        if pos.x >= this.size.x or pos.y >= this.size.y or pos.x < 0 or pos.y < 0 or this.isOccupied(pos) or c is None:
            return False

        ent = c(this)
        ent.setPosition(pos)
        this.entities[pos.y][pos.x] = ent
        this.addComment("Organizm " + c.__name__ + " zostal stworzony")

        return True

    def killEntity(this, pos, c=None):
        if this.isOccupied(pos):
            if c is not None:
                this.addComment(
                    "Organizm " + type(this.entities[pos.y][pos.x]).__name__ + " zostaje zabity przez " + c.__name__)
            else:
                this.addComment("Organizm " + type(this.entities[pos.y][pos.x]).__name__ + " zostal zniszczony")
            this.entities[pos.y][pos.x] = None
            return True
        return False

    def swap(this, pos1, pos2):
        if pos1.y < this.size.y and pos2.y < this.size.y and pos1.x < this.size.x and pos2.x < this.size.x:
            pos1Cp = Vec2(pos1.x, pos1.y)
            pos2Cp = Vec2(pos2.x, pos2.y)

            if this.isOccupied(pos1Cp):
                this.entities[pos1Cp.y][pos1Cp.x].setPosition(pos2Cp)
            if this.isOccupied(pos2Cp):
                this.entities[pos2Cp.y][pos2Cp.x].setPosition(pos1Cp)

            temp = this.getEntityPtr(pos1Cp)
            this.entities[pos1Cp.y][pos1Cp.x] = this.getEntityPtr(pos2Cp)
            this.entities[pos2Cp.y][pos2Cp.x] = temp

    def tick(this):
        ordEntities = []
        for eArr in this.entities:
            for ePtr in eArr:
                if ePtr is not None:
                    ordEntities.append(ePtr)

        def sortByStr(e):
            return e.getStrength()

        ordEntities.sort(key=sortByStr, reverse=False)

        for ent in ordEntities:
            pos = ent.getPosition()
            if this.entities[pos.y][pos.x] is ent:
                ent.tick()
                ent.addAge()

    def draw(this):
        this.screen.fill((0, 0, 0))

        for y in range(len(this.entities)):
            for x in range(len(this.entities[y])):
                if this.entities[y][x] is not None:
                    pygame.draw.rect(this.screen, this.entities[y][x].getColor(), pygame.Rect(x * CellDist, y * CellDist, CellSize, CellSize))
                    text = World.font.render(this.entities[y][x].DisplayChar, True, (0, 0, 0))
                    this.screen.blit(text, (x * CellDist + CellDist / 2 - text.get_width(),
                                            y * CellDist + CellDist / 2 - text.get_height() / 2))
                else:
                    pygame.draw.rect(this.screen, (40, 40, 40),
                                     pygame.Rect(x * CellDist, y * CellDist, CellSize, CellSize))

        animalClasses = Animal.__subclasses__()
        plantClasses = Plant.__subclasses__()

        for i in range(len(animalClasses)):
            aClass = animalClasses[i]
            pygame.draw.rect(this.screen, aClass(this).getColor(), pygame.Rect(i * CellDist, (this.size.y + 1) * CellDist, CellSize, CellSize))
            text = World.font.render(aClass(this).DisplayChar, True, (0, 0, 0))
            this.screen.blit(text, (i * CellDist + CellDist / 2 - text.get_width(), (this.size.y + 1) * CellDist + CellDist / 2 - text.get_height() / 2))

        plStIdx = len(animalClasses)
        for i in range(plStIdx, plStIdx + len(plantClasses)):
            aClass = plantClasses[i - plStIdx]
            pygame.draw.rect(this.screen, aClass(this).getColor(), pygame.Rect(i * CellDist, (this.size.y + 1) * CellDist, CellSize, CellSize))
            text = World.font.render(aClass(this).DisplayChar, True, (0, 0, 0))
            this.screen.blit(text, (i * CellDist + CellDist / 2 - text.get_width(), (this.size.y + 1) * CellDist + CellDist / 2 - text.get_height() / 2))

        for i in range(len(this.comments)):
            text = World.font.render(this.comments[i] + ".", True, (255, 255, 255))
            this.screen.blit(text, ((this.size.x + 1) * CellDist , i * 10))

        pygame.display.flip()

    def save(this):
        file = open("save", "w")
        file.write("%d\n" % this.size.x)
        file.write("%d\n" % this.size.y)
        for eArr in this.entities:
            for ent in eArr:
                if ent is not None:
                    ent.save(file)
        file.close()

    def load(this):
        file = open("save", "r")
        this.size.x = int(file.readline())
        this.size.y = int(file.readline())
        this.reset(this.size)
        while True:
            className = file.readline()
            if className == "":
                return
            className.rstrip('\n')
            print()
            x = int(file.readline())
            y = int(file.readline())
            this.spawnEntity(Vec2(x, y), globals()[className.split("\n")[0]])
            entity = this.getEntityPtr((Vec2(x, y)))
            entity.load(file)

        file.close()

    def addComment(this, comment):
        this.comments.insert(0, comment)

    def getEntityPtr(this, pos):
        return this.entities[pos.y][pos.x]

    def isOccupied(this, pos):
        return (this.getEntityPtr(pos) is not None)

    def getSize(this):
        return this.size
