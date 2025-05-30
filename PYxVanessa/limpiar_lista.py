# Necesitamos una función en Python que reciba una lista de números
# de contacto y devuelva una nueva lista con la mayor cantidad posible
# de números válidos y corregidos, listos para usarse en campañas de
# comunicación como por ejemplo WhatsApp y SMS.
import re

lista_cruda = [
    " 3001234567 ", "300123456", "03101234567", "+57 3101234567", "0057-320-9998888",
    "310abc123456", "310 123 4567", "12345", "57 300 222 5733", "320.999.8888",
    "+573101234567", "310.123.4567", "300 123 4567", "+57-315-111-2222", "0057 301 333 4444",
    "abc3101234567", "3211234567", " 0057310123456 ", "3151112222", "+57 321 321 3210",
    "00300 123 4567", "571231234567", "+573001234567", "300.123.4567", "57-300-999-7777",
    "310-123-4567", "312.555.6789", " 00573203333444", "57-311-666-7777", "+57 3116667777",
    "300-abc-4567", "57+3009991111", "3100000000", "+57 3010000000", "301-000-0000",
    "3001234567", "3201234567", "0057300123457", "3149999999", "300.123.4567",
    "3001234567", "0057310123456", "3101234567", "57 320 123 4567", "300-000-0000",
    "003003003003", "300@123#4567", "   ", "0000000000", "320123456"
]


# Recibe como parametro una lista
def limpiar_numeros_celulares(lista_cruda):
    lista_valida = []

    for valor in lista_cruda:
        numero = str(valor)
        numero = re.sub(r'\D', '', numero)
        
        if  numero.startswith('00'):
            numero = numero[2:]
        
        if  numero.startswith('0'):
            numero = numero[1:]

        if numero.startswith('57'):
            numero = numero[2:]
        
        if len(numero) != 10:
            continue

        if len(numero) == 10 and numero.startswith('3'):
            lista_valida.append(numero)

    return lista_valida


lista_valida = limpiar_numeros_celulares(lista_cruda)
print(lista_valida)
print(len(lista_valida))
