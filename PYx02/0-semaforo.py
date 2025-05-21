# Simula el comportamiento de un semáforo. El usuario debe ingresar
# el color que ve y el programa debe imprimir si puede o no cruzar la calle.

color = input('Ingrese el color del semaforo (rojo,amarillo,verde): ').lower()

if color == 'rojo':
    print('Frena lo antes posible')
elif color == 'amarillo':
    print('Deberias reducir la velocidad')
elif color == 'verde':
    print('No pare\' sigue sigue no pare\' sigue sigue')
else:
    print('no mani, ese color no es valido o '
          'demas que sos virologamente miope :,c')
