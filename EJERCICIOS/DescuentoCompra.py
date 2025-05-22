#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuánto deberá pagar finalmente por su compra.

valor=float(input("Valor de la compra-->"))
print("Valor sin descuento-->${:.2f}".format(valor))

descuento=valor*0.15
valorDescuento=valor-descuento

print("Valor con descuento-->${:.2f}".format(valorDescuento))