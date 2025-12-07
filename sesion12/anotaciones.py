from typing import List

edad: int = 30  
nombre: str = "Jhon" 
altura: float = 1.75
activo: bool = True
print(type(edad))  # <class 'int'>
print(type(nombre))  # <class 'str'>
print(type(altura))  # <class 'float'>
print(type(activo))  # <class 'bool'>

numeros: list[int] = []
nombres: dict[str, str] = {}  
tuplas: tuple[int, str] = ()

def sumar(a: int, b: int) -> int:
    return a + b

print(sumar(10,10))

def cuadrados(numeros: list[int]) -> list[int]:
    return [n ** 2 for n in numeros]
numeros = cuadrados([2,4,6])
print (numeros)


class Persona:
    especie: str = "Homo sapiens"
    def __init__(self, nombre: str, edad: int):
        self.nombre: str = nombre
        self.edad: int = edad

jhon = Persona("Jhon",10)


def cuadrados(numeros: List[int]) -> List[int]:
    return [n ** 2 for n in numeros]
numeros = cuadrados([2, 4, 6])
print(numeros)
