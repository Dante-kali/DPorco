posicion_fila = int(input("Elija la fila en la que quiera poner el 0: "))
posicion_columna = int(input("Elija la columna en la que quiera poner el 0: "))
decision_de_usuario = input(
    "Elegir caracter de reprentacion de casillero en el tablero: "
)

fila_limpia = [decision_de_usuario] * 10
for i in range(10):
    if i == posicion_fila:
        fila = (
            fila_limpia.copy()
        )  # copy() se usa para copiar y que no se sobreescriba `fila_limpia`
        fila[posicion_columna] = "0"
        # fila es igual al copy de fila limpia y fila limpia queda igual
        # El join esta convirtiendo la lista en string y separándolo con los espacios
        print(" ".join(fila))
    else:
        print(" ".join(fila_limpia))

""""    
# creo el tablero
fila = ["."] * 3
tablero = []
for i in range(4):
    tablero.append(fila.copy())
# tablero [2][1] hace que se vaya a la lista y el otro corchete que se vaya al el elemento de la lista
    
tablero[2][1] = "0"
for fila in tablero:
    print(fila)
""" ""
