# Definición
class Vector:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def __sumar(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)
    def __restar(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)
    def __multiplicar(self, escalar):
        return Vector(self.x * escalar, self.y * escalar)
    def __dividir(self, escalar):
        return Vector(self.x / escalar, self.y / escalar)
    def mostrar(self):
        return f"({self.x}, {self.y})"
    def __add__(self, vector):
        return self.__sumar(vector)
    def __sub__(self, vector):
        return self.__restar(vector)
    def __mul__(self, escalar):
        return self.__multiplicar(escalar)
    def __truediv__(self, escalar):
        return (self.__dividir(escalar))
    

# Uso
vector1 = Vector(1, 1)
vector2 = Vector(2, 3)
vector3 = vector1 + vector2  # Suma de vectores
vector4 = vector1 - vector2  # Resta de vectores
print(f"A: {vector1.mostrar()}")
print(f"B: {vector2.mostrar()}")
print(f"A+B: {vector3.mostrar()}")
print(f"A-B: {vector4.mostrar()}")
vector5 = vector1 * 5 # Multiplicación por escalar
vector6 = vector2 / 2 # División por escalar
print(f"A*B: {vector5.mostrar()}")
print(f"A/B: {vector6.mostrar()}")