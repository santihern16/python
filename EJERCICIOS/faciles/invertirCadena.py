cadena = input("Ingresa una cadena de texto: ")
invertida = ""

#print(cadena[::-1])

'''
for c in cadena:
    invertida = c + invertida

'''

for i in range(len(cadena)-1, -1, -1):
    invertida += cadena[i]

print(invertida)