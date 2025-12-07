class Estudiante:
    """Clase que representa a un estudiante."""
    def __init__(self, nombre: str, notas: list[int]) -> None:
        """Inicializa una nueva instancia de la clase Estudiante.
        Args:
            nombre (str): El nombre del estudiante.
            notas (list[int]): Las notas del estudiante.
        """
        self.nombre = nombre
        self.notas = notas

    def calcular_promedio(self) -> float:
        """Calcula el promedio de las notas del estudiante.
        Returns:
            float: El promedio de las notas.
        """
        return sum(self.notas) / len(self.notas)
    
    def aprobo(self) -> bool:
        """Determina si el estudiante aprobó el curso.
        Returns:
            bool: True si aprobó, False en caso contrario.
        """
        return self.calcular_promedio() >= 51
    
    def resumen(self) -> str:
        """Genera un resumen del estudiante.
        Returns:
            str: Un resumen con el nombre, notas, promedio y estado de aprobación.
        """
        mensaje = f"Estudiante: {self.nombre}"
        mensaje += f", Notas: {self.notas}"
        mensaje += f", Promedio: {self.calcular_promedio()}"
        mensaje += f", Aprobado: {self.aprobo()}"
        return mensaje
    
estudiante_uno = Estudiante("Mati", [85, 90, 70])
print(estudiante_uno.resumen())