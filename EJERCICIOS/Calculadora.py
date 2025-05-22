'''
Construir una calculadora con las 4 operaciones aritméticas.
El usuario debe digitar la operacion que desea realizar con la inicial 
de la misma.
'''
print("CALCULADORA ARITMÉTICA\n")
print("1.Suma(S, s)\n2.Resta(R, r)\n3.Multiplicación(P, p - M, m)\n4.División(D, d)\n")

opcion=input("Escriba la inicial de la operación que desea realizar-->").lower()

if opcion=='s':
    print("SUMA")
    num1=float(input("Numero 1-->"))
    num2=float(input("Numero 2-->"))
    resultado=num1+num2
    print(f"El resultado de la suma de {num1:.0f} + {num2:.0f} es: {resultado:.0f}")

elif opcion=='r':
    print("RESTA")
    num1=float(input("Numero 1-->"))
    num2=float(input("Numero 2-->"))
    resultado=num1-num2
    print(f"El resultado de la resta de {num1:.0f} - {num2:.0f} es: {resultado:.0f}")

elif opcion=='p' or opcion=='m':
    print("MULTIPLICACION")
    num1=float(input("Numero 1-->"))
    num2=float(input("Numero 2-->"))
    resultado=num1*num2
    print(f"El resultado de la multiplicacion de {num1:.0f} * {num2:.0f} es: {resultado:.0f}")

elif opcion=='d':
    print("DIVISION")
    num1=float(input("Numero 1-->"))
    num2=float(input("Numero 2-->"))
    resultado=num1/num2
    print(f"El resultado de la división de {num1} / {num2} es: {resultado}")

else:
    print("Escriba una opción válida no sea imbécil...")