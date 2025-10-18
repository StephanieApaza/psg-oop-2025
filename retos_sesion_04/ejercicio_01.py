class Cuenta:
    def __init__(self, numero_cuenta, nombre_titular, saldo):
        self.__numero_cuenta = numero_cuenta
        self.nombre_titular = nombre_titular
        self.__saldo = saldo

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta
    
    @property
    def saldo(self):
        return self.__saldo

    # Mostrar datos de la cuenta
    def mostrar_datos(self):
        print(f"Nombre del titular: {self.nombre_titular}")
        print(f"Número de cuenta: {self.__numero_cuenta}")
        print(f"Saldo actual: {self.__saldo}")

    # Método para realizar depósitos
    def realizar_deposito(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Se realizó un depósito de {monto} el saldo actual es {self.__saldo}")
        else:
            print("El monto a depositar debe ser mayor a 0.")

    # Método para realizar retiros    
    def realizar_retiro(self, monto):
        if self.__saldo > monto:
            self.__saldo -= monto
            print(f"Se retiró {monto} el saldo actual es {self.__saldo}")
        else:
            print(f"Saldo insuficiente. Intentó retirar {monto}, pero solo tiene {self.__saldo}")

# Implementando la clase
cuenta1 = Cuenta(134500045, "Lorena Mendoza", 1500)
cuenta1.mostrar_datos()
print("-------------------------------------------------")
cuenta1.realizar_deposito(500)
cuenta1.realizar_retiro(800)
print("-------------------------------------------------")
print(f"Saldo final: {cuenta1.saldo}")
