# Productos
class Helado:
    def __init__(self, sabor, envase):
        self.sabor = sabor
        self.envase = envase

    def comer(self):
        print(f"{self.sabor} 🍦 en {self.envase}")

class HeladoVainilla(Helado):
    def __init__(self, envase):
        super().__init__("Vainilla", envase)

class HeladoChocolate(Helado):
    def __init__(self, envase):
        super().__init__("Chocolate", envase)

# Fabricas
class Maquina:
    def preparar(self, envase):
        pass
    
class MaquinaVainilla(Maquina):
    def preparar(self, envase):
        return HeladoVainilla(envase)
    
class MaquinaChocolate(Maquina):
    def preparar(self, envase):
        return HeladoChocolate(envase)

# Factory central (decide que máquina usar)
class FabricaHelados:
    def crear_helado(self, sabor, envase):
        if sabor == "vainilla":
            maquina = MaquinaVainilla()
        elif sabor == "chocolate":
            maquina = MaquinaChocolate()
        else:
            raise ValueError("Ese sabor no esta disponible.")

        return maquina.preparar(envase)


# Menú de opciones para pedidos de helado
fabrica = FabricaHelados()
while True:
    print("\n🍨 Pedidos de Helado 🍨")
    print("1. Vainilla en Cono")
    print("2. Vainilla en Vaso")
    print("3. Chocolate en Cono")
    print("4. Chocolate en Vaso")
    print('Escribe "salir" para terminar tu pedido.\n')
    
    opcion = input("Seleccione una opción: ").lower().strip()

    if opcion == "salir":
        print("Saliendo de la heladería. ¡Gracias por tu compra!")
        break
    if opcion == "1":
        helado = fabrica.crear_helado("vainilla", "cono")
    elif opcion == "2":
        helado = fabrica.crear_helado("vainilla", "vaso")
    elif opcion == "3":
        helado = fabrica.crear_helado("chocolate", "cono")
    elif opcion == "4":
        helado = fabrica.crear_helado("chocolate", "vaso")
    else:
        print("Opción inválida, intente pedir nuevamente.")
        continue

    helado.comer()

