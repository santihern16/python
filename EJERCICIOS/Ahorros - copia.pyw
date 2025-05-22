'''
Calculo para saber el porcentaje de ahorro mensual según el método 50-40-10
'''

sueldo=float(input("PAGO DE ESTA QUINCENA-->"))

ahorro=sueldo*0.50
gastos=sueldo*0.40
personal=sueldo*0.10

print(f"Sueldo: ${sueldo:.2f}")
print(f"Tienes que ahorrar: ${ahorro:.2f}")
print(f"Gastos para lo necesario: ${gastos:.2f}")
print(f"Para gastar en lo que quieras: ${personal:.2f}")