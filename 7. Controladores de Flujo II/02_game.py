import time

tablero = []
for i in range(5):  # Filas
    # time.sleep(1)
    # print(tablero)
    fila = []
    for j in range(10):  # Columnas
        fila.append(".")  # fila -> [".", ".", "."]
    tablero.append(
        fila
    )  # tablero -> [[".", ".", "."], [".", ".", "."], [".", ".", "."], [".", ".", "."], [".", ".", "."]]

# print(tablero)
print()
for xx in tablero:
    time.sleep(0.2)
    # print(xx)
    print("  ".join(xx))
print()
