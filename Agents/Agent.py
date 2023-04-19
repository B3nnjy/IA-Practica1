from GameValues.Values import *

class Agent:
    def __init__(self, startPos, map, name, color):
        self.x = startPos[0]
        self.y = startPos[1]
        self.map = map
        self.name = name
        self.color = color
        self.cost = 0
        
    def processDirection(self, direction: Direction):
        x, y = self.x, self.y
        if direction == Direction.Up:
            y = max(0, y-1)
        elif direction == Direction.Down:
            y = min(len(self.map), y+1)
        elif direction == Direction.Left:
            x = max(0, x-1)
        elif direction == Direction.Right:
            x = min(len(self.map[0]), x+1)
        return (x, y)
        
    def senseTerrain(self, direction: Direction):
        senseX, senseY = self.processDirection(direction)
        return Terrain(self.map[senseY, senseX])
        
    def move(self, direction: Direction):
        moveX, moveY = self.processDirection(direction)
        terrain = self.senseTerrain(direction)
        
        if Passable.from_terreno(terrain):
            self.x, self.y = moveX, moveY
            self.cost += Cost.from_terreno(terrain)
            return True
        else:
            print(f"{self.name}: No me puedo mover a ({moveX}, {moveY})")
            return False