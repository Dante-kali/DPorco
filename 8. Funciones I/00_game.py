import time

# # Ejercicio 1: encapsular el siguiente código en una función
# #               y utilizarla para dibujar el tablero 10 veces

"""filas = 8
Columnas = 10
def mini_game():
    tablero = []
    for i in range(filas):
        # fila = []
        # for j in range(Columnas):
        #     fila.append(".")
        fila = ["."] * Columnas  # listas de <Columnas> elementos
        tablero.append(fila)

    # tablero tienen <filas> elementos
    for xx in tablero:
        print("  ".join(xx)) # convertir la lista en str juntada por espacios e imprimirla
        # qué es xx?
for i in range(10):
    mini_game()"""

# Ejercicio 2: modificar la función anterior para que dibuje un "0" en
#              la 4ta fila y 5ta columna, es decir en la posición (3, 4)

"""def dibujar_tablero(filas, Columnas):

    tablero = []
    
    for i in range(filas):
        fila = ["."] * Columnas
        tablero.append(fila)
    
    tablero[3][4] = "0"
    
    for xx in tablero:
        print("  ".join(xx))
    

for i in enumerate(range(10)):
    dibujar_tablero()
    print()
"""
# Ejercicio 3: encapsular las líneas de código de "posicionamiento" en una función que se llame "mover"


"""filas = 8
Columnas = 10

def dibujar_tablero(posicion_fila, posicion_columna):
    
    tablero = []
    
    for i in range(filas):
        fila = ["."] * Columnas
        tablero.append(fila)

    tablero[posicion_fila][posicion_columna] = "0" # UNICA MODIFICACION
    
    for xx in tablero:
        print("  ".join(xx))
        
def mover(xx,yy):
    xx += 1
    
    yy += 1
    
    if xx > filas - 1:
        xx = 0
    
    if yy > Columnas - 1:
        yy = 0
    
    return xx,yy

posicion_fila = 0
posicion_columna = 0

while True:
    
    dibujar_tablero(posicion_fila, posicion_columna)
    posicion_fila,posicion_columna = mover(posicion_fila,posicion_columna)
    print()
    time.sleep(1)
"""

# Ejercicio 4: pedir al usuario que especifique en cada momento la fila y la columna en la cuál dibujar el "0"

"""FILAS = 6
COLUMNAS = 8
def dibujar_tablero(posicion_fila, posicion_columna):
    tablero = []
    for i in range(FILAS):
        fila = ["."] * COLUMNAS
        tablero.append(fila)

    tablero[posicion_fila][posicion_columna] = "0" # UNICA MODIFICACION
    for xx in tablero:
        print("  ".join(xx))


def mover(fila, columna):
    fila = int(input("Ingresar fila: "))
    columna = int(input("Ingresar columna: "))

    if fila > FILAS - 1:
        fila = 0
    if columna > COLUMNAS - 1:
        columna = 0

    return fila, columna


posicion_fila = 0
posicion_columna = 0
while True:
    dibujar_tablero(posicion_fila, posicion_columna)
    posicion_fila, posicion_columna = mover(posicion_fila, posicion_columna)
    print()
    time.sleep(0.5)"""

# Ejercicio 5: modificar el ejercicio anterior para que el usuario pueda mover el "0" utilizando las letras "a,w,d,s"
#              a: izquierda, w: arriba, d: derecha, s: abajo

FILAS = 6
COLUMNAS = 8


def dibujar_tablero(posicion_fila, posicion_columna):

    tablero = []

    for i in range(FILAS):

        fila = ["."] * COLUMNAS
        tablero.append(fila)

    tablero[posicion_fila][posicion_columna] = "0"

    for xx in tablero:
        print("  ".join(xx))

    return tablero


def mover_con_letras(xx, yy):

    while True:
        tablero = dibujar_tablero(posicion_fila, posicion_columna)
        usuario = input("a: izquierda, w: arriba, d: derecha, s: abajo")
        usuario.lower()

        if usuario == "a":
            tablero[posicion_fila][posicion_columna - 1] = "0"

        elif usuario == "d":
            tablero[posicion_fila][posicion_columna + 1] = "0"

        elif usuario == "w":
            tablero[posicion_fila + 1][posicion_columna] = "0"

        elif usuario == "s":
            tablero[posicion_fila - 1][posicion_columna] = "0"


def mover(fila, columna):

    if fila > FILAS - 1:
        fila = 0

    if columna > COLUMNAS - 1:
        columna = 0

    return fila, columna


posicion_fila = 0
posicion_columna = 0

while True:

    dibujar_tablero(posicion_fila, posicion_columna)

    mover_con_letras(posicion_fila, posicion_columna)

    posicion_fila, posicion_columna = mover(posicion_fila, posicion_columna)

    print()

    time.sleep(0.2)
