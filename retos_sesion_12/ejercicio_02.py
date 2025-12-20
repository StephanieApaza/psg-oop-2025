class Tarea:
    """Representa una tarea individual"""

    def __init__(self, titulo: str, descripcion: str) -> None:
        """Inicializa una nueva tarea

        Args:
            titulo (str): Título de la tarea
            descripcion (str): Descripción de la tarea
        """
        self.titulo: str = titulo
        self.descripcion: str = descripcion
        self.completada: bool = False

    def marcar_completada(self) -> bool:
        """Marca la tarea como completada"""
        self.completada = True

    def __str__(self) -> str:
        """Representación en texto de la tarea
        Returns:
            titulo, descripcion (str): Título y descripción de la tarea
        """
        estado = "✅ Completada" if self.completada else "⏳ Pendiente"
        return f"{self.titulo} - {self.descripcion} [{estado}]"

class GestorDeTareas:
    """Gestiona una colección de tareas"""

    def __init__(self) -> None:
        """Inicializa el gestor con una lista vacía de tareas"""
        self.tareas: list[Tarea] = []

    def agregar_tarea(self, titulo: str, descripcion: str) -> None:
        """Agrega una nueva tarea al gestor
        
        Args:
            titulo (str): Título de la tarea
            descripcion (str): Descripción de la tarea
        """
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)
        print("✅ Tarea agregada correctamente.")

    def eliminar_tarea(self, titulo: str) -> None:
        """Elimina una tarea por su título
        
        Args:
            titulo (str): Título de la tarea
        """
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                print("Tarea eliminada correctamente.")
                return
        print("No se encontró una tarea con ese título.")

    def completar_tarea(self, titulo: str) -> None:
        """Marca una tarea como completada por su título
        
        Args:
            titulo (str): Título de la tarea
        """
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                tarea.marcar_completada()
                print("✔️  Tarea marcada como completada.")
                return
        print("No se encontró una tarea con ese título.")

    def listar_tareas(self) -> None:
        """Muestra todas las tareas con su estado"""
        if not self.tareas:
            print("No hay tareas registradas.")
            return

        print("\n📋 Lista de tareas:")
        for tarea in self.tareas:
            print(tarea)

def mostrar_menu() -> None:
    """Muestra el menú principal"""
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Marcar tarea como completada")
    print("4. Listar tareas")
    print("5. Salir")

def main() -> None:
    """Ejecuta el programa principal de gestor de tareas"""
    gestor = GestorDeTareas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            titulo = input("Título de la tarea: ").strip()
            descripcion = input("Descripción de la tarea: ").strip()
            gestor.agregar_tarea(titulo, descripcion)

        elif opcion == "2":
            titulo = input("Título de la tarea a eliminar: ").strip()
            gestor.eliminar_tarea(titulo)

        elif opcion == "3":
            titulo = input("Título de la tarea a completar: ").strip()
            gestor.completar_tarea(titulo)

        elif opcion == "4":
            gestor.listar_tareas()

        elif opcion == "5":
            print("Gestor de tareas finalizado.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()