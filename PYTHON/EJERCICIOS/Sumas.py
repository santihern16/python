#pedir 2 numeros enteros al usuario y sumarlos.
from cgi import print_form


print("Programa para sumar 2 numeros.\n")
num1=int(input("Digite el primer número: "))
num2=int(input("Digite el segundo número: "))

resultado=num1+num2

print(f"El resultado de la suma de {num1} y {num2} es: {resultado}")