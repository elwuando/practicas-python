# Una funcion que reciba un texto y me diga cuantas vocales tiene.

vocales = ['a', 'e', 'i', 'o', 'u'] # Creamos una lista con las vocales

mensaje = input('Ingrese un texto: ').lower()

def contar_vocales(texto):
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    print('El texto tiene', contador, 'vocales')

contar_vocales(mensaje)
