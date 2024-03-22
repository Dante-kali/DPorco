class Cliente:
    
    def __init__(self, nombre, edad, email, region, intereses):
        self.nombre = nombre
        self.region = region
        self.email = email
        self.edad = edad
        self.intereses = intereses
        
    def __str__(self):
       return f"Bienvenido a Whinter_Official, {self.nombre}" 
   
    def actualizar_datos(self, nombre, edad, email, region):
        self.nombre = nombre
        self.region = region
        self.email = email
        self.edad = edad
        
    def agregar_intereses(self, interes):
        self.intereses.append(interes)
    
# Ejemplo de uso
p1 = Cliente("Dante", 12, "porcodante8@gmail.com", "Argentina", ["tecnologia", "electronica"])

print(p1)
