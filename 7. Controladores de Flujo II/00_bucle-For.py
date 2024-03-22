# 1. Imprimir por pantalla los valores de las variables xx e yy.

# xx = 0
# yy = 10
# print(f"La variable xx vale: {xx}")
# print(f"La variable yy vale: {yy}")

# 2. Imprimir por pantalla los valores de las variables xx e yy 10 veces cada uno.

# xx = 0
# yy = 10

# # por Stefania
# print("xx" * 10, "yy"*10)
# print()
# # Kenneth
# print(str(xx)*10, str(yy)*10)
# print()

# # Luciano
# for i in range(10):
#     print(xx, yy)
# print()

# # Mariano
# print([xx] * 10)
# print([yy] * 10)
# print()

# 3. Modificar el ejercio anterior para que el valor de xx aumente hasta 9
# y el valor de yy disminuya hasta 1

import time

# xx = 0
# yy = 10

# for i in range(10):
#     time.sleep(1)
#     print(f"La variable 'i' vale: {i}")
#     print(f"La variable xx vale: {xx }")
#     print(f"La variable yy vale: {yy}")
#     print()

# j = 0

# while True:
#     time.sleep(1)
#     print(f"j vale: {j}")


#     if j == 3:
#         j = 0

tablero = []
for i in range(5):
    # time.sleep(1)
    # print(tablero)
    fila = []
    for j in range(3):
        fila.append(".")  # fila -> [".", ".", "."]
    tablero.append(
        fila
    )  # tablero -> [[".", ".", "."], [".", ".", "."], [".", ".", "."], [".", ".", "."], [".", ".", "."]]

xx = 0
yy = 10
for i in range(10):
    time.sleep(0.2)
    print(f"La variable 'i' vale: {i}")
    print(f"La variable xx vale: {xx + i}")
    print(f"La variable yy vale: {yy - i}")
    print()
