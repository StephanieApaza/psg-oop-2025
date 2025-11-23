# Definición
class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __add__(self, otra_fraccion):
        """Suma de fracciones"""
        resultado_numerador = (self.numerador * otra_fraccion.denominador) + (otra_fraccion.numerador * self.denominador)
        resultado_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(resultado_numerador, resultado_denominador)
    
    def __sub__(self, otra_fraccion):
        """Resta de fracciones"""
        resultado_numerador = (self.numerador * otra_fraccion.denominador) - (otra_fraccion.numerador * self.denominador)
        resultado_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(resultado_numerador, resultado_denominador)
    
    def __mul__(self, otra_fraccion):
        """Multiplicación de fracciones"""
        resultado_numerador = self.numerador * otra_fraccion.numerador
        resultado_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(resultado_numerador, resultado_denominador)

    def __truediv__(self, otra_fraccion):
        """División de fracciones"""
        resultado_numerador = self.numerador * otra_fraccion.denominador
        resultado_denominador = self.denominador * otra_fraccion.numerador
        return Fraccion(resultado_numerador, resultado_denominador)
    
    # Comparaciones
    def __eq__(self, otra_fraccion):
        """Comparación de igualdad entre fracciones"""
        if isinstance(otra_fraccion, Fraccion):
            return self.numerador * otra_fraccion.denominador == otra_fraccion.numerador * self.denominador
        return False

    def __ne__(self, otra_fraccion):
        """Comparación de desigualdad entre fracciones"""
        if isinstance(otra_fraccion, Fraccion):
            return self.numerador * otra_fraccion.denominador != self.denominador * otra_fraccion.numerador
        return True

    def __lt__(self, otra_fraccion):
        """Comparación entre fracciones: Menor que"""
        if isinstance(otra_fraccion, Fraccion):
            return self.numerador * otra_fraccion.denominador < otra_fraccion.numerador * self.denominador
        return False

    def __gt__(self, otra_fraccion):
        """Comparación entre fracciones: Mayor que"""
        if isinstance(otra_fraccion, Fraccion):
            return self.numerador * otra_fraccion.denominador > otra_fraccion.numerador * self.denominador
        
# Uso
fraccion_uno = Fraccion(10, 3)
fraccion_dos = Fraccion(35, 5)

print(f"Fracciones: {fraccion_uno} | {fraccion_dos}")
print("\nOperaciones:")
print(f"{fraccion_uno} + {fraccion_dos} = {fraccion_uno + fraccion_dos}")
print(f"{fraccion_uno} - {fraccion_dos} = {fraccion_uno - fraccion_dos}")
print(f"{fraccion_uno} * {fraccion_dos} = {fraccion_uno * fraccion_dos}")
print(f"{fraccion_uno} / {fraccion_dos} = {fraccion_uno / fraccion_dos}")

print("\nComparaciones:")
print(f"{fraccion_uno} == {fraccion_dos}: {fraccion_uno == fraccion_dos}")
print(f"{fraccion_uno} != {fraccion_dos}: {fraccion_uno != fraccion_dos}")
print(f"{fraccion_uno} <  {fraccion_dos}: {fraccion_uno < fraccion_dos}")
print(f"{fraccion_uno} >  {fraccion_dos}: {fraccion_uno > fraccion_dos}")