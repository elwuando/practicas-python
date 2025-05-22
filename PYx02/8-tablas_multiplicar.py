# Debes repasar las tablas de multiplicar del 1 al 5.
# Haz un programa que te permita ver cada tabla de multiplicar una por una.

opcion = ''

for tabla_multiplicacion in range(1, 6):
    while opcion != 'no':
        opcion = input('¿Deseas ver la siguiente tabla?: ').lower()
        if opcion == 'si':
            for numero in range(1, 11):
                tablas = tabla_multiplicacion * numero
                print(f'{tabla_multiplicacion}*{numero}={tablas}')
            break
        elif opcion == 'no':
            print('Programa finalizado')
        else:
            print('la opcion ingresada no es valida, Vuelve a intentarlo')
