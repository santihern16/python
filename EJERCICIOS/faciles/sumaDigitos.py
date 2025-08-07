#Haz un programa que reciba un número entero positivo y calcule la suma de sus dígitos. Ejemplo: 1234 → 1+2+3+4 = 10.

suma = 0
numeros = input("Num: ")

for n in numeros:
    suma += int(n)

print(f"Suma: {suma}")