#eliminar elementos de lista

lista=[1,2,3,4,5,6,"santixo"]
#se puede pasar un parametro del indice que se quiere eliminar, de lo contrario se eliminará el último elemento
lista.pop(3)

print(lista)

#remove elimina un elemento específico
lista.remove(5)
lista.remove("santixo")
print(lista)

#voltear la lista
lista.reverse()
print(lista)
#clear elimina todos los elementos de la lista
lista.clear()
print(lista)