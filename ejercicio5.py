class cuenta_bancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print("depósito realizado. saldo actual:", self.saldo)
        else:
            print("el monto debe ser mayor a cero")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print("retiro realizado. saldo actual:", self.saldo)
        else:
            print("advertencia: no tienes suficiente saldo")

    def mostrar_saldo(self):
        print("saldo de", self.titular + ":", self.saldo)


mi_cuenta = cuenta_bancaria("juan", 100)

mi_cuenta.mostrar_saldo()
mi_cuenta.depositar(50)
mi_cuenta.retirar(30)
mi_cuenta.retirar(150)
mi_cuenta.mostrar_saldo()
 