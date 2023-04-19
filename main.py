from Grficos.GLaberinto import Laberinto

def leer_lab():
    with open("mapa2.txt", "r") as f:
        lineas = f.readlines()

    lab = []  # lista para guardar la matriz
    for linea in lineas:
        fila = [int(num) for num in linea.strip().split(",")]
        lab.append(fila)
    return lab


matriz = leer_lab()

print("Matriz leida: ")
for fila in matriz:
    print(fila)

laberinto = Laberinto(matriz)

laberinto.runGame()