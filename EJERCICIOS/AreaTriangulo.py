'''
3. Área de un triángulo
Desarrolle un programa para calcular el área de un triángulo, cargando por teclado el valor de
la base, pero sabiendo que su altura es igual al cuadrado de la base. (Observar que la altura no
es un dato... sólo se indica la forma de calcularla de acuerdo a la base que sí es un dato).
'''
print("AREA DEL TRIANGULO")
base=float(input("Base-->"))

altura=base**2

area=base*altura

print("El area del triángulo es: {:.2f}".format(area))
