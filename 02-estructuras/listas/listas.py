#LISTAS: Estructuras de datos que pueden almacenar diferentes valores.

lista=["esta","es","mi","primera","lista",6,3,2022,["sublista", True, False],"fin lista"]

print(lista)
print(lista[0:8])
print(lista[5:8])

#Determinar cuantos elementos tiene la lista
print(len(lista))

#Agregar elementos a una lista al final
lista2=[1,2,3,4,5]

lista2.append(6)
lista2.append("Santixo")

print(lista2)

#Agregar elementos a una lista en determinada posicion

lista3=[1,2,4,5,6]
#Parámetro 1: índice o posicion donde se va a agregar el elemento
#Parámetro 2: El elemento que se va a agregar a determinada posicion
lista3.insert(2,3)

#agregar varios elementos al final

lista3.extend([7,8,9])
print(lista3)

#Saber si un elemento pertenece a la lista

lista=[1,2,3,4,5,6,"santixo"]

print("santixo" in lista)

'''
Saber en que índice está un elemento de la lista
'''
lista2=[1,2,3,4,5,6,"santixo", "santixo"]
print(lista.index("santixo"))

#saber cuantas veces está un elemento en la lista
print(lista2.count("santixo"))


