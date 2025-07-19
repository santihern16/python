'''
Construir una calculadora con las 4 operaciones aritméticas.
El usuario debe digitar la operacion que desea realizar
'''
def mostrarMenu():
        print("1.Suma\n2.Resta\n3.Multiplicación\n4.División\n5.Salir")

def pedirNumeros():
    try:
        option = int(input("Ingresa una opcion ---> "))
        return option
    except ValueError as e:
        print(f"Error {e}. Ingresa una opcion valida.")
        return 0

print("CALCULADORA ARITMÉTICA\n")

option = 0

while option != 5:
    mostrarMenu()
    option = pedirNumeros()
    
    if option > 5 or option < 1:
        print("Por favor ingresa un numero del 1 al 5.")
        continue
    else:
        if option == 1:
            print("SUMA")
            num1 = float(input("Numero 1-->"))
            num2 = float(input("Numero 2-->"))
            resultado=num1+num2
            print(f"El resultado de la suma de {num1:.0f} + {num2:.0f} es: {resultado:.0f}")

        elif option == 2:
            print("RESTA")
            num1=float(input("Numero 1-->"))
            num2=float(input("Numero 2-->"))
            resultado=num1-num2
            print(f"El resultado de la resta de {num1:.0f} - {num2:.0f} es: {resultado:.0f}")

        elif option == 3:
            print("MULTIPLICACION")
            num1=float(input("Numero 1-->"))
            num2=float(input("Numero 2-->"))
            resultado=num1*num2
            print(f"El resultado de la multiplicacion de {num1:.0f} * {num2:.0f} es: {resultado:.0f}")

        elif option == 4:
            print("DIVISION")
            num1=float(input("Numero 1-->"))
            num2=float(input("Numero 2-->"))
            if num2 == 0:
                print("Error. Division no valida entre 0.")
            else:
                resultado=num1/num2
                print(f"El resultado de la división de {num1} / {num2} es: {resultado}")

        elif option == 5:
            print("Gracias por utilizar la calculadora")
            break