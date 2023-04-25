from Grficos.GLaberinto import Laberinto
from Grficos.Menu.Menu import Menu
from Grficos.OpcLaberinto import OpcLaberinto

fileName = "mapa2.txt"


def leer_lab():
    with open(fileName, "r") as f:
        lineas = f.readlines()

    lab = []  # lista para guardar la matriz
    for linea in lineas:
        fila = [int(num) for num in [*linea.strip()]]
        lab.append(fila)
    return lab


def escribir_lab(lab):
    output = ""
    for line in lab:
        output += "".join(str(x) for x in line)
        output += "\n"

    output = output.strip()

    with open(fileName, "w") as f:
        f.writelines(output)


agent = Menu().agent

opc = OpcLaberinto(leer_lab())

matriz = opc.runGame()
escribir_lab(matriz)

laberinto = Laberinto(matriz, agent)
laberinto.runGame()


