# Escribe un programa que imprima todas las posibles combinaciones
# diferentes de dos dígitos.

for numero in range(10):
    for combinacion in range(numero + 1, 10):
        if numero != 8 or combinacion != 9:
            print(f"{numero}{combinacion}", end=", ")
        else:
            print(f"{numero}{combinacion}")
