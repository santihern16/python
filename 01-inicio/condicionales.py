#Condicionales

numero=int(input("Digite un numero entero: "))

if numero>0: 
    print("El numero es positivo.")
elif numero==0:
    print("El numero es 0")
else:
    print("El numero es negativo.")

print("fin del condicional")

print("\nCondicionales ternarios")

edad = 17
mensaje = "Es mayor de edad" if edad >=18 else "Es menor de edad"
print(mensaje)