#Escribe un programa que lea 10 números enteros y determine cuántos son pares y cuántos son impares usando un bucle for.
pares = 0
impares = 0 

for n in range(1, 11):
    num = int(input(f"Num {n}: "))
    if num % 2 == 0:
        print(f"El numero {num} es par")
        pares += 1
    else:
        print(f"El numero {num} es impar")
        impares += 1

print(f"Total numeros pares: {pares}")
print(f"Total numeros impares: {impares}")