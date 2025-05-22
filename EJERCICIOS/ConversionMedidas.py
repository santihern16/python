'''
Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:
• yardas
• pulgadas
• centímetros
• metros
Sabiendo que: 1 pie = 12 pulgadas, 1 yarda = 3 pies, 1 pulgada = 2.54 centímetros, 
1 metro = 100 centímetros.

'''

pies=float(input("Valor en pies-->"))

pulgadas=pies*12
yardas=pies/3
centimetro=pies*30.48
metro=pies/3.281

print(f"El valor de {pies} pies en pulgadas es {pulgadas}")
print(f"El valor de {pies} pies en yardas es {yardas}")
print(f"El valor de {pies} pies en centímetros es {centimetro}")
print(f"El valor de {pies} pies en metros es {metro:.4f}")


