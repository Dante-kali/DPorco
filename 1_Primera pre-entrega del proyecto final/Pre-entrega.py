registro = {}


def registrar():
    while True:
        usuario = input("\nIngresar un nombre de usuario: ")
        contraseña = input("Ingresar una contraseña: ")
        registro[usuario] = contraseña
        seguir = input("Desea seguir agregando usuarios (si o no)?: ")

        if seguir.lower() == "no":
            break

        elif seguir.lower() == "si":
            pass

        else:
            print("Opcion no valida")

        print(f"\nRegistro exitoso {usuario}\n")


registrar()


def mostrar_registro():
    print("\nRegistro de Usuarios:")
    for usuario, contraseña in registro.items():
        print(f"{usuario}: {contraseña}")


mostrar_registro()


def loggear():
    nombre = input("\nIngresar su nombre de usuario: ")
    contraseña = input("Ingresar su contraseña: ")

    if nombre in registro and contraseña == registro[nombre]:
        print(f"\nHas ingresado con éxito {nombre}\n")
    else:
        print("\nInicio de sesión sin éxito. Usuario o contraseña incorrectos.\n")


loggear()
