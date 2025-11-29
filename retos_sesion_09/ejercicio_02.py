class BeatBox:
    __instancia = None
    reproduciendo = False

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia
    
    def __init__(self):
        if self.reproduciendo:
            print("La consola ya se esta reproduciendo.")
            return
        self.__pista_seleccionada = None
        self.__nivel_volumen = 20      
        self.__efecto_aplicado = None 
        self.reproduciendo = True

    def seleccionar_pista(self, nombre_pista):
        """Selecciona una pista de audio."""
        self.__pista_seleccionada = nombre_pista
        print(f"Pista seleccionada: {self.__pista_seleccionada}")

    def ajustar_volumen(self, volumen):
        """Aumenta o disminuye el volumen."""
        if volumen == "subir":
            if self.__nivel_volumen < 100:
                self.__nivel_volumen += 5
                print(f"Volumen aumentado a {self.__nivel_volumen}")
            else:
                print("El volumen ya está al máximo.")

        elif volumen == "bajar":
            if self.__nivel_volumen > 0:
                self.__nivel_volumen -= 5
                print(f"Volumen disminuido a {self.__nivel_volumen}")
            else:
                print("El volumen ya está al mínimo.")

    def aplicar_efecto(self, efecto):
        """Aplica un efecto de sonido."""
        efectos_validos = ["eco", "reverb", "distorsion"]

        if efecto not in efectos_validos:
            print("❎ Efecto inválido. Aplica una de estas opciones: eco, reverb, distorsion")
            return
        
        self.__efecto_aplicado = efecto
        print(f"Efecto aplicado: {self.__efecto_aplicado}")

    def mostrar_estado(self):
        """Muestra el estado actual de la consola."""
        print("\nESTADO DE LA CONSOLA:")
        print(f"Pista seleccionada: {self.__pista_seleccionada}")
        print(f"Volumen: {self.__nivel_volumen}")
        print(f"Efecto aplicado: {self.__efecto_aplicado}\n")

# Menú
while True:
    print("-"*40)
    print("CONSOLA BEATBOX")
    print("1. Seleccionar pista")
    print("2. Subir volumen")
    print("3. Bajar volumen")
    print("4. Aplicar efecto")
    print("5. Mostrar estado")
    print("6. Salir")
    print("-"*40)

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Ingresa el nombre de la pista: ")
        BeatBox().seleccionar_pista(nombre)
    elif opcion == "2":
        BeatBox().ajustar_volumen("subir")
    elif opcion == "3":
        BeatBox().ajustar_volumen("bajar")
    elif opcion == "4":
        efecto = input("Ingresa un efecto (eco, reverb, distorsion): ").lower()
        BeatBox().aplicar_efecto(efecto)
    elif opcion == "5":
        BeatBox().mostrar_estado()
    elif opcion == "6":
        print("Saliendo de la consola BeatBox...")
        break
    else:
        print("❎ Opción inválida. Intenta nuevamente.")

