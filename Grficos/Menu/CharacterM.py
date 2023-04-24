import pygame

from GameValues.Values import HumanoImg, MonoImg, PulpoImg, SqashImg


class MenuSprites(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

        self.image = pygame.Surface((390, 100))
        self.rect = self.image.get_rect()
        self.image.fill("white")

        self.fontColor = (0, 0, 0)

        self.SpriteMono = MonoImg.Down.value
        pass

    def draw(self):
        self.font = pygame.font.Font(None, 24)

        self.ImageMono = pygame.image.load(self.SpriteMono).convert_alpha()
        self.ImageMono = pygame.transform.scale(self.ImageMono, (80, 80))
        self.monotxt = self.font.render("Mono", False, self.fontColor)
        pass

    def update(self):
        self.draw()
        self.rect.topleft = (10, 5)
        screen = pygame.display.get_surface()

        self.image.blit(self.ImageMono, (100, 0))
        self.image.blit(self.monotxt, (110, 85))

        screen.blit()