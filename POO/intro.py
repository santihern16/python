class Persona:
    pies = 2 # Atributos de clase
    manos = 2
    def __init__(self, nombre, edad):
        self.nombre = nombre # Atributos de instancia
        self.edad = edad
        print(f"Bienvenido {nombre}")

p1 = Persona("Santiago", 23)
print(p1.nombre)
print(p1.edad)
print(Persona.pies)

class Guerrero:
    ataque = 300
    defensa = 250
    agilidad = 100

    def __init__(self, nombre, color_pelo, edad) -> None:
        self.nombre = nombre
        self.color_pelo = color_pelo
        self.edad = edad

    def atacar(self, cantidad: int):
        print(f"{self.nombre} ataca y genera {self.ataque * cantidad} de damage ⚔️")
    
    def defender(self):
        print(f"{self.nombre} se defiende y recibe {self.ataque - self.defensa} de damage")

guerrero1 = Guerrero("Viking", "Negro", 45)
guerrero1.atacar(2)
guerrero1.defender()

# Metodos de clase

class Clase():
    @classmethod
    def metodoClase(cls):
        return 'Metodo de clase', cls
    
    @staticmethod
    def metodoEstatico():
        return "Metodo estatico"

print(Clase.metodoClase())
mi_clase = Clase()
print(mi_clase.metodoClase())

print(Clase.metodoEstatico())
print(mi_clase.metodoEstatico())