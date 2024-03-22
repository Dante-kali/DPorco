# Pedir al usuario que ingrese 2 numeros, sumarlos y motrarlos por pantalla
# Si el usuario ingresa algo que no puede ser interpretado como numero
# entonces mostrarle un mensaje de error y pedirle que ingrese números nuevamente

while True:
    try:
        numero_usuario = int(input("ingrese un numero: "))
        numero_usuario_2 = int(input("ingrese otro numero: "))

    except ValueError:
        print("Error Syntax")

    else:
        print(numero_usuario + numero_usuario_2)
        break

print("programa finalizado con exito")
