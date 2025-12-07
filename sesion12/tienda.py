class Tienda:
    def impuesto_tarjeta(self, monto):
        return monto * 0.05
    def impuesto_transferencia(self, monto):
        return monto * 0.02
    def impuesto_qr(self, monto):
        return monto * 0.01
    def pagar_tarjeta(self, monto):
        impuesto = self.impuesto_tarjeta(monto)
        total = monto + impuesto
        print(f"Pago con tarjeta: Monto={monto}, Impuesto={impuesto}, Total={total}")
    def pagar_transferencia(self, monto):
        impuesto = self.impuesto_transferencia(monto)
        total = monto + impuesto
        print(f"Pago con transferencia: Monto={monto}, Impuesto={impuesto}, Total={total}")
    def pagar_qr(self, monto):
        impuesto = self.impuesto_qr(monto)
        total = monto + impuesto
        print(f"Pago con QR: Monto={monto}, Impuesto={impuesto}, Total={total}")

tienda = Tienda()
tienda.pagar_tarjeta(100)
tienda.pagar_transferencia(100)
tienda.pagar_qr(100)

class Tienda:
    def calcular_impuesto(self, monto, tasa):
        return monto * tasa
    def pagar(self, monto, metodo):
        tasas = {
            "tarjeta": 0.05,
            "transferencia": 0.02,
            "qr": 0.01
        }
        tasa = tasas.get(metodo, 0)
        impuesto = self.calcular_impuesto(monto, tasa)
        total = monto + impuesto
        print(f"Pago con {metodo}: Monto={monto}, Impuesto={impuesto}, Total={total}")

tienda = Tienda()
tienda.pagar(100, "tarjeta")
tienda.pagar(100, "transferencia")
tienda.pagar(100, "qr")