'''
Crea un programa que pida una frase y cuente cuántas veces aparece cada palabra.

Ejemplo:
Entrada: "hola mundo hola"
Salida:
{
    "hola": 2,
    "mundo": 1
}

'''

frase = input("Frase: ")

palabras = frase.split()
print(palabras)
contador = {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print(contador)