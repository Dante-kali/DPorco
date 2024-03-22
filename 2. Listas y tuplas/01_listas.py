# Creamos una lista y la imprimos
mi_lista = [1, 5, 6, 7, "frodo", "sam", "merry"]
print("la lista es: ", mi_lista)

# Imprimimos "frodo" con indice
print(mi_lista[4])

# Calculamos la longitud de la lista y de "frodo"
print(f"la longitud de la lista es: {len(mi_lista)}")
print(f"la longitud del nombre 'frodo' es: {len(mi_lista[4])}")

# Reemplazamos 1 elemento de la lista
mi_lista[3] = "Gandalf"
print("la nueva lista es: ", mi_lista)

# Reemplazar de a rebanadas (slices)
mi_lista[:2] = ["aragorn", "boromir"]
print("la nueva lista es: ", mi_lista)

# Concatenamos dos listas diferentes
mi_otra_lista = ["Legolas", "Gimli"]
mi_lista = mi_lista + mi_otra_lista
print("la nueva lista es: ", mi_lista)

# Agregamos 1 elemento a la lista
elemento = "Pippin"
mi_lista.append(elemento)
print("la nueva lista es: ", mi_lista)

# Removemos un elemento de la lista con "del"
del mi_lista[2]
print("la nueva lista es: ", mi_lista)

# Agregamos 1 elemento a la lista
elemento = "Luke Skywalker"
mi_lista.append(elemento)
print("la nueva lista es: ", mi_lista)

# Extraemos el último elemento de la lista con "pop"
mi_personaje = mi_lista.pop()
print("la nueva lista es: ", mi_lista)
print("El personaje extraído es: ", mi_personaje)
