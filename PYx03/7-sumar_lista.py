# Escribe una función sumar_lista(lista) que reciba una lista de números
# y devuelva la suma total.

lista = range(1, 11)


def sumar_lista(lista):
    total = 0.0
    for numero in lista:
        total += numero

    return total


resultado = sumar_lista(lista)
print(resultado)
