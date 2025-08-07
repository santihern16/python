niveles_amenaza = ('bajo', 'moderado', 'alto', 'critico')

amenaza_actual = "bajo"
print(f"Nivel de amenaza actual: {amenaza_actual}")

if amenaza_actual in niveles_amenaza:
    if amenaza_actual == 'bajo':
        print("Actividad recomendada: Realizar auditorías de seguridad regulares.")
    elif amenaza_actual == 'moderado':
        print("Actividad recomendada: Reforzar la concienciación de los empleados sobre riesgos de Ciberseguridad.")
    elif amenaza_actual == 'alto':
        print("Actividad recomendada: Implementar medidas de seguridad adicionales y revisar accesos.")
    elif amenaza_actual == 'critico':
        print("Actividad recomendada: Activar el protocolo de respuesta a incidentes.")
else:
    print("Selecciona un nivel de amenaza adecuado (bajo, moderado, alto, crítico)")