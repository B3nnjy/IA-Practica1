import platform
import subprocess

import pygame
import ctypes
from GameValues.Values import *
from Agents.Agents import *
from Agents.AgentSprite import AgentSprite

S_WIDTH = 800
S_HEIGHT = 600


class Laberinto:
    def __init__(self, map, nombre):
        self.nombre = nombre
        self.map = map
        self.cellWidth = S_WIDTH / len(self.map[0])
        self.cellHeight = S_HEIGHT / len(self.map)
        self.spriteList = pygame.sprite.Group()

        start = self.findStart()
        self.end = self.findEnd()

        self.agents = [
            AgentSprite(
                Agent3(
                    start,
                    Direction.Right,
                    map,
                    self.nombre
                ),
                self.cellWidth,
                self.cellHeight
            )
        ]

        self.spriteList.add(self.agents)

        pygame.init()
        return

    def findStart(self):
        columnas = len(self.map[0])
        filas = len(self.map)
        for i in range(filas):
            for j in range(columnas):
                if self.map[i][j] == Terrain.Inicio.value:
                    return (j, i)

    def findEnd(self):
        columnas = len(self.map[0])
        filas = len(self.map)
        for i in range(filas):
            for j in range(columnas):
                if self.map[i][j] == Terrain.Fin.value:
                    return (j, i)

    def runGame(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        self.screen.fill("black")
        pygame.display.set_caption("Laberinto game")
        self.drawMap()
        self.clock.tick(60)

        running = True
        move = True

        while (running):
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pressed()
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    x = int(mouseX / self.cellWidth)
                    y = int(mouseY / self.cellHeight)

                    # click derecho
                    if mouse[2]:
                        cell = self.map[y][x]

                        # Mostrar información sobre la celda
                        if platform.system() == 'Windows':
                            ctypes.windll.user32.MessageBoxW(0, Terrain(cell).name, "Celda", 0)
                        elif platform.system() == 'Linux':
                            subprocess.call(['notify-send', 'Celda', Terrain(cell).name])
                        pass
                elif event.type == pygame.KEYDOWN:
                    if move:
                        if event.key == pygame.K_LEFT:
                            self.agents[0].agent.turn_left()
                        elif event.key == pygame.K_RIGHT:
                            self.agents[0].agent.turn_right()
                        elif event.key == pygame.K_UP:
                            self.agents[0].agent.forward()
                            pass
                    elif event.key == pygame.K_RETURN:
                        running = False
                        pass

                    if self.agents[0].agent.x == self.end[0] and self.agents[0].agent.y == self.end[1]:
                        pygame.event.clear(pygame.KEYDOWN)
                        move = False
                        pass
                elif event.type == pygame.QUIT:
                    running = False
            self.drawMap(move)

        pygame.quit()
        return

    def drawMap(self, move=True):
        columnas = len(self.map[0])
        filas = len(self.map)
        terreno = [item.value for item in Terrain]

        X = Y = 0
        for i in range(filas):
            for j in range(columnas):
                if self.map[i][j] in terreno:
                    color = Color.from_terrain(Terrain(self.map[i][j]))
                else:
                    print("ERROR! Celda no reconocida")
                    color = Color.Error.value

                pygame.draw.rect(self.screen, color, (X, Y, self.cellWidth, self.cellHeight))
                pygame.draw.rect(self.screen, Color.Borde.value, (X, Y, self.cellWidth, self.cellHeight), 1)

                X += self.cellWidth
            X = 0
            Y += self.cellHeight

        self.spriteList.update()
        self.spriteList.draw(self.screen)
        if not move:
            self.TheEnd()
        pygame.display.flip()

    def TheEnd(self):
        font = pygame.font.Font(None, 50)

        txt = font.render("Has llegado al final!!", True, (100, 100, 100))
        txtC = font.render(f"Costo: {self.agents[0].agent.cost}", True, (100,100,100))
        self.screen.blit(txt, (200, 200))
        self.screen.blit(txtC, (300, 240))
        pygame.display.flip()
