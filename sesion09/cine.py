class Sala:
    __instancia = None
    titulo = ""
    reproduciendo = False
    clientes = []

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia

    def iniciar(self, titulo):
        if self.reproduciendo:
            print("La película se esta reproduciendo")
            return
        self.titulo = titulo
        self.reproduciendo = True
        print(f"Iniciando la pelicula {self.titulo}")

    def unirse(self, cliente):
        self.clientes.append(cliente)
        print(f"{cliente} se ha unido a la sala")

    def estado(self):
        estado = "Reproduciendo" if self.reproduciendo else "Detenida"
        print(f"Pelicula {self.titulo} | Estado {estado}")

    def listar(self):
        print(f"Clientes en la sala: {len(self.clientes)}")
        for cliente in self.clientes:
            print(f"{cliente}")

    def finalizar(self):
        print("Película finalizada")
        self.reproduciendo = False

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre}"
    
    def unirse(self):
        Sala().unirse(self)

while True:
    print("-"*40)
    print("Menú de cine virtual")
    print("1. Iniciar película")
    print("2. Unirse a sala")
    print("3. Ver estado")
    print("4. Ver clientes")
    print("5. Finalizar película")
    print("6. Salir")
    print("-"*40)

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        titulo = input("Título de la película: ")
        Sala().iniciar(titulo)
    elif opcion == "2":
        nombre = input("Escribe tu nombre: ")
        cliente = Cliente(nombre)
        cliente.unirse()
    elif opcion == "3":
        Sala().estado()
    elif opcion == "4":
        Sala().listar()
    elif opcion == "5":
        Sala().finalizar()
    elif opcion == "6":
        break
    else:
        print("Opción no válida.")

