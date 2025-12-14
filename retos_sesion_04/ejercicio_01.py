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
    def realizar_deposito(self, monto_depositar):
        if monto_depositar > 0:
            self.__saldo += monto_depositar
            print(f"Se realizó un depósito de {monto_depositar} el saldo actual es {self.__saldo}")
        else:
            print("El monto a depositar debe ser mayor a 0.")

    # Método para realizar retiros    
    def realizar_retiro(self, monto_retirar):
        if self.__saldo >= monto_retirar:
            self.__saldo -= monto_retirar
            print(f"Se retiró {monto_retirar} el saldo actual es {self.__saldo}")
        else:
            print(f"Saldo insuficiente. Intentó retirar {monto_retirar}, pero solo tiene {self.__saldo}")

# Implementando la clase
cuenta_lorena = Cuenta(134500045, "Lorena Mendoza", 1500)
cuenta_lorena.mostrar_datos()
print("-------------------------------------------------")
cuenta_lorena.realizar_deposito(500)
cuenta_lorena.realizar_retiro(800)
print("-------------------------------------------------")
print(f"Saldo final: {cuenta_lorena.saldo}")
