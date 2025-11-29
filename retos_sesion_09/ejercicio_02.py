class BeatBox:
    __instancia = None

    def __new__(cls):
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        return cls.__instancia
    
    def seleccionar_pista(self, pista_Seleccionada):
        """Selecciona una pista por su nombre"""
        if not pista_Seleccionada.strip():
            print("El nombre de la pista no puede estar vacío.")
            return
        
        self.__pista = pista_Seleccionada.strip()
        print(f"Pista seleccionada: {self.__pista}")

    def ajustar_volumen(self):
        """Sube o baja el volumen dentro del rango 0–100"""
        print("\nAjustar volumen:")
        print("1. Subir volumen")
        print("2. Bajar volumen")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            if self.__nivel_volumen < 10:
                self.__nivel_volumen += 5
                print(f"Volumen aumentado a {self.__nivel_volumen}")
            else:
                print("El volumen ya está al máximo (10).")

        elif opcion == "2":
            if self.__nivel_volumen > 0:
                self.__nivel_volumen -= 5
                print(f"Volumen disminuido a {self.__nivel_volumen}")
            else:
                print("El volumen ya está al mínimo (0).")

        else:
            print("❌ Opción no válida.")

        def aplicar_efecto(self):
            """Aplica uno de los efectos disponibles"""
            print("\nAplicar efecto de sonido:")
            print("1. Eco")
            print("2. Reverb")
            print("3. Distorsión")
            print("4. Quitar efecto")

            opcion = input("Seleccione una opción: ")

            efectos = {
                "1": "Eco",
                "2": "Reverb",
                "3": "Distorsión",
                "4": None
            }

            if opcion in efectos:
                self.__efecto = efectos[opcion]
                if self.__efecto:
                    print(f"Efecto aplicado: {self.__efecto}")
                else:
                    print("Efecto eliminado")
            else:
                print("Opción no válida.")

    def mostrar_estado(self):
        """Muestra la configuración actual de la consola"""
        pista = self.__pista if self.__pista else "Ninguna"
        efecto = self.__efecto if self.__efecto else "Ninguno"

        print("\nEstado actual de la consola BeatBox:")
        print(f" Pista: {pista}")
        print(f" Volumen: {self.__volumen}")
        print(f" Efecto: {efecto}")

    # Representación como string
    def __str__(self):
        pista = self.__pista if self.__pista else "Ninguna"
        efecto = self.__efecto if self.__efecto else "Ninguno"
        return f"BeatBox(pista={pista}, volumen={self.__volumen}, efecto={efecto})"
    
def menu():
    beatbox = BeatBox()

    while True:
        print("\n=== 🎧 Consola BeatBox ===")
        print("1. Ingresar el nombre de la pista de audio")
        print("2. Ajustar volumen")
        print("3. Aplicar efecto de sonido")
        print("4. Mostrar estado actual")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pista = input("Ingrese el nombre de la pista: ")
            beatbox.seleccionar_pista(pista)

        elif opcion == "2":
            beatbox.ajustar_volumen()

        elif opcion == "3":
            beatbox.aplicar_efecto()

        elif opcion == "4":
            beatbox.mostrar_estado()

        elif opcion == "5":
            print("Saliendo de BeatBox...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")