#preguntar al usuario 2 numeros para multiplicar.

num1=int(input("Digite el primer numero que desea multiplicar: "))
num2=int(input("Digite el segundo numero que desea multiplicar: "))

resultado=num1*num2

if(resultado>=100):
    print(f"El resultado es {resultado}, lo cual es mayor o igual de 100")
else:
    print("El resultado es {}, lo cual es menor que 100".format(resultado))