import time


def sumar_numeros(numeros: int):
    for i in range(numeros):
        time.sleep(0.5)
        numeros += numeros
        i += 1
        print(i, numeros)
