'''
2. Descuento en medicinas
Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia
(cargar por teclado el precio de ese medicamento) sabiendo que todos los medicamentos
tienen un descuento del 35%. Mostrar el precio actual, el monto del descuento y el monto final
a pagar.
'''
print("LAS MEDICINAS TIENEN UN 35% DE DESCUENTO HOY")
precio=float(input("Precio de la medicina-->"))

descuento=precio*0.35
precioFinal=precio-descuento

print(f"Precio de la medicina: ${precio}")
print(f"Descuento: ${descuento}")
print(f"Precio final a pagar: ${precioFinal}")