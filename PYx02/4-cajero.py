# Simula un cajero que permite ver el saldo y retirar dinero.

saldo = 52000000
opcion = ''

while opcion != '3':
    print('\n-|-Menu de opciones-|-\n'
          '1. Ver saldo.\n'
          '2. Retirar dinero.\n'
          '3. Salir.')
    opcion = input('Ingresa una de las tres opciones: ')

    if opcion == '1':
        print(f'\nTu saldo actual es de: ${saldo}')
    elif opcion == '2':
        monto = int(input('Ingrese el monto a retirar: '))
        if monto > saldo:
            print('No tienes suficiente saldo, PONTE A CHAMBEAR')
        else:
            # saldo = saldo - monto
            saldo -= monto
            print(f'Retiro exitoso, tu nuevo saldo es: ${saldo}')
    elif opcion == '3':
        print('Gracias por usar nuestros servicios')
    else:
        print('El valor que ingresaste no es valido, Vuelvelo a intentar.')
