import time

# Creamos la cantidad de filas y columnas
filas = 10
columnas = 10

tablero = []

# Con el bucle for creamos un tablero de juego (listas dentro de una lista "[[...][...][...]]")

# Con el bucle for y range hacemos que se ejecute 10 veces
for i in range(filas):
    fila = []

    # Con el bucle for y range hacemos que se ejecute 10 veces
    for i in range(columnas):

        # Se agrega un "." a fila en cada ejecucion y al mismo tiempo esa fila se agrega al tablero
        fila.append(".")
    tablero.append(fila)


j = 0

# Creamos un minijuego con el bucle while y for

# Mientras que j sea menor que 10 se va a seguir ejecutando
while j < 10:
    time.sleep(0.5)

    # Remplazamos un "." por un "0" con el indice de las listas
    tablero[2][j] = "0"

    # Hacemos lo mismo pero a la inversa
    tablero[2][j - 1] = "."

    # Con el bucle for iteramos, y pegamos todas las listas con "join"
    for xx in tablero:
        print("  ".join(xx))

    # Por ultimo, sumamos 1 con cada ejecucion para que el bucle no sea infinito
    j += 1

    print("\n_____________________________________________\n")
