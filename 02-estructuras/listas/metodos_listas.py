#Agregando elemento al final
import os
os.system('cls')

frutas = ["manzana", "banana", "sandia"]
lista = [1, 3 ,45, 6, 2, 6, '@', 84, 5]
print(lista)

lista.append(10)
print(lista)

#Agregando elementos en un indice especifico
lista.insert(1, '@')
print(lista)

#Agrega varios elementos al final de la lista
lista.extend([2, '🥲'])
print(lista)

#Eliminar elementos de la lista
lista.remove('@') #Remueve el PRIMER elemento que coincida con el parametro
print(lista)

ultimo = lista.pop() #Elimina el elemento de la lista y lo devuelve, por defecto indice -1
lista.pop(2) #Elimina el indice 2 de la lista
print(lista)
print(ultimo)

#Eliminar un rango de elementos
animales = ['perro', 'gato', 'loro', 'raton', 'tortuga']
print(animales)
del animales[1:3] #Elimina el rango de elementos desde el índice 1 hasta, pero sin incluir, el índice 3
print(animales)

lista.clear() #Elimina todos los elementos de la lista
print(lista)

#Ordenar listas
numeros = [1, 3, 5, 2, 4]
numeros.sort() #Ordena la lista de menor a mayor, pero no devuelve nada
print(numeros)

print("Creando una nueva lista")
sorted_numbers = sorted(numeros, reverse=True) #Ordena la lista y devuelve una nueva lista
print(sorted_numbers)

print("Lista de frutas (todo en minusculas)")
frutas = ["manzana", "banana", "sandia", "pera", "arandano"]
print(sorted(frutas)) #Ordena la lista de frutas

print("Lista de frutas (mezcla de mayusculas y minusculas)")
frutas = ["Manzana", "banana", "sandia", "Pera", "arandano"]
print(sorted(frutas)) #Ordena la lista de frutas pero no las ordena correctamente por las mayusculas
frutas.sort(key=str.lower) #Ordena la lista como si todos los elementos fueran minusculas
print(frutas)

#Cositas utiles
animals = ['🐶', '🐈', '🦍', '🐶']
print(animals.count('🐶')) # Hay 2 perritos en la lista
print('🐈' in animals) # Comprueba si existe el elemento en la lista -> True