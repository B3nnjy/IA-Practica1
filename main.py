from Grficos.GLaberinto import Laberinto

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
        

laberinto = Laberinto(leer_lab())
matriz = laberinto.runGame()

escribir_lab(matriz)