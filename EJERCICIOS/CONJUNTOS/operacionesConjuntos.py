#Operaciones con conjuntos

a={1,2,3}
b={2,3,5}

#Union de conjuntos

c=a | b

print(c)

#Insercion de ocnjuntos
c=a & b
print(c)

#Diferencia
c=b - a
print(c)

#Diferencia simetrica: están en A y B pero no en ambos
c=a ^ b
print(c)

#Determinar si un conjunto es subconjunto de otro
a={1,2,3}
b={3,4,5}
c={1,2,3,4,5}

print(a.issubset(c)) #Es A es un subconjunto de C?
print(b.issubset(c)) #Es B es un subconjunto de C?
print(c.issuperset(a)) #Es C el superconjunto de A?

#Conjunto disconexos (que no comparten ningun elemento)
print(a.isdisjoint(b))

#Conjuntos inmutables
a=frozenset({1,2,3}) #Volvemos el conjunto A inmutable (No se puede MODIFICAR(como una tupla))
b={3,4,5}
c={1,2,3,4,5}


