# Creando un conjunto con colores
conjunto = {"Rojo", "Blanco", "Azul"}

# Agregamos colores al conjunto
conjunto.update(["Violeta", "Dorado"])

# Eliminamos colores del conjunto
conjunto.discard("Blanco")
conjunto.discard("Dorado")
conjunto.discard("Celeste")

# Imprimimos el conjunto resultante
print(conjunto)
