import pygame
import tkinter
from tkinter import messagebox
import GameValues.Values as GV

S_WIDTH = 800
S_HEIGHT = 600

class Laberinto:

    def __init__(self, matriz):
        self.matriz = matriz
        pygame.init()
        return
    
    def runGame(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
        self.screen.fill("black")
        
        self.drawMap()
        
        self.clock.tick(60)
        
        running = True
        dragging = False

        while(running):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pressed()
                    
                    # click izquierdo
                    if mouse[0]:
                        # Encontrar coordenadas de la celda inicial
                        (mouseX, mouseY) = pygame.mouse.get_pos()
                        startX = int(mouseX/self.cellWidth)
                        startY = int(mouseY/self.cellHeight)
                        
                        # Activar el arrastre
                        dragging = True
                        value = 0 if self.matriz[startY][startX] == 1 else 1
                    # click de rueda
                    elif mouse[1]:
                        pass
                    # click derecho
                    elif mouse[2]:
                        # Encontrar coordenadas de la celda correcta
                        (mouseX, mouseY) = pygame.mouse.get_pos()
                        x = int(mouseX/self.cellWidth)
                        y = int(mouseY/self.cellHeight)
                        cell = self.matriz[y][x]
                        
                        # Mostrar información sobre la celda
                        tkinter.Tk().wm_withdraw() #to hide the main window
                        messagebox.showinfo("Celda", "Pared" if cell == 0 else "Piso")
                        pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragging:
                        # Encontrar coordenadas de la celda final
                        (mouseX, mouseY) = pygame.mouse.get_pos()
                        endX = int(mouseX/self.cellWidth)
                        endY = int(mouseY/self.cellHeight)

                        pathX = (min(startX, endX), max(startX, endX)+1)
                        pathY = (min(startY, endY), max(startY, endY)+1)


                        # Invertir las celdas
                        for i in range(pathY[0], pathY[1]):
                            for j in range(pathX[0], pathX[1]):
                                self.matriz[i][j] = value
                        
                        # Volver a dibujar el mapa
                        self.drawMap()
                        pass
                        
                elif event.type == pygame.QUIT:
                    running = False

        pygame.quit()
        return

    def drawMap(self):
        columnas = len(self.matriz[0])
        filas = len(self.matriz)
        terreno = [item.value for item in GV.Terreno] 
        
        self.cellWidth = S_WIDTH/columnas
        self.cellHeight = S_HEIGHT/filas
        
        X = Y = 0
        for i in range(filas):
            for j in range(columnas):
                
                if self.matriz[i][j] in terreno:
                    color = GV.Colores.from_terreno(GV.Terreno(self.matriz[i][j]))
                else:
                    print("ERROR! Celda no reconocida")
                    color = GV.Colores.Error.value

                pygame.draw.rect(self.screen, color, (X, Y, self.cellWidth, self.cellHeight))
                pygame.draw.rect(self.screen, GV.Colores.Borde.value, (X, Y, self.cellWidth, self.cellHeight), 1)

                X += self.cellWidth
            X = 0
            Y += self.cellHeight
        
        pygame.display.flip()