# Definición
class Fruta:
    def __init__(self, nombre, peso):  # Constructor
        self.nombre = nombre
        self.peso = int(peso)

    def __str__(self):  # Método de representación en cadena
        return f"{self.nombre} ➡ {self.peso} g" 

    def __eq__(self, otro):  # Método de igualdad
        if isinstance(otro, Fruta):
            return self.nombre == otro.nombre and self.peso == otro.peso
        return False
    
    def __lt__(self, otro):  # Método de menor que
        if isinstance(otro, Fruta):
            return self.nombre == otro.nombre and self.peso < otro.peso
        return False

    def __gt__(self, otro):  # Método de mayor que
        if isinstance(otro, Fruta):
            return self.nombre == otro.nombre and self.peso > otro.peso
        return False
    
    def __ne__(self, otro):
        if isinstance(otro, Fruta):
            return self.nombre != otro.nombre and self.peso != otro.peso
        return False
    
    def __le__(self, otro):
        if isinstance(otro, Fruta):
            return self.nombre == otro.nombre and self.peso <= otro.peso
        return False
    
    def __ge__(self, otro):
        if isinstance(otro, Fruta):
            return self.nombre == otro.nombre and self.peso >= otro.peso
        return False

# Uso
manzana1 = Fruta('🍎', 150)
manzana2 = Fruta('🍎', 120)
manzana3 = Fruta('🍎', 150)
print(f'{manzana1} | {manzana2} | {manzana3}')
print(manzana1 == manzana3) 
print(manzana1 < manzana2)  
print(manzana1 > manzana2)
print(manzana2 < manzana3)
print(manzana2 != manzana3)
print(manzana2 <= manzana3)
print(manzana2 >= manzana3)