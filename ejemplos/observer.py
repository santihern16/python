from typing import List


# Interfaz del observador
class Observer:
    def update(self, message: str):
        raise NotImplementedError


# Sujeto que mantiene la lista de observadores y los notifica
class Topic:
    def __init__(self):
        self.observers: List[Observer] = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, message: str):
        for observer in self.observers:
            observer.update(message)


# Observador concreto (Usuarios que reciben notificaciones)
class User(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f"{self.name} recibió notificación: {message}")


# Uso del patrón Observer
topic = Topic()

user1 = User("Carlos")
user2 = User("Ana")

topic.attach(user1)
topic.attach(user2)

topic.notify("Nuevo mensaje en el tema de discusión.")

topic.detach(user2)

topic.notify("Otro mensaje ha sido publicado.")

# Salida:
# Carlos recibió notificación: Nuevo mensaje en el tema de discusión.
# Ana recibió notificación: Nuevo mensaje en el tema de discusión.
# Carlos recibió notificación: Otro mensaje ha sido publicado.