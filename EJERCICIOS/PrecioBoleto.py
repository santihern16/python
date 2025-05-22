'''
7. Precio del boleto
Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia. Para el
cálculo del mismo se debe considerar el monto base (que se cobra siempre), más un valor
extra calculado en base a la cantidad de kilómetros a recorrer: Por cada kilómetro a recorrer
se cobra $0.30 de adicional.

'''

precioBase=10

km=float(input("Duración del viaje en kilómetros (km)-->"))

# Calculating the price of the trip.
precioRecorrido=km*0.30
precioFinal=precioBase+precioRecorrido

# Printing the final price of the trip.
print("El precio total a pagar es: ${:.2f}".format(precioFinal))