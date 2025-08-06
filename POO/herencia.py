class Animal:
    def __init__(self, especie, edad) -> None:
        self.especie = especie
        self.edad = edad

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describir(self):
        print(f"Soy un Animal del tipo {type(self).__name__}")


# Perro hereda de Animal
class Perro(Animal):
    def __init__(self, especie, edad, owner):
        super().__init__(especie, edad) # Accede al constructor padre y pasa los parametros
        self.owner = owner
      
    def hablar(self):
        print("Guau Guau")
    
    def moverse(self):
        print("Caminando a 4 patas")

mi_perro = Perro("Cocker", 6, "Santiago")
mi_perro.describir()
mi_perro.hablar()
mi_perro.moverse()

class Gato(Animal):
    pass

print(Perro.__bases__) # (<class '__main__.Animal'>,)
print(Animal.__subclasses__())