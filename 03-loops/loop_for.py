from os import system
system("cls")

frutas = ["manzana", "banana", "cereza", "durazno", "kiwi"]

# Iterar una lista
for fruta in frutas:
    print(fruta)

# Iterar sobre cualquier cosa que sea iterable
cadena = "santixo"
for char in cadena:
    print(char)

# enumerate()
# permite iterar sobre un objeto iterable y obtener el índice y el valor
frutas = ["manzana", "banana", "cereza", "durazno", "kiwi"]
for index, fruta in enumerate(frutas):
    print(f"{index}: {fruta}")

# bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for num in numeros:
        print(f"{letra}{num}")

# break y continue
print("\nbreak")

animales = ["perro", "gato", "elefante", "jirafa", "león"]
for index, animal in enumerate(animales):
    print(animal)
    if animal == 'elefante':
        print("Se ha encontrado al elefante en el índice", index)
        break

print("\ncontinue")
for index, animal in enumerate(animales):
    if animal == 'jirafa': continue
    print(animal)


#Comprension de listas (list comprehension)
animales = ["perro", "gato", "elefante", "jirafa", "león"]
animales_mays = [animal.upper() for animal in animales]
print(animales_mays)