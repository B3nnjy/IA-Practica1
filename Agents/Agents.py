from Agents.Agent import Agent
from GameValues.Values import *

class Agent1(Agent):
    def __init__(self, startPos, direction: Direction, map, tipo):
        super().__init__(startPos, direction, map, tipo, Color.Agente.value)
        self.direction = direction
    
    def turn(self):
        self.direction = Direction.turn_left(self.direction)
    
    def forward(self):
        self.move(self.direction)

class Agent2(Agent):
    def __init__(self, startPos, direction: Direction, map, tipo):
        super().__init__(startPos, direction, map, tipo, Color.Agente.value)
        self.direction = direction

class Agent3(Agent):
    def __init__(self, startPos, direction: Direction, map, tipo):
        super().__init__(startPos, direction, map, tipo, Color.Agente.value)

class Agent4(Agent):
    def __init__(self, startPos, direction: Direction, map, tipo):
        super().__init__(startPos, direction, map, tipo, Color.Agente.value)
    
    def moveRow(self, movement):
        if movement < 0:
            movement *= -1
            self.direction = Direction.Left
        else:
            self.direction = Direction.Right
        
        for i in range(movement):
            self.move(self.direction)
            
    def moveCol(self, movement):
        if movement < 0:
            movement *= -1
            self.direction = Direction.Down
        else:
            self.direction = Direction.Up
        
        for i in range(movement):
            if not self.move(self.direction):
                break

class Agent5(Agent):
    def __init__(self, startPos, direction: Direction, map, tipo):
        super().__init__(startPos, direction, map, tipo, Color.Agente.value)
    
    def move(self, movement, directions: tuple(Direction)):
        self.direction = directions[0]
        for i in range(movement):
            if not self.move(directions[0]):
                break
            if not self.move(directions[1]):
                break
