class Area:
    def __init__(self, tipo, lado1, lado2=None):
        self.tipo = tipo
        self.lado1 = lado1
        self.lado2 = lado2
    def calcular(self):
        if self.tipo == "rectangulo":
            return self.lado1 * self.lado2
        elif self.tipo == "cuadrado":
            return self.lado1 ** 2
area_rectangulo = Area("rectangulo", 5, 10)
print(area_rectangulo.calcular())
area_cuadrado = Area("cuadrado", 5)
print(area_cuadrado.calcular())

class Calculadora:
    """Clase que representa una calculadora simple."""
    def area(self, lado1, lado2):
        """Calcula el área de un rectángulo o cuadrado.

        Args:
            lado1 (int): El primer lado.
            lado2 (int): El segundo lado.

        Returns:
            int: El área calculada.
        """
        return lado1, lado2
    
calculadora = Calculadora()
print(calculadora.area(4, 8))
print(calculadora.area(4, 4))