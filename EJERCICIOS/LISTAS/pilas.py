#Simulando pilas

print("Pila inicial")
pilas=[1,2,3,4]
print(pilas)

print("Agregando elementos...")
pilas.append(5)
pilas.append(6)
print(pilas)

print("Sacando elementos...")
n=pilas.pop()
print(pilas)
print("Se ha sacado el elemento {}".format(n))