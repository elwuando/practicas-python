# Crea una función analizar_calificaciones(calificaciones)
# que reciba un diccionario con alumnos y sus notas
# (ej: {"Ana": 4.5, "Luis": 3.7} ) y devuelva:
calificaciones = {
    'Ana': [2.5, 3.0, 4.8, 2.1, 5.0],
    'Luis': [2.0, 5.0, 2.0, 3.3, 4.2, 3.0],
    'Carlos': [2.0, 1.0, 2.5, 3.3, 3.2, 3.0]
}


# Recibe como parametro el diccionario
def analizar_calificaciones(calificaciones):
    resultado = {}
    aprobados = 0

    for alumno, notas in calificaciones.items():
        suma = 0.0
        sumatoria = len(notas)

        for numero in notas:
            suma += numero

        promedio = suma / sumatoria
        if promedio >= 3.0:
            aprobados += 1

        resultado[alumno] = promedio
    resultado['Aprobados'] = aprobados

    return resultado


resultado = analizar_calificaciones(calificaciones)
print(resultado)
