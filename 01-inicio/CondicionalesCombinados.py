#Condicionales combinados
#Calcular si es mayor de edad o no

edad=int(input("¿Cuál es su edad?: "))

if edad>0 and edad<100:
    if edad>=18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
else:
    print("Edad incorrecta")
