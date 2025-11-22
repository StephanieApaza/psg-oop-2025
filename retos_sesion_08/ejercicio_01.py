# Definición
class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, otra_fraccion):
        """Suma de fracciones"""
        nuevo_numerador = (self.numerador * otra_fraccion.denominador) + (otra_fraccion.numerador * self.denominador)
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __sub__(self, otra_fraccion):
        """Resta de fracciones"""
        nuevo_numerador = (self.numerador * otra_fraccion.denominador) - (otra_fraccion.numerador * self.denominador)
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __mul__(self, otra_fraccion):
        """Multiplicación de fracciones"""
        nuevo_numerador = self.numerador * otra_fraccion.numerador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __truediv__(self, otra_fraccion):
        """División de fracciones"""
        nuevo_numerador = self.numerador * otra_fraccion.denominador
        nuevo_denominador = self.denominador * otra_fraccion.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    # Comparaciones
    def __eq__(self, otra_fraccion):
        """Igualdad"""
        if isinstance(otra_fraccion, Fraccion):
            return self.numerador * otra_fraccion.denominador == otra_fraccion.numerador * self.denominador
        return False

    def __ne__(self, otra_fraccion):
        """Desigualdad"""
        if isinstance(otra_fraccion, Fraccion):
            return (self.numerador * otra_fraccion.denominador != self.denominador * otra_fraccion.numerador)
        return True

    def __lt__(self, otra_fraccion):
        """Menor que"""
        if isinstance(otra_fraccion, Fraccion):
            return self.numerador * otra_fraccion.denominador < otra_fraccion.numerador * self.denominador
        return False

    def __gt__(self, otra_fraccion):
        """Mayor que"""
        if isinstance(otra_fraccion, Fraccion):
            return self.numerador * otra_fraccion.denominador > otra_fraccion.numerador * self.denominador

    # Representación   
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
        
# Uso
fraccion_uno = Fraccion(3, 4)
fraccion_dos = Fraccion(1, 3)

print("Operaciones:")
print(f"{fraccion_uno} + {fraccion_dos} = {fraccion_uno + fraccion_dos}")
print(f"{fraccion_uno} - {fraccion_dos} = {fraccion_uno - fraccion_dos}")
print(f"{fraccion_uno} * {fraccion_dos} = {fraccion_uno * fraccion_dos}")
print(f"{fraccion_uno} / {fraccion_dos} = {fraccion_uno / fraccion_dos}")

print("\nComparaciones:")
print(f"{fraccion_uno} == {fraccion_dos}: {fraccion_uno == fraccion_dos}")
print(f"{fraccion_uno} != {fraccion_dos}: {fraccion_uno != fraccion_dos}")
print(f"{fraccion_uno} <  {fraccion_dos}: {fraccion_uno < fraccion_dos}")
print(f"{fraccion_uno} >  {fraccion_dos}: {fraccion_uno > fraccion_dos}")