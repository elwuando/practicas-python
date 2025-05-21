# Este programa asignará un número aleatorio con signo a la variable
# número cada vez que se ejecute. Complete el código fuente para
# imprimir si el número almacenado en la variable es positivo o negativo.

import random
numero = random.randint(-10, 10)

if numero > 0:
    print('El numero es positivo')
elif numero == 0:
    print('El numero es cero')
elif numero < 0:
    print('El numero es negativo')
