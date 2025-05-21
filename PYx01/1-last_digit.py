# Este programa asignará un número con signo aleatorio a la variable
# número cada vez que se ejecute. Complete el código fuente para
# imprimir el último dígito del número almacenado en la variable.

import random
numero = random.randint(-10000, 10000)
numero_final = str(numero)[-1]
numero_final = int(numero_final)

if numero_final > 5:
    print(f'El ultimo digito de {numero} es {numero_final} y es mayor que 5')
elif numero_final == 0:
    print(f'El ultimo digito de {numero} es {numero_final} y es cero')
elif numero_final < 6 and not 0:
    print(f'El ultimo digito de {numero} es {numero_final}\
         y es menor que 6 y no es 0')
