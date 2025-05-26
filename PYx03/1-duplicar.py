# Dada una lista de números del 1 al 10, crea una nueva lista
# donde cada número esté duplicado (ej: 2, 4, 6)

lista_numeros = [numero for numero in range(1, 11)]
print(lista_numeros)

lista_numeros = [numero*2 for numero in lista_numeros]
print(lista_numeros)
