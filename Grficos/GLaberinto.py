import pygame

def InitGraf(columnas, filas, matriz):
    width = 800/columnas
    height = 600/filas

    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    screen.fill("black")

    X = Y = 0
    n = m = 0
    for i in range(filas):
        while True:
            if matriz[n][m] == 1:
                color = (204, 188, 161)
            else:
                color = (46, 30, 49)

            pygame.draw.rect(screen, color, (X, Y, width, height))
            pygame.draw.rect(screen, (97, 42, 82), (X, Y, width, height), 1)

            X += width
            m += 1

            if m >= columnas:
                X = 0
                m = 0
                break

        Y += height
        n += 1

    pygame.display.flip()
    clock.tick(60)

    running = True

    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    return
