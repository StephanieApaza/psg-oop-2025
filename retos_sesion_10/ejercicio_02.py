# Productos
class Monstruo:
    def __init__(self, tipo, fortalezas, debilidades, icono):
        self.tipo = tipo
        self.fortalezas = fortalezas
        self.debilidades = debilidades
        self.icono = icono

    def representar(self):
        return f"{self.tipo} {self.icono}  listo para luchar"
    
    def pelear(self, otro_monstruo):
        if otro_monstruo.tipo in self.fortalezas:
            return f"{self.tipo} gana la batalla 🏅"
        elif otro_monstruo.tipo in self.debilidades:
            return f"{self.tipo} pierde la batalla ✖️"
        else:
            return "Empate"
        
class Dragon(Monstruo):
    def __init__(self):
        super().__init__(tipo="dragón", fortalezas=["zombi"], debilidades=["vampiro"], icono="🐉")

class Zombi(Monstruo):
    def __init__(self):
        super().__init__(tipo="zombi", fortalezas=["vampiro"], debilidades=["dragón"], icono="🧟‍♀️")

class Vampiro(Monstruo):
    def __init__(self):
        super().__init__(tipo="vampiro", fortalezas=["dragón"], debilidades=["zombi"], icono="🧛‍♀️")

# Fabricas
class Spawner:
    def crear(self):
        pass

class SpawnerDragon(Spawner):
    def crear(self):
        return Dragon()

class SpawnerZombi(Spawner):
    def crear(self):
        return Zombi()

class SpawnerVampiro(Spawner):
    def crear(self):
        return Vampiro()
    
# Factory central (decide que monstruos crear)
class FabricaMonstruos:
    def crear_monstruo(self, tipo):
        tipo = tipo.lower()

        if tipo == "dragón" or tipo == "dragon":
            maquina = SpawnerDragon()
        elif tipo == "zombi":
            maquina = SpawnerZombi()
        elif tipo == "vampiro":
            maquina = SpawnerVampiro()
        else:
            raise ValueError("Ese monstruo no está disponible.")

        return maquina.crear()
    
# Menú de selección de monstruos
fabrica = FabricaMonstruos()

print("🧩 Selección de Monstruos 🧩")
print('Escribe "salir" en cualquier momento para terminar el simulador de batallas de monstruos.\n')

while True:
    print("\nJugador 1: Elige tu monstruo (dragón/zombi/vampiro):")
    eleccion_uno = input("> ").lower().strip()

    if eleccion_uno == "salir":
        print("Saliendo del juego...")
        break

    print("\nJugador 2: Elige tu monstruo (dragón/zombi/vampiro):")
    eleccion_dos = input("> ").lower().strip()

    if eleccion_dos == "salir":
        print("Saliendo del juego...")
        break

    try:
        monstruo_uno = fabrica.crear_monstruo(eleccion_uno)
        monstruo_dos = fabrica.crear_monstruo(eleccion_dos)
    except ValueError as error:
        print(error)
        continue

    print("\nRepresentaciones:")
    print("Jugador 1:", monstruo_uno.representar())
    print("Jugador 2:", monstruo_dos.representar())

    print("\n⚔️  Resultado de la batalla ⚔️")
    resultado = monstruo_uno.pelear(monstruo_dos)
    print(resultado)