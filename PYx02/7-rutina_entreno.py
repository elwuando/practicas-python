# Nuestra rutina de entreno juntos será según el día de la semana.
# Cada día tenemos un entrenamiento propio, completa el código fuente para

dia = input('¿Qué día es hoy?: ').lower()

if dia == 'lunes' or dia == 'miercoles' or dia == 'viernes':
    print('Hoy toca cardio 🏃‍♂️')
elif dia == 'martes' or dia == 'jueves':
    print('Hoy toca pesas 🏋️‍♂️')
elif dia == 'sabado':
    print('Dia libre. ¡Relajate! 😌')
elif dia == 'domingo':
    print('Hoy es domingo. ¡planificacion de la semana y descaso!🛌')
else:
    print('Día no reconocido. Intenta de nuevo.')
