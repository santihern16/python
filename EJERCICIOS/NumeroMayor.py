#Pedir 3 numeros y determinar cual es el mayor

num1=int(input("Primer numero-->"))
num2=int(input("Segundo numero-->"))
num3=int(input("Tercer numero-->"))

if num1>=num2 and num1>=num3:
    print(f"{num1} es mayor")
elif num2>=num1 and num2>=num3:
    print(f"{num2} es mayor")
elif num3>=num1 and num3>=num2:
    print(f"{num3} es mayor")