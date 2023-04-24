import pygame

from GameValues.Values import HumanoImg, MonoImg, PulpoImg, SqashImg


class MenuSprites(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface((80, 85))
        self.rect = self.image.get_rect()
        self.image.fill("white")

        self.fontColor = (0, 0, 0)

        self.SpriteHumano = HumanoImg.Down.value
        pass

    def draw(self):
        self.font = pygame.font.Font(None, 24)

        self.ImageHumano = pygame.image.load(self.SpriteHumano).convert_alpha()
        self.ImageHumano = pygame.transform.scale(self.ImageHumano, (80, 80))
        self.humanotxt = self.font.render("Humano", False, self.fontColor)
        pass

    def update(self):
        self.draw()
        self.rect.topleft = (10, 5)
        screen = pygame.display.get_surface()

        self.image.blit(self.ImageHumano, (0, 0))
        self.image.blit(self.humanotxt, (0, 85))