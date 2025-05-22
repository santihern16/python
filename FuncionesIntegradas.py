n=float("10.5")
print(type(n))

d=int("20")
print(type(d))

cadena=str(10)
print(10)
print(type(cadena))

#convirtiendo valor entero a binario
num=bin(10)
print(num)

#convertir entero a hexadecimal
dec=hex(234)
print(dec)

#convertir binario a entero
binario=int("0b1010", 2) #en base 2
print(binario)

#convertir hexadecimal a entero
hexa=int("0xea", 16)
print(f"El numero en hexadecimal es: {hexa}")

#EJEMPLO
ejemplo=int(input("Ingrese un numero entero para convertirlo a hexadecimal: "))
ejemplo=hex(ejemplo)
print(f"El numero convertido a hexadecimal es: {ejemplo}")

#Valor absoluto
absoluto=abs(-8)
print(f"El numero absoluto de -8 es {absoluto}")

#redondear un numero
redondear=round(5.6)
print(f"El numero redondeado es {redondear}")

#funcion para contar el numero de caracteres de una cadena (len)
nombre=len("Santiago")
print(f"Su nombre tiene {nombre} caracteres")
