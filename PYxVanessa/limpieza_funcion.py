# Implementacion y mejora en el filtrado numeros celulares para
# el envio de campañas publicitarias por medio de SMS y whatsapp.

import re

clientes = [
    {"id": "cliente001", "nombre": "Andrea López", "telefono": "300-456-7890"},
    {"id": "cliente002", "nombre": "Carlos Pérez", "telefono": "(+57) 315 000 0000"},
    {"id": "cliente003", "nombre": "Mariana Díaz", "telefono": "31O-222-3344"},  # letra O en lugar de 0
    {"id": "cliente004", "nombre": "Luis Herrera", "telefono": "301@123@4567"},
    {"id": "cliente005", "nombre": "Sofía Gómez", "telefono": "12345"},
    {"id": "cliente006", "nombre": "Daniel Rodríguez", "telefono": "N/A"},
    {"id": "cliente007", "nombre": "Camila Torres", "telefono": "+57_300_999_1111"},
    {"id": "cliente008", "nombre": "Julián Ríos", "telefono": "300.123.4567"},
    {"id": "cliente009", "nombre": "Laura Martínez", "telefono": "Telefono no disponible"},
    {"id": "cliente010", "nombre": "Sebastián Cruz", "telefono": "00300-4455-667"},
    {"id": "cliente011", "nombre": "Valentina Ruiz", "telefono": "+57300ABC5678"},
    {"id": "cliente012", "nombre": "Mateo Ramírez", "telefono": "+57-@@@-####"},
    {"id": "cliente013", "nombre": "Isabella Moreno", "telefono": "+57 (315) 888-7777"},
    {"id": "cliente014", "nombre": "Tomás Vega", "telefono": "31 5555"},
    {"id": "cliente015", "nombre": "Luciana Castro", "telefono": "☎️ 3001234567"},
    {"id": "cliente016", "nombre": "Simón Méndez", "telefono": "300 123 456 789"},  # demasiado largo
    {"id": "cliente017", "nombre": "Gabriela León", "telefono": "+57-300-0000-0000"},
    {"id": "cliente018", "nombre": "Emilio Navarro", "telefono": "___"},
    {"id": "cliente019", "nombre": "Renata Flores", "telefono": "300-300-300"},
    {"id": "cliente020", "nombre": "Diego Cárdenas", "telefono": "null"},
    {"id": "cliente021", "nombre": "Natalia Romero", "telefono": "+57 300x999x888"},
    {"id": "cliente022", "nombre": "Juan Camilo", "telefono": "abc123"},
    {"id": "cliente023", "nombre": "Esteban Silva", "telefono": "😶"},
    {"id": "cliente024", "nombre": "Juliana Salas", "telefono": "+57 310-000-0000"},
    {"id": "cliente025", "nombre": "Felipe García", "telefono": " "},
    {"id": "cliente026", "nombre": "Diana Ortiz", "telefono": "+57 3a0 123 4567"},
    {"id": "cliente027", "nombre": "Camilo Páez", "telefono": "311\\444\\7777"},
    {"id": "cliente028", "nombre": "Manuela Rivas", "telefono": "+57-311-@@@-@@@@"},
    {"id": "cliente029", "nombre": "Ricardo Méndez", "telefono": "321-0000"},
    {"id": "cliente030", "nombre": "Paula Castaño", "telefono": "3109990000"}
]

# Recibe como parametro una lista
def limpiar_numeros_celulares(clientes):

    lista_corregida = []
    lista_validos = []
    lista_descartados = []

    for cliente in clientes:

        numero = cliente.get('telefono', None)
        if numero is None:
            lista_descartados.append((cliente,'Fue descartado por nos poseer telefono'))
            continue

        numero = re.sub(r'\D', '', str(numero))

        if numero.startswith('00'):
            numero = numero[2:]

        if numero.startswith('0'):
            numero = numero[1:]

        if numero.startswith('57'):
            numero = numero[2:]

        if len(numero) != 10:
            lista_descartados.append((cliente,'Fue descartado por no tener 10 digitos'))
            continue

        if not numero.startswith('3'):
            lista_descartados.append((cliente, 'Fue descartado por no empezar con el prefijo 3'))
            continue
        else:
            if cliente['telefono'] == numero:
                lista_validos.append(cliente)

        if cliente['telefono'] != numero:
            cliente['telefono'] = numero
            lista_corregida.append(cliente)

    return lista_validos, lista_corregida, lista_descartados

lista_validos, lista_corregida, lista_descartados = limpiar_numeros_celulares(clientes)

print(lista_validos)
print(len(lista_validos))

print(f'\n{lista_corregida}')
print(len(lista_corregida))

print(f'\n{lista_descartados}')
print(len(lista_descartados))
