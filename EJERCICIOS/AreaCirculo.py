#calcular el radio de la circunferencia

#importamos el modulo matematico en el que se encuentra el numero PI
import math

radio=float(input("Digite el radio de la circunferencia: "))

area=math.pi*radio**2
longitud=2*math.pi*radio
#para que el resultado muestre solo 2 decimales ponemos :.nf
print(f"El area es: {area:.3f}")
print("La longitud de la circunferencia es: {:.3f}".format(longitud))