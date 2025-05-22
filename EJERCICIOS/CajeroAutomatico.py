'''
Hacer un programa que simule un cajero automático con un salgo incicial de $1000 
y que contenga el siguiente menú de opciones:

1. Ingresar dinero en la cuenta
2. Retirar dinero en la cuenta
3. Mostrar dinero disponible
4. Salir
'''
from profile import Profile


saldo=1000
print("BIENVENIDO AL CAJERO AUTOMÁTICO")

print("1. Ingresar dinero en la cuenta\n2. Retirar dinero en la cuenta\n3. Mostrar dinero disponible\n4. Salir")

opcion=int(input("Ingrese la opcion que desea realizar: "))

if opcion==1:
    print("SALDO ACTUAL: ${}".format(saldo))
    ingresar=float(input("Cuanto desea ingresar a su cuenta?: $"))
    nuevo_saldo=saldo+ingresar
    print("Usted ha ingresado: ${:.2f}".format(ingresar))
    print("Su nuevo saldo es de: ${:.2f}".format(nuevo_saldo))

elif opcion==2:
    print("SALDO DISPONIBLE: ${}".format(saldo))
    retirar=float(input("Cuanto desea retirar de su cuenta?: $"))
    if (retirar>saldo):
        print("Fondos insuficientes para retirar...")
    else:
        nuevo_saldo=saldo-retirar    
        print("Usted ha retirado: ${:.2f}".format(retirar))
        print("Su nuevo saldo es de: ${:.2f}".format(nuevo_saldo))

elif opcion==3:
    print("SU SALDO ACTUAL ES DE: ${}".format(saldo))

elif opcion==4:
    print("Usted ha salido del cajero. Gracias por utilizar nuestros servicios")

else:
    print("Digite una opción válida...")