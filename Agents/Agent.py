from GameValues.Values import *

class Agent:
    def __init__(self, startPos: tuple, direction, map, name, color):
        self.x = startPos[0]
        self.y = startPos[1]
        self.map = map
        self.name = name
        self.color = color
        self.cost = 0
        self.direction = direction
        
    def processDirection(self, direction: Direction):
        x, y = self.x, self.y
        if direction == Direction.Up:
            y = -1 if self.y == 0 else max(0, y-1)
        elif direction == Direction.Down:
            y = -1 if self.y >= len(self.map) - 1 else min(len(self.map) - 1, y + 1)
        elif direction == Direction.Left:
            x = -1 if self.x == 0 else max(0, x - 1)
        elif direction == Direction.Right:
            x = -1 if self.x >= len(self.map[0]) - 1 else min(len(self.map[0]) - 1, x+1)
        return x, y
        
    def senseTerrain(self, direction: Direction):
        senseX, senseY = self.processDirection(direction)

        if senseY == -1 or senseX == -1:
            return Terrain(0)
        return Terrain(self.map[senseY][senseX])
        
    def move(self, direction: Direction):
        moveX, moveY = self.processDirection(direction)
        terrain = self.senseTerrain(direction)
        
        if Passable.from_terrain(terrain):
            self.x, self.y = moveX, moveY
            self.cost += Costos.from_agent(self.name).from_terrain(terrain)
            return self.x, self.y
        else:
            print(f"{self.name}: No me puedo mover a ({moveX}, {moveY})")
            return False
    
    def turn_left(self):
        self.direction = Direction.turn_left(self.direction)

    def turn_right(self):
        self.direction = Direction.turn_right(self.direction)
        
    def forward(self):
        return self.move(self.direction)