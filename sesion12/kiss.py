class Calculadora:
    """Clase que representa una calculadora simple."""
    def sumar(self, a, b):
        """Suma dos números enteros.

        Args:
            a (int): El primer número.
            b (int): El segundo número.

        Returns:
            int: La suma de los dos números.
        """
        return a + b
    
calc = Calculadora()
print(calc.sumar(5, 7))