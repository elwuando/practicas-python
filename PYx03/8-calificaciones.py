# Crea una función analizar_calificaciones(calificaciones)
# que reciba un diccionario con alumnos y sus notas
# (ej: {"Ana": 4.5, "Luis": 3.7} ) y devuelva:
calificaciones = {
    'Ana': [2.5, 3.0, 4.8, 2.1, 5.0],
    'Luis': [5.0, 1.0, 4.0, 3.3, 4.2, 3.1]
}


# Recibe como parametro el diccionario
def analizar_calificaciones(calificaciones):
    suma = 0

    for alumno, notas in calificaciones.items():
        sumatoria = len(notas)
        for numero in notas: 
            suma += numero
            promedio = suma / sumatoria
            if promedio >= 3.0:
                return 0

resultado = analizar_calificaciones(calificaciones)
print(calificaciones)



respuesta = {
    'Ana': {
        'promedio': 0,
        'aprobado': True 
    },
    'Luis': {
        'promedio': 0,
        'aprobado': False
    }
}
