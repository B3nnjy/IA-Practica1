from enum import Enum

class Terrain(Enum):
    Pared = 0
    Piso = 1
    Inicio = 2
    Fin = 3

class Color(Enum):
    Pared = (46, 30, 49)
    Piso = (204, 188, 161)
    Inicio = (139, 215, 232)
    Fin = (87, 209, 63)

    Agente = (0, 150, 0)
    Error = (255, 0, 0)
    Borde = (97, 42, 82)
    
    @classmethod
    def from_terrain(arr, color):
        return arr[color.name].value
    
class Passable(Enum):
    Pared = False
    Piso = True
    Inicio = True
    Fin = True
    
    @classmethod
    def from_terrain(arr, color):
        return arr[color.name].value

class Cost(Enum):
    Pared = -1
    Piso = 1
    Inicio = 1
    Fin = 2
    
    @classmethod
    def from_terrain(arr, color):
        return arr[color.name].value

class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3
    
    @classmethod
    def turn_right(arr, direction):
        return Direction((direction.value + 1) % 4)
    
    @classmethod
    def turn_left(arr, direction):
        return Direction((direction.value - 1) % 4)