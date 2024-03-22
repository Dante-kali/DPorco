# Descripción de la actividad.

# 1. Para aprobar un crédito, el cliente debe ser mayor de edad.
# 2. Además, debe tener una antigüedad en el sistema financiero de mínimo 3 años y
# un ingreso mayor a 2500 dólares.
# 3. En caso no tenga la antigüedad suficiente su ingreso mensual debe ser como mínimo 4000 dólares.
# 4. Si no cumple ninguna de las condiciones, no se aprueba el crédito

# Pedimos los datos para aprobar el credito
edad = int(input("Ingrese su edad: "))
antiguedad = int(input("Ingrese su antiguedad: "))
ingreso = int(input("Ingrese su pago mensual: "))

# Creamos condicionales para saber si cumple las condiciones

# Comprobamos su ingreso y tambien su edad y antiguedad
if ingreso >= 2500 and (edad - antiguedad) >= 18:
    print("Su ingreso ha sido aprobado")

# Comprobamos si su antiguedad tiene sentido con su edad
elif antiguedad >= 3 and (edad - antiguedad) >= 18:
    print("Su antiguedad ha sido aprobada...")

# Comprobamos que su antiguedad cumpla con los parametros
if antiguedad < 3:
    if ingreso > 4000:
        print("Su ingreso ha sido aprobado")

# Comprobamos su edad y tambien si su antiguedad tiene sentido
elif edad >= 18 and (edad - antiguedad) >= 18:
    print("Su edad ah sido aprobada...")

else:
    print("Sus datos no cumplen las condiciones")
