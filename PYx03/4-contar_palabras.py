# Dada una frase fija (ej: “hola hola mundo esto es Python mundo mundo”),
# crea un diccionario que cuente cuántas veces aparece cada palabra

frase = 'hola hola mundo esto es Python mundo mundo'

palabras = frase.split()
contar = {}

for palabra in palabras:
    if palabra in contar:
        contar[palabra] += 1
    else:
        contar[palabra] = 1

print(contar)
