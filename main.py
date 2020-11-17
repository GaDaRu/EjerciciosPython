import turtle
from math import pi

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def x(self):
        return self.x()

    def y(self):
        return self.y()

class Forma:
    def __init__(self, color, x, y, nombre):
        self.color = color
        self.x = x
        self.y = y
        # super().__init__(x,y)
        self.nombre = nombre

    def imprimir(self):
        # colo = turtle.Screen()
        # colo.bgcolor(self.color)
        #
        # figura = turtle.Turtle()
        # figura.circle(self.x)
        for i in range(self.y):
            for j in range(self.x):
                print("*")
            print()

    def setColor(self, color):
        self.color = color

    def getColor(self):
        print(self.color)

class Rectangulo(Forma):
    def __init__(self,color, x, y, lMe, lMa):
        super().__init__(color, x, y, "Rectangulo")
        self.lMe = lMe
        self.lMa = lMa

    def imprimir(self):
        print("Nombre: " + self.nombre + ", Color: " + self.color + ", Centro: X" + ", Lado: ")
        print(self.lMe)

        for i in range(self.lMe):
            for j in range(self.lMa):
                print("*")
            print()

    def calArea(self):
        print(self.lMe*self.lMa)

    def calPerimetro(self):
        print((2*self.lMa)+(2*self.lMe))

    def camRectangulo(self, escala):
        self.lMa = self.lMa*escala
        self.lMe = self.lMe*escala
        self.imprimir()


class Eclipse(Forma):
    def __init__(self,color, x, y, R, r):
        super().__init__(color, x, y, "Eclipse")
        self.R = R
        self.r = r

    def areaEclipse(self):
        print(pi*(self.R*self.r))

class Cuadrado(Rectangulo):
    def __init__(self,color, x, y, lMe, lMa):
        super().__init__(color, x, y, lMe, lMa)

class Circulo(Eclipse):
    def __init__(self,color, x, y, R, r):
        super().__init__(color, x, y, R, r)

# fo = Forma("green", 80, 12, "Triangulo")
# fo.getColor()
# fo.imprimir()

Rec = Rectangulo("green", 20, 30, 3, 3)
# Rec.imprimir()
# Rec.calArea()
# Rec.camRectangulo(2)