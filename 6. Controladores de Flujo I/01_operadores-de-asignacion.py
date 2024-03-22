import time

longitud = 0
mi_texto = "C'est La Mort"

for i in mi_texto:
    time.sleep(0.3)
    longitud += 1

    print(i, longitud)

print(f"La longitud de {mi_texto} es {longitud}")
