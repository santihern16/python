#Conjuntos: grupos de elementos desordenados en los que no puede haber elmentos duplicados

#si no se agrega el set se entiende como un diccionario

conjunto=set()
conjunto={1,2,3,"hola",4.56}

print(conjunto)

#Agregar elementos a un conjunto(en un indice aleatorio)
conjunto.add("chao")
conjunto.add(4)
print(conjunto)

#Eliminar un elemento del conjunto

conjunto.discard("chao")
print(conjunto)

#Pertenece al conjunto?
print(11 in conjunto)
print(3 not in conjunto)

#Vaciar un conjunto

conjunto.clear()
print(conjunto)