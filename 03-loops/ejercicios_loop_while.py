###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
num = 10
while num > 0:
    print(num)
    num -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
# 2 + 4 + 6 + 8 + 10 
print("\nEjercicio 2:")
num = 0
suma_pares = 0
while num <= 20:
    if num % 2 == 0:
        suma_pares += num
        print(end="" f"{num} + ")
    num += 1
print(f"\nLa suma de los pares es: {suma_pares}")
# Comprobar resultado: print(sum(range(0, 21, 2)))  # Resultado: 110

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

def calcular_factorial():  
    num = int(input("Ingrese un numero para calcular el factorial: "))
    factorial = 1
    contador = 1

    while contador <= num:
        factorial *= contador
        contador += 1

    print(f"{num}! = {factorial}") 

# calcular_factorial()

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

def check_password():    
    while True:
        passwrd = input("Ingresa tu password: ")
        if len(passwrd) < 8:
            print("Tu password debe tener al menos 8 caracteres, por favor intenta de nuevo")
            continue
        else:
            print("Gracias")
            break
    print(f"Password ingresada correctamente.")

# check_password()

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

def tabla_multiplicar():
    cont = 1
    num = int(input("Digita un numero: "))

    while cont <= 10:
        result = num * cont
        print(f"{num} x {cont} = {result}")
        cont += 1

# tabla_multiplicar()

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

def numeros_primos():
    # Solicita al usuario un número entero positivo
    num = int(input("Introduce un numero entero positivo: "))
    actual = 2  # Comienza desde el primer número primo

    # Itera desde 2 hasta el número ingresado
    while actual <= num:
        es_primo = True  # Suponemos que el número es primo
        divisor = 2

        # Verifica si 'actual' es divisible por algún número menor que él
        while divisor < actual:
            if actual % divisor == 0:
                es_primo = False  # Si es divisible, no es primo
                break
            divisor += 1

        # Si es primo, lo imprime
        if es_primo:
            print(actual)
        actual += 1  # Pasa al siguiente número

numeros_primos()