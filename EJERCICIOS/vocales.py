#Pedir un caracter e indicar si es una vocal o no

#TRANFORMAR UN CARACTER A MINUSCULA
caracter=input("Digite una letra: ").lower()
#caracter=caracter.lower()
#caracter=input("Digite una letra: ").upper() /Transformar a mayúscula

if caracter=='a' or caracter=='e' or caracter=='i' or caracter=='o' or caracter=='u':
    print(f"{caracter} es una vocal")
else:
    print(f"{caracter} no es ninguna vocal")