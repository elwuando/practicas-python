# Diseñar una solución que permita automatizar el registro diario de clientes
# ingresados y ventas realizadas en cada tienda Vanessa, reemplazando el
# método actual que usa libretas y archivos de Excel desordenados.

salida = {}
continuar = 'si'

while continuar == 'si':

    fecha = input('Fecha (Año-Mes-Dia): ')
    clientes = int(input('Numero de clientes: '))
    facturas = int(input('Numero de facturas: '))
    valor = float(input('Valor total de ventas: '))
    almacen = input('Nombre del almacen: ')

    reporte_cliente = {
        'fecha': fecha,
        'clientes': clientes,
        'facturas': facturas,
        'valor_ventas': valor
    }

    if almacen not in salida:
        salida[almacen] = []

    salida[almacen].append(reporte_cliente)

    continuar = input('¿Desea ingresar otro reporte? (si/no): ').lower()

    if continuar != 'si':
        print(f'\n{salida}')

'''salida = {
    'la33': [
        {
            'fecha': '2025-06-04',
            'clientes': 99,
            'facturas': 81,
            'valor_ventas': 1500000
        },
        {
            'fecha': '2025-06-04',
            'clientes': 99,
            'facturas': 81,
            'valor_ventas': 1500000
        },
    ],
    'puerta': [
        {
            'fecha': '2025-06-04',
            'clientes': 99,
            'facturas': 81,
            'valor_ventas': 1500000
        }
    ]
}'''
