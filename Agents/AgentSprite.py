import pygame
from Agents.Agent import Agent
from GameValues.Values import Direction, AgentImag
from enum import Enum


class AgentSprite(pygame.sprite.Sprite):

    def __init__(self, agent: Agent, width, height) -> None:
        super().__init__()
        self.rect = None
        self.image = None
        self.agent = agent

        self.width = width
        self.height = height

        self.surface = pygame.Surface([width, height])
        self.surface.fill((0, 0, 0))
        self.surface.set_colorkey((0, 0, 0))

    def draw(self):
        imageAgent = None

        if self.agent.direction == Direction.Up:
            imageAgent = AgentImag.for_agent(self.agent.name).Up.value
        elif self.agent.direction == Direction.Right:
            imageAgent = AgentImag.for_agent(self.agent.name).Right.value
        elif self.agent.direction == Direction.Down:
            imageAgent = AgentImag.for_agent(self.agent.name).Down.value
        elif self.agent.direction == Direction.Left:
            imageAgent = AgentImag.for_agent(self.agent.name).Left.value

        self.image = pygame.image.load(imageAgent).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        pass

    def update(self):
        self.draw()

        self.rect.topleft = (self.agent.x * self.width, self.agent.y * self.height)
        screen = pygame.display.get_surface()
        screen.blit(self.image, self.rect)
        pass
