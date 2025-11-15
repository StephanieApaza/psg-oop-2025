# Definición
class Persona:
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, soy {self.nombre} con {self.edad} años")

    def despedirse(self):
        print(f"Adiós, soy {self.nombre}")

    def __del__(self): # Destructor
        self.despedirse()

    def __repr__(self):  # Método de representación oficial
        return f"Persona('{self.nombre}', {self.edad})"
    
    def __str__(self):  # Método de representación en cadena
        return f"{self.nombre} ➡ {self.edad} años"

# Uso
jhon = Persona('Jhon', 30)
jhon.saludar()
#del jhon  # Eliminación
print(repr(jhon))
print(eval(repr(jhon)))
print(jhon) 