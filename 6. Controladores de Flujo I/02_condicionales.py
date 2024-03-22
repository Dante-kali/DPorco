xx = int(input("Ingresar año de nacimiento: "))


# Silenciosa  : 1920 - 1940
# Boomer      : 1946 - 1964
# Generación X: 1965 - 1979
# Generación Y: 1980 - 2000
# Generación Z: 2001 - 2010

if xx >= 1920 and xx <= 1940:
    print("\n--Generación Silenciosa--\n")

elif xx >= 1946 and xx <= 1964:
    print("\n--Boomer--\n")

elif xx >= 2001 and xx <= 2010:
    print("\n--Generación Z--\n")

elif xx >= 1980 and xx <= 2000:
    print("\n--Generación Y--\n")

elif xx >= 1965 and xx <= 1979:
    print("\n--Generacion X--\n")

else:
    print("no existe generacion asociada c:")
