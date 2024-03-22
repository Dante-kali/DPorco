# creando variables
mi_texto = "mundo de piedra"
mi_otro_texto = "maquiavelico"
separador = "      "

# Imprimimos la variable mi texto
print()
print(mi_texto)

# Imprimimos el indice [0] de la variable (mi_texto)
print()
print(mi_texto[1])

# imprimimos del indice [1] en adelante con slicing
print()
print(mi_texto[1:])

# Concatenamos y imprimimos las tres variables
print()
print(mi_texto + mi_otro_texto)
print(mi_texto + separador + mi_otro_texto)

# imprimimos la longintud de la variables separador con la funcion "len"
longitud = len(separador)
print(separador)
print(longitud)

# cambiamos el contenido de la variable "mi_texto"
mi_texto = "sin mercy"

# Imprimimos la variable
print(mi_texto)

# Imprimimos de el indice [1] al [8] con slicing
print(mi_texto[1:8])

# Imprimimos de el indice [1] al [8] dando saltos de a [2] con slicing
print(mi_texto[1:8:2])

# Imprimimos la cadena volteada con slicing
print(mi_texto[::-1])
cadena_volteada = mi_texto[::-1]
