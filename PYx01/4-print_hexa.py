# Escribe un programa que imprima todos los números del 0 al 98 en decimal
# y en hexadecimal (como en el siguiente ejemplo)

for numero in range(0, 99):
    print(float(numero), '=', hex(numero))
