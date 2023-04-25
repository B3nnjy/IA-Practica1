import pygame

from GameValues.Values import HumanoImg, MonoImg, PulpoImg, SqashImg


class Character(pygame.sprite.Sprite):
    def __init__(self, Sprite, Name, pos: tuple[int, int]) -> None:
        super().__init__()
        self.font = None
        self.pos = pos
        self.Sprite = Sprite
        self.Name = Name
        self.image = pygame.Surface((85, 100))
        self.rect = self.image.get_rect()
        self.image.fill("white")
        self.fontColor = (0, 0, 0)
        pass

    def draw(self):
        self.font = pygame.font.Font(None, 24)

        self.Image = pygame.image.load(self.Sprite).convert_alpha()
        self.Image = pygame.transform.scale(self.Image, (80, 80))
        self.txt = self.font.render(self.Name, False, self.fontColor)
        pass

    def update(self):
        self.draw()
        self.rect.topleft = (self.pos[0], self.pos[1])
        screen = pygame.display.get_surface()

        self.image.blit(self.Image, (0, 0))
        self.image.blit(self.txt, (0, 85))

        screen.blit(self.image, self.rect)
        pass


class CharacterH(Character):
    def __init__(self) -> None:
        super().__init__(HumanoImg.Down.value, "Humano", (10, 5))
        pass


class CharacterM(Character):
    def __init__(self) -> None:
        super().__init__(MonoImg.Down.value, "Mono", (100, 5))
        pass


class CharacterP(Character):
    def __init__(self):
        super().__init__(PulpoImg.Down.value, "Pulpo", (200, 5))
        pass


class CharacterS(Character):
    def __init__(self):
        super().__init__(SqashImg.Down.value, "Sastquash", (300, 5))
        pass
