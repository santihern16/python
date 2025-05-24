frutas = ["manzana", "banana", "sandia"]
print(frutas)
print(frutas[0])
print(frutas[-1])

matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)
print(matrix[1][1]) # numero 4

#Slicing
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros[2:5]) # 3, 4, 5
print(numeros[:3])
print(numeros[-3:])
print(numeros[:]) # Crea una copia de la lista completa

print(numeros[1:-1:2])
print("Reversa: ", numeros[::-1]) # En reversa

#Modificando listas
numeros[1] = 20
print(numeros)

#Agregando
numeros += [11, 12, 13]
print(numeros)

#Longitud de la lista
print(len(numeros))