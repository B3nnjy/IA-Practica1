import pygame
from Agents.Agent import Agent
from GameValues.Values import Direction
from enum import Enum

class AgentSprite(pygame.sprite.Sprite):
    def __init__(self, agent: Agent, width, height) -> None:
        super().__init__()
        self.agent = agent

        self.width = width
        self.height = height

        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        
    def draw(self):
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        
        if self.agent.direction == Direction.Up:
            arrow = [
                (self.width/2,   self.height/3*2),
                (self.width/4*3, self.height/4*3),
                (self.width/2,   self.height/4),
                (self.width/4,   self.height/4*3),
            ]
        elif self.agent.direction == Direction.Right:
            arrow = [
                (self.width/3,   self.height/2),
                (self.width/4,   self.height/4*3),
                (self.width/4*3, self.height/2),
                (self.width/4,   self.height/4)
            ]
        elif self.agent.direction == Direction.Down:
            arrow = [
                (self.width/2,   self.height/3),
                (self.width/4*3, self.height/4),
                (self.width/2,   self.height/4*3),
                (self.width/4,   self.height/4),
                ]
        elif self.agent.direction == Direction.Left:
            arrow = [
                (self.width/3*2, self.height/2),
                (self.width/4*3, self.height/4*3),
                (self.width/4,   self.height/2),
                (self.width/4*3, self.height/4)
            ]
        
        pygame.draw.polygon(self.image, self.agent.color, arrow)
        
    def update(self, *args, **kwargs) -> None:
        # print(self.agent.name)
        self.rect.topleft = (self.agent.x * self.width, self.agent.y * self.height)
        self.draw()
        return super().update(*args, **kwargs)