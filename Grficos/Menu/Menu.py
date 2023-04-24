import pygame

from Grficos.Menu.MenuSprites import CharacterP, CharacterH, CharacterM, CharacterS


class Menu():
    def runMenu(self):
        self.spriteList = pygame.sprite.Group()
        self.sprites = [CharacterH(), CharacterM(), CharacterP(), CharacterS()]
        self.spriteList.add(self.sprites)

        pygame.init()
        pygame.font.init()

        self.font = pygame.font.Font(None, 30)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((400, 150))
        self.screen.fill("white")
        self.title = self.font.render("Choose a character", False, (0, 0, 0))

        self.clock.tick(60)

        running = True

        while (running):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()
                    if self.sprites[0].rect.collidepoint(mousepos):
                        self.agent = "Humano"
                        running = False
                    elif self.sprites[1].rect.collidepoint(mousepos):
                        self.agent = "Mono"
                        running = False
                    elif self.sprites[2].rect.collidepoint(mousepos):
                        self.agent = "Pulpo"
                        running = False
                    elif self.sprites[3].rect.collidepoint(mousepos):
                        self.agent = "Sasquatch"
                        running = False
                elif event.type == pygame.QUIT:
                    running = False

            self.spriteList.update()
            self.spriteList.draw(self.screen)
            self.screen.blit(self.title, (100, 130))
            pygame.display.flip()
        pygame.quit()
        return self.agent
