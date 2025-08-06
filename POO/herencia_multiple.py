class Clase1:
    pass
class Clase2:
    pass
class Clase3:
    pass
class Clase4(Clase1, Clase3, Clase2):
    pass

# Es posible también que una clase herede de otra clase y a su vez otra clase herede de la anterior.

# MRO o Method Order Resolution

# el MRO depende del orden en el que las clases son pasadas: 1, 3, 2.

print(Clase4.__mro__)

'''

class Clase1:
    pass
class Clase2(Clase1):
    pass
class Clase3(Clase2):
    pass
'''