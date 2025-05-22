#Pedir 2 numeros y determinar cual es par

num1=int(input("Primer numero: "))
num2=int(input("Segundo numero: "))

if num1%2==0 and num2%2==0:
    print("Ambos numeros son pares")
elif num1%2==0 and num2%2!=0:
    print(f"{num1} es par")
elif num1%2!=0 and num2%2==0:
    print(f"{num2} es par")
else:
    print("Ambos numeros son impares")