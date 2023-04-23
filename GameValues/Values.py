from enum import Enum

class Terrain(Enum):
    Pared = 0
    Piso = 1
    Inicio = 2
    Fin = 3
    Mount = 4
    Tierra = 5
    Agua = 6
    Arena = 7
    Bosque = 8
    Pantano = 9
    Nieve = 10

class Color(Enum):
    Pared = (46, 30, 49)
    Piso = (204, 188, 161)
    Inicio = (139, 215, 232)
    Fin = (87, 209, 63)
    Mount = (0, 0, 0)
    Tierra = (184, 156, 44)
    Agua = (75, 209, 209)
    Arena = (176, 138, 51)
    Bosque = (68, 140, 4)
    Pantano = (148, 81, 138)
    Nieve = (255, 255, 255)


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
    Mount = True
    Tierra = True
    Agua = True
    Bosque = True
    Pantano = True
    Nieve = True
    
    @classmethod
    def from_terrain(arr, color):
        return arr[color.name].value

class Cost(Enum):
    Pared = -1
    Piso = 1
    Inicio = 1
    Fin = 2

class costHumano(Enum):
    Pared = -1
    Piso = 1
    Inicio = 1
    Fin = 2

    Mount = 0
    Tierra = 1
    Agua = 2
    Arena = 3
    Bosque = 4
    Pantano = 5
    Nieve = 5

    @classmethod
    def from_terrain(arr, terreno):
        return arr[terreno.name].value

class costMono(Enum):
    Pared = -1
    Piso = 1
    Inicio = 1
    Fin = 2

    Mount = 0
    Tierra = 2
    Agua = 4
    Arena = 3
    Bosque = 1
    Pantano = 5
    Nieve = 0

    @classmethod
    def from_terrain(arr, terreno):
        return arr[terreno.name].value


class costPulpo(Enum):
    Pared = -1
    Piso = 1
    Inicio = 1
    Fin = 2

    Mount = 0
    Tierra = 2
    Agua = 1
    Arena = 0
    Bosque = 3
    Pantano = 2
    Nieve = 0

    @classmethod
    def from_terrain(arr, terreno):
        return arr[terreno.name].value


class costSasquatch(Enum):
    Pared = -1
    Piso = 1
    Inicio = 1
    Fin = 2

    Mount = 15
    Tierra = 4
    Agua = 0
    Arena = 0
    Bosque = 4
    Pantano = 5
    Nieve = 3

    @classmethod
    def from_terrain(arr, terreno):
        return arr[terreno.name].value



class Costos(Enum):
    Humano = costHumano
    Mono = costMono
    Pulpo = costPulpo
    Sasquatch = costSasquatch

    @classmethod
    def from_agent(arr, agent):
        return arr[agent].value


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

class HumanoImg(Enum):
    Up = "Sprites/Humano/Humano-up.png"
    Down = "Sprites/Humano/Humano-down.png"
    Left = "Sprites/Humano/Humano-right.png"
    Right = "Sprites/Humano/Humano-left.png"

    @classmethod
    def for_direc(cls, direc):
        return cls[direc.name].value

class MonoImg(Enum):
    Up = "Sprites/Mono/Mono-up.png"
    Down = "Sprites/Mono/Mono-down.png"
    Left = "Sprites/Mono/Mono-left.png"
    Right = "Sprites/Mono/Mono-right.png"

    @classmethod
    def for_direc(cls, direc):
        return cls[direc.name].value

class PulpoImg(Enum):
    Up = "Sprites/Pulpo/Pulpo-up.png"
    Down = "Sprites/Pulpo/Pulpo-down.png"
    Left = "Sprites/Pulpo/Pulpo-left.png"
    Right = "Sprites/Pulpo/Pulpo-right.png"

    @classmethod
    def for_direc(cls, direc):
        return cls[direc.name].value

class SqashImg(Enum):
    Up = "Sprites/Sqash/Sqash-up.png"
    Down = "Sprites/Sqash/Sqash-down.png"
    Left = "Sprites/Sqash/Sqash-left.png"
    Right = "Sprites/Sqash/Sqash-right.png"

    @classmethod
    def for_direc(cls, direc):
        return cls[direc.name].value

class AgentImag(Enum):
    Humano = HumanoImg
    Mono = MonoImg
    Pulpo = PulpoImg
    Sasquatch = SqashImg


    @classmethod
    def for_agent(cls, agent):
        return cls[agent].value
