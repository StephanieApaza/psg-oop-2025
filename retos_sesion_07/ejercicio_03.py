# Definición
class Romano:
    def __init__(self, valor_romano):
        self._valor_romano = valor_romano.upper()
        self._valor_entero = self.convertir_entero(self._valor_romano)

    def convertir_entero(self, valor_romano):
        """Convierte un número romano a su equivalente entero"""
        valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
        total = 0

        for simbolo in valor_romano:
            total += valores.get(simbolo, 0)
        return total

    def convertir_romano(self, numero):
        """Convierte un número entero a su representación romana"""
        equivalencias = [
            ("C", 100), ("L", 50), ("X", 10), ("V", 5), ("I", 1)]
        resultado = ""

        for simbolo, valor in equivalencias:
            while numero >= valor:
                resultado += simbolo
                numero -= valor

        return resultado

    def __add__(self, nuevo_numero):
        """Permite sumar dos números romanos"""
        suma_entera = self._valor_entero + nuevo_numero._valor_entero
        resultado_romano = self.convertir_romano(suma_entera)
        return Romano(resultado_romano)

    def __str__(self):
        """Muestra el valor romano al imprimir el objeto"""
        return self._valor_romano

# Uso
num1 = Romano("L")
num2 = Romano("V") 

resultado = num1 + num2

print(f"{num1} + {num2} = {resultado}")