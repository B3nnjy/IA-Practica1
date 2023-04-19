from Agents.Agent import Agent
from GameValues.Values import *

class Agent1(Agent):
    def __init__(self, startPos, matriz, direction: Direction):
        super.__init__(self, startPos, matriz, "Agente 1", Color.Agente)
        self.direction = direction
    
    def turn(self):
        self.direction = Direction.turn_left(self.direction)
    
    def forward(self):
        self.move(self.direction)

class Agent2(Agent):
    def __init__(self, startPos, matriz, direction: Direction):
        super.__init__(self, startPos, matriz, "Agente 2", Color.Agente)
        self.direction = direction
    
    def turn_left(self):
        self.direction = Direction.turn_left(self.direction)

    def turn_right(self):
        self.direction = Direction.turn_right(self.direction)
        
    def forward(self):
        self.move(self.direction)

class Agent3(Agent):
    def __init__(self, startPos, matriz):
        super.__init__(self, startPos, matriz, "Agente 3", Color.Agente)

class Agent4(Agent):
    def __init__(self, startPos, matriz):
        super.__init__(self, startPos, matriz, "Agente 4", Color.Agente)
    
    def moveRow(self, movement):
        if movement < 0:
            movement *= -1
            direction = Direction.Left
        else:
            direction = Direction.Right
        
        for i in range(movement):
            self.move(direction)
            
    def moveCol(self, movement):
        if movement < 0:
            movement *= -1
            direction = Direction.Down
        else:
            direction = Direction.Up
        
        for i in range(movement):
            if not self.move(direction):
                break

class Agent5(Agent):
    def __init__(self, startPos, matriz):
        super.__init__(self, startPos, matriz, "Agente 5", Color.Agente)
    
    def move(self, movement, directions: tuple(Direction)):
        for i in range(movement):
            if not self.move(directions[0]):
                break
            if not self.move(directions[1]):
                break
