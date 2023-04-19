from enum import Enum

class Terreno(Enum):
    Pared = 0
    Piso = 1

class Passable(Enum):
    Pared = False
    Piso = True
    
    @classmethod
    def from_terreno(cls, color):
        return cls[color.name].value

class Colores(Enum):
    Pared = (46, 30, 49)
    Piso = (204, 188, 161)
    Error = (255, 0, 0)
    Borde = (97, 42, 82)
    Agente = (0, 150, 0)
    
    @classmethod
    def from_terreno(cls, color):
        return cls[color.name].value

class Direction(Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3