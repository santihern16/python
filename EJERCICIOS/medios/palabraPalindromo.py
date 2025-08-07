'''
Crea un programa que verifique si una palabra o frase es un palíndromo (se lee igual al derecho y al revés). 
Debe ignorar espacios, mayúsculas y signos de puntuación.
Conceptos a practicar: Manipulación de strings, métodos de cadenas, limpieza de datos

otras formas de limpiar datos

#frase_modificada = "".join(frase.split())
#frase_modificada = frase.replace(" ", "").lower().strip(",.:;'][]{}/")
'''

import re

casos = [
    "Anita lava la tina",
    "A man, a plan, a canal: Panama",
    "race a car",  # No es palíndromo
    "Madam",
    "No 'x' in Nixon"  # No es palíndromo
]

for frase in casos:
    frase_modificada = re.sub(r'[^a-zA-Z]', '', frase).lower()
    resultado = "Es palindromo" if frase_modificada[::-1] == frase_modificada else "NO es palindromo"
    print(f"{frase} -> {resultado}")