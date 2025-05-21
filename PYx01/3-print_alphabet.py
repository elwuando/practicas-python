# Escribe un programa que imprima el alfabeto ASCII, en minúsculas,
# no seguido de una nueva línea.

for numero in range(97, 123):
    if numero != 101 and numero != 113:
        print(chr(numero), end='')
