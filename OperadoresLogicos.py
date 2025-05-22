#permite construir expresiones logicas, se obtiene como resultado booleanos
#and
#or
#not

d=13
e=23
r=12
t=10

logico=((d>e)or(r<t))
print(logico)

#usando el not cambia el valor del booleano al contrario
logico=not((d>e)or(r<t))
print(logico)

logico=((d>e)and(r<t))
print(logico)

#combinando
a=10
b=12
c=13
d=10

resultado=((a>b)or(a<c))and((a==c)or(a>=b))
print(resultado)
