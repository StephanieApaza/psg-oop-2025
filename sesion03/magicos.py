class Persona:
    def __init__(self, nombre, edad): # Constructor
        self.nombre = nombre
        self.edad = edad

    def __str__(self): # Método especial
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    def __repr__(self): # Método especial
        return f"Persona('{self.nombre}', {self.edad})"
    
    def __del__(self): # Método especial
        print(f"{self.nombre} ha sido eliminado")
    
# jhon = Persona("Jhon", 30)
# print(jhon) # Nombre: Jhon, Edad: 30
# jane = Persona("Jane", 25)
# detalle = str(jane)
# print(detalle) # Nombre: Jane, Edad: 25

jhon = Persona("Jhon", 30)
print (jhon)
print (repr(jhon))
print(jhon.__dict__) # {'nombre': 'Jhon', 'edad': 30}
jane = Persona("Jane", 25)
print (jane)
print (repr(jane))
print(jane.__dict__) # {'nombre': 'Jane', 'edad': 25}