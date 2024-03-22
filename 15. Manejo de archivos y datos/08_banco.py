class Cliente:
    def __init__(self, nombre, identificador, email):
        self.nombre = nombre
        self.identificador = identificador
        self.email = email


class Persona(Cliente):
    def __init__(self, nombre, identificador, edad, email):
        super().__init__(nombre, identificador, email)
        self.edad = edad

    def __str__(self):
        return f"Persona: {self.nombre}"


class Empresa(Cliente):
    def __init__(self, nombre, identificador, email):
        super().__init__(nombre, identificador, email)
        self.razon_social = nombre

    def __str__(self):
        return f"Empresa: {self.razon_social}"

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = {}

    def __str__(self):
        return f"Banco {self.nombre}"

    def crear_cuenta(self, xx: Cliente):
        # xx no puede ser `str`, no puede ser `int`
        self.cuentas[xx.email] = 0

    def mostrar_todas_las_cuentas(self):
        return self.cuentas

    def transformar_cuentas_en_texto(self):
        texto = ""
        for identificador, saldo in self.cuentas.items():
            detalle = f"La cuenta {identificador} tiene saldo: {saldo}"
            texto = texto + detalle + "<br>"

        return texto

    def consultar_cuenta(self, xx: Cliente):
        email = xx.email
        return self.cuentas[email]

    def depositar_en_cuenta(self, cliente: Cliente, monto: int):
        self.cuentas[cliente.email] = self.cuentas[cliente.email] + monto




