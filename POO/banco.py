class CuentaBancaria:
    titular = "Santiago Hernandez"
    saldo = 0

    def depositar(self, monto):
        self.saldo = self.saldo + monto

    def retirar(self, monto):
        if monto > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo = self.saldo - monto

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

p1 = CuentaBancaria()
p1.depositar(300)
p1.retirar(250)
p1.mostrar_saldo()