#intercambiar los valores de 2 variables

a=input("a-->")
b=input("b-->")

print(f"El valor de a es {a}")
print(f"El valor de b es {b}")

#intercambiando variables
a, b= b, a

print("INTERCAMBIANDO...")

print(f"El nuevo valor de a es {a}")
print(f"El nuevo valor de b es {b}")