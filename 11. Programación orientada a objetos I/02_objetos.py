class Triangulo:

    # def inicializar_el_triangulo_en_cuestion(self):
    def __init__(self, base, altura, lado_extra):
        print("----- creacion -----")
        print(f"Se ha creado un el objeto\n")

        self.base = base
        self.altura = altura
        self.lado_extra = lado_extra
        print()

    def obtener_superficie(self):
        print()
        print("----- superficie -----")
        area = (self.base * self.altura) / 2
        print(f"el area del triangulo es {area}\n")
        return area

    def __str__(self):
        print()
        print("----- nombramiento -----")
        print(f"Este es el triangulo {self.base, self.altura, self.lado_extra}\n")
        return self.base, self.altura, self.lado_extra


# triangulo = Construir un triangulo de lados 3, 4 y 5 cuya base es 4 y su altura 3


xx = Triangulo(3, 4, 9)
yy = Triangulo(2, 5, 9)
ww = Triangulo(5, 6, 9)
zz = Triangulo(4, 7, 9)

triangulo1 = xx.obtener_superficie()
triangulo2 = yy.obtener_superficie()
triangulo3 = ww.obtener_superficie()
triangulo4 = zz.obtener_superficie()

xx = xx.__str__()
yy = yy.__str__()
ww = ww.__str__()
zz = zz.__str__()
