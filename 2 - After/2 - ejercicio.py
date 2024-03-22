numero = int(input("Elija la pocision en la que quiera poner el 0: "))

for i in range(10):

    if numero > 9:
        print("Error")
        break

    elif i == numero + 1:
        print("0")
