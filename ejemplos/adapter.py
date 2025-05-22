# Interfaz esperada por el cliente
class PaymentProcessor:
    def process_payment(self, amount: int):
        raise NotImplementedError


# Clase con la interfaz incompatible
class ExternalPaymentAPI:
    def make_payment(self, amount_in_dollars: float):
        print(f"Procesando pago de ${amount_in_dollars} usando API externa.")


# Adaptador que convierte ExternalPaymentAPI a PaymentProcessor
class PaymentAdapter(PaymentProcessor):
    def __init__(self, external_api: ExternalPaymentAPI):
        self.external_api = external_api

    def process_payment(self, amount: int):
        self.external_api.make_payment(float(amount))


# Uso del adaptador
external_api = ExternalPaymentAPI()
payment_processor = PaymentAdapter(external_api)

payment_processor.process_payment(100)  # Salida: Procesando pago de $100.0 usando API externa.