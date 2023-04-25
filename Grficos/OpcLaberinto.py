import platform
import subprocess

import pygame
import ctypes
from GameValues.Values import *
from Agents.Agents import *
from Agents.AgentSprite import AgentSprite

S_WIDTH = 800
S_HEIGHT = 600


class OpcLaberinto:
    def __init__(self, map):
        self.map = map
        self.cellWidth = S_WIDTH / len(self.map[0])
        self.cellHeight = S_HEIGHT / len(self.map)

        pygame.init()
        return

    def runGame(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        pygame.display.set_caption("Configuracion del mapa")
        self.screen.fill("black")
        self.drawMap()
        self.clock.tick(60)

        running = True
        dragging = False

        while (running):
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pressed()
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    x = int(mouseX / self.cellWidth)
                    y = int(mouseY / self.cellHeight)

                    # click izquierdo
                    if mouse[0]:
                        startX = x
                        startY = y

                        # Activar el arrastre
                        dragging = True
                        value = 0 if self.map[startY][startX] == 1 else 1
                    # click de rueda
                    elif mouse[1]:
                        # Ciclar tipo de celda
                        self.map[y][x] = (self.map[y][x] + 1) % len(Terrain)
                        pass
                    elif mouse[2]:
                        cell = self.map[y][x]

                        # Mostrar información sobre la celda
                        if platform.system() == 'Windows':
                            ctypes.windll.user32.MessageBoxW(0, Terrain(cell).name, "Celda", 0)
                        elif platform.system() == 'Linux':
                            subprocess.call(['notify-send', 'Celda', Terrain(cell).name])
                        pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragging:
                        # Encontrar coordenadas de la celda final
                        (mouseX, mouseY) = pygame.mouse.get_pos()
                        endX = int(mouseX / self.cellWidth)
                        endY = int(mouseY / self.cellHeight)

                        pathX = (min(startX, endX), max(startX, endX) + 1)
                        pathY = (min(startY, endY), max(startY, endY) + 1)

                        # Invertir las celdas
                        for i in range(pathY[0], pathY[1]):
                            for j in range(pathX[0], pathX[1]):
                                self.map[i][j] = value

                        # Volver a dibujar el mapa
                        dragging = False
                        pass
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:

                        contI = 0
                        contF = 0
                        for i in range(len(self.map)):
                            for j in range(len(self.map[i])):
                                if self.map[i][j] == Terrain.Inicio.value:
                                    contI += 1
                                if self.map[i][j] == Terrain.Fin.value:
                                    contF += 1

                        if contI > 1 or contF > 1:
                            if contI > 1:
                                print("Existen multiples inicios", contI)
                                pass
                            if contF > 1:
                                print("Existen multiples finales", contF)
                                pass
                            continue

                        running = False
                        pass
                elif event.type == pygame.QUIT:
                    running = False
            self.drawMap()

        pygame.quit()
        return self.map

    def drawMap(self):
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

        pygame.display.flip()