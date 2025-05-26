from os import system

system("cls")

print("Bucle while")

cont = 0
while cont <= 5:
    print(f"Numero #{cont}")
    cont += 1

#Ejemplo de blucle con break
def print_hello_world_repeatedly(contador):
#    cont = 1
    while True:
        print(f"Hola mundo {contador}")

        if contador == 5:
            break
        contador += 1

print_hello_world_repeatedly(0)

# Ejemplo con continue
# Mostrar los numeros impares

cont = 0
while cont < 10:
    cont += 1

    if cont % 2 == 0:
        continue
    # Continue se salta la interaccion de abajo 👇🏾
    print(cont)

print("\nElse en bucle while")
# Else en bucle while
cont = 0
while cont <= 5:
    print(cont)
    cont += 1
else:
    print("El bucle termina aqui 👇🏾")


# Manejando errores try y except
while True:
    try:
        numero = int(input("Ingrese un numero positivo: "))
        if numero >= 0:
            print(f"El numero es ingresado es {numero}")
            break
        else:
            print("El numero no es positivo, intente nuevamente")
            continue
    except:
        print("Debes introducir un numero valido")