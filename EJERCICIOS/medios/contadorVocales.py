'''
Pide una palabra al usuario y cuenta cuántas vocales tiene.
Conceptos: for, strings básicos, contadores
'''

def contarVocales(palabra, vocales):
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

# Versión mas python (más compacta):
def contarVocalesVCorta(palabra, vocales):
    return sum(1 for letra in palabra.lower() if letra in vocales)


if __name__ == '__main__':
    palabra = "murcielago."
    vocales = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']

    result = contarVocales(palabra.lower(), vocales)
    result2 = contarVocalesVCorta(palabra, vocales)

    print(f"La palabra {palabra} tiene {result} vocales")
    print(f"La palabra {palabra} tiene {result2} vocales")