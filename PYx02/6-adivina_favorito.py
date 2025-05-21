# Imagina que estoy pensando un número entre el 1 y el 10,
# y tú debes adivinarlo.

# Cada que ejecutes el programa, pensaré un número diferente.
import random

contador_intentos = 0
intento = ''
numero_favorito = random.randint(1, 10)

while intento != numero_favorito:
    intento = int(input('Ingresa y adivina el numero (entre 1 y 10): '))
    contador_intentos += 1
    if intento != numero_favorito:
        print('No, Intenta de nuevo')
    elif intento == numero_favorito:
        print(f'Muy bien! Has adivinado el numero\nHaz Realizado {contador_intentos} intentos')
        break
