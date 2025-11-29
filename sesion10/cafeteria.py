# Productos
class Cafe:
    def tomar(self):
        print("Tomando un café")

class Expreso(Cafe):
    def tomar(self):
        print("☕ Tomando un expreso")

class Cappuccino(Cafe):
    def tomar(self):
        print("🥛 Tomando un cappuccino")

# Fabricas
class Cafetera:
    def preparar(self):
        pass
class CafeteraExpreso(Cafetera):
    def preparar(self):
        return Expreso()
class CafeteraCappuccino(Cafetera):
    def preparar(self):
        return Cappuccino()

# Factory Central (decide qué fábrica usar)
class Barista:
    def preparar_cafe(self, tipo):
        if tipo == "expreso":
            return CafeteraExpreso().preparar()
        if tipo == "cappuccino":
            return CafeteraCappuccino().preparar()
        raise ValueError("❌ Café no disponible. Intente de nuevo")

# Cliente (No conoce las fábricas, solo pide el café)
while True:
    tipo_cafe = input("💬 ¿Qué café desea? (expreso/cappuccino/salir): ")
    tipo_cafe = tipo_cafe.lower().strip()
    if tipo_cafe == "salir":
        print("🚶‍♂️ Saliendo de la cafetería.")
        break
    try:
        barista = Barista()
        cafe = barista.preparar_cafe(tipo_cafe)
        cafe.tomar()
    except ValueError as e:
        print(e)