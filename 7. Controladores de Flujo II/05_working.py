import time

# Ejercicios Básicos en `for` y `wile` Loops de Python

## `for`
# 1. Escribir un programa que calcule la suma de los primeros 10 enteros positivos.
#    ```bash
#    # Ejemplo
#    - Entrada esperada: Ninguna
#    - Salida esperada: 55
#     ```

"""suma = 0
for i in range(1, 11):
    time.sleep(.2)
    suma += i

print(suma)"""

# 2. Escribir un programa que imprima los primeros 10 números impares.
#    ```bash
#    # Ejemplo
#    - Entrada esperada: Ninguna
#    - Salida esperada: 1 3 5 7 9 11 13 15 17 19
#     ```

"""for i in range(10):
    time.sleep(.2)
    if i % 2 != 0:
        print(i)"""

# 3. Escribir un programa que calcule el factorial de un número entero dado. Un factorial es el producto de todos los enteros positivos desde 1 hasta un número dado. Se representa con el signo de exclamación (!). Por ejemplo, el factorial de 5 se escribe como 5! y se calcula como 5 x 4 x 3 x 2 x 1 = 120.
#    ```bash
#    # Ejemplo
#    - Entrada esperada: 5
#    - Salida esperada: 120
#     ```

"""rango = 5

for xx in range(rango):
    
    if xx != 0:
        rango *= xx
print(rango)"""

# 4. Escribir un programa que tome como input del usuario un número y calcule la suma de todos los números pares menores al valor ingresado:
#     ```bash
#    # Ejemplo
#     >> Ingresar número: 9
#     >> La suma de los números pares menores a 9 es: 20
#     ```

"""numero = int(input("Ingrese un numero al azar: "))
suma = 0
for i in range(1, numero):
    time.sleep(.2)
    if i % 2 == 0:
        suma += i
print(suma)"""

# 5. Escribir un programa que encuentre el elemento más grande en una lista de enteros dada.
#    ```bash
#    # Ejemplo
#    - Entrada esperada: [5, 10, 2, 8, 3]
#    - Salida esperada: 10
#     ```

"""mi_lista = [5, 10, 2, 8, 3]
mi_lista.sort(reverse=True)
numero_grande = mi_lista[0]

for i in mi_lista:
    time.sleep(.2)
    if i == numero_grande:
        print(i)"""

# 6. Escribir un programa que imprima un rectángulo de asteriscos de un ancho y alto dados.
#    - Entrada esperada: ancho=4, alto=3
#    - Salida esperada:
#       ```
#       ****
#       ****
#       ****
#       ```

# Forma dificil
"""ancho = 4
alto = 3
tablero = []

for i in range(alto):
    time.sleep(.2)
    fila = []
    
    for i in range(ancho):    
        time.sleep(.2)    
        fila.append("*")
    tablero.append(fila)

for i in tablero:
    time.sleep(.2)
    tablero = "".join(i)
    print(tablero)"""

# Forma Facil
"""for i in range(alto):
    time.sleep(.2)
    print("*" * ancho)"""

# 7. Escribir un programa que imprima un triángulo rectángulo de asteriscos de una altura dada.
#    - Entrada esperada: alto=5
#    - Salida esperada:
#       ```
#       *
#       **
#       ***
#       ****
#       *****
#       ```

"""alto = 5

for i in range(alto + 1):
    i *= "*" 
    print(i) """

# 8. Escribir un programa que imprima la tabla de multiplicar para los números del 1 al 5.
#    - Entrada esperada: Ninguna
#    - Salida esperada:
#       ```
#        1  2  3  4  5
#       --------------
#       1|1  2  3  4  5
#       2|2  4  6  8  10
#       3|3  6  9  12 15
#       4|4  8  12 16 20
#       5|5  10 15 20 25
#       ```

""""""

# 9. Escribir un programa que calcule e imprima la suma de todos los números entre 1 y 10, y la suma de sus cuadrados.
#    - Entrada esperada: Ninguna
#    - Salida esperada:
#       ```
#       La suma de los números es: 55
#       La suma de los cuadrados es: 385
#       ```

"""suma = 0
suma_cuadrados = 0

for i in range(1, 11):
    time.sleep(.2)
    suma += i
    suma_cuadrados += i ** 2

print(suma)
print(suma_cuadrados)"""

# 10. Escribir un programa que tome una lista de nombres y edades, y devuelva un diccionario que contenga solo los nombres de las personas que tienen 18 años o más.

#     ```
#     # Ejemplo
#     - Entrada esperada: [("Alice", 25), ("Bob", 16), ("Charlie", 19)]
#     - Salida esperada: {"Alice": 25, "Charlie": 19}
#     ```

"""lista = [("Alice", 25), ("Bob", 16), ("Charlie", 19)]
diccionario = {}
mayores = {}

for i in lista:
    nombre,edad = i
    diccionario[nombre] = edad

print(diccionario)

for nombre, edad in diccionario.items():
    
    if edad >= 18:
        mayores[nombre] = edad
print(mayores)
"""

# 11. Escribir un programa que tome una cadena de texto y devuelva un diccionario que contenga la frecuencia de cada palabra en la cadena.

#     ```
#     # Ejemplo
#     - Entrada esperada: "the quick brown fox jumps over the lazy dog"
#     - Salida esperada: {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}
#     ```

"""lista = "the quick brown fox jumps over the lazy dog".split(" ")
diccionario = {}

for i in lista:
    xx = lista.count(i)
    nombre= i
    diccionario[nombre] = xx 
    
print(diccionario)
"""
# 12. Escribir un programa que tome una lista de números y devuelva un diccionario que contenga la cantidad de números pares e impares en la lista.

#     ```
#     # Ejemplo
#     - Entrada esperada: [1, 2, 3, 4, 5, 6]
#     - Salida esperada: {"par": 3, "impar": 3}
#     ```

"""lista = [1, 2, 3, 4, 5, 6]
diccionario = {}
pares = 0
impares = 0

for xx in lista:
    if xx % 2 == 0:
        pares += 1
        
    else:
        impares += 1
        
diccionario["par"] = pares
diccionario["impar"] = impares   

print(diccionario)  """

# 13. Escribir un programa que tome una lista de enteros y devuelva un diccionario que contenga el máximo, mínimo y promedio de los números en la lista.

#     ```
#     # Ejemplo
#     - Entrada esperada: [5, 10, 2, 8, 3]
#     - Salida esperada: {"max": 10, "min": 2, "prom": 5.6}
#     ```

"""lista = [5, 10, 2, 8, 3]
lista.sort(reverse=True)
diccionario = {}
suma = 0
cantidad_numeros = 0

for xx in lista:
    suma += xx
    
diccionario["max"] = lista[0]
diccionario["min"] = lista[-1]
diccionario["prom"] = suma / len(lista)
print(diccionario)"""

# ## `while`
# 14. Imprime todos los números pares del 0 al 20 usando un bucle "while".

#    ```
#    Ejemplo
#    - Ejemplo de salida: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20
#    ```

"""xx = 0
lista = []

while xx < 20: 
    
    if xx == 20:
        print(xx, end="")
    
    else:
        xx += 2
        print(xx, end=", ")"""


# 15. Imprime todos los números del 10 al 1 en orden descendente usando un bucle "while".

#    ```
#    Ejemplo
#    - Ejemplo de salida: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
#    ```

"""import time

xx = 11

while xx > 0:
    print(xx, end=", " if xx != 1 else "")
    time.sleep(0.2)
    xx -= 1"""

# 16. Pide al usuario que ingrese un número entero positivo y luego imprime todos los números impares del 0 hasta ese número en orden ascendente usando un bucle "while".

#    ```
#    Ejemplo
#    - Ejemplo de salida (el usuario ingresa 4): 1, 3
#    ```

"""numero_usuario = int(input("Ingrese su numero: "))
xx = 0

while xx <= numero_usuario:
    xx += 1
    
    if xx % 2 != 0:
        print(xx, end=" ,")
        
    
    if xx == numero_usuario:
        xx = numero_usuario + 1
"""
# 17. Elije una contraseña. Pide al usuario que ingrese una contraseña y sigue pidiéndoles que ingresen una contraseña hasta que ingresen la contraseña que has elegido usando un bucle "while".

#    ```
#    Ejemplo: la contraseña es admin1234
#    >> Ingrese la contraseña: password1234
#    >> Contraseña incorrecta. Ingrese la contraseña: admin!
#    >> Contraseña incorrecta. Ingrese la contraseña: admin1234
#    >> Bienvenido usuario!

#    ```

"""contraseña = "visiones"
xx = 0

while xx < 10:
    usuario = input("Ingrese la contraseña: ")
    
    if usuario == contraseña:
        xx == 10
        print("Bienvenido usuario!")
    
    else:
        print("contraseña incorrecta!")"""


# 18. Modifica el ejercicio anterior para que el usuario tenga sólo 3 intentos fallidos.


#    ```
#    Ejemplo: la contraseña es admin1234
#    >> Ingrese la contraseña: password1234
#    >> Contraseña incorrecta. Ingrese la contraseña: admin!
#    >> Contraseña incorrecta. Ingrese la contraseña: ADMIN1234
#    >> Usuario bloqueado!

#    ```

"""contraseña = "visiones"
xx = 0

while xx < 3:
    usuario = input("Ingrese la contraseña: ")
    xx += 1
    
    if usuario == contraseña:
        xx == 10
        print("Bienvenido usuario!")
    
    elif xx == 3:
        print("contraseña incorrecta!")
        print("\n Usuario bloqueado")
    
    else:
        print("\ncontraseña incorrecta!")
        print("ingrese otra contraseña\n")"""

# 19. Modifica el ejercicio anterior para que se indiquen cuántos intentos restantes tiene el usuario.


#    ```
#    Ejemplo: la contraseña es admin1234
#    >> Ingrese la contraseña (3 intentos restantes): password1234
#    >> Contraseña incorrecta. Ingrese la contraseña (2 intentos restantes): admin!
#    >> Contraseña incorrecta. Ingrese la contraseña (1 intentos restantes): ADMIN1234
#    >> Usuario bloqueado!

#    ```

"""contraseña = "visiones"
xx = 3

while xx > 0:
    usuario = input("Ingrese la contraseña: ")
    xx -= 1
    
    if usuario == contraseña:
        xx == 10
        print("Bienvenido usuario!")
    
    elif xx == 0:
        print(f"contraseña incorrecta! (intentos restantes {xx})")
        print("\n Usuario bloqueado")
    
    else:
        print("\ncontraseña incorrecta!")
        print(f"ingrese otra contraseña (intentos restantes {xx})\n")
"""
