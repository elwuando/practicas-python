# Imagina que estás en un restaurante y quieren
# saber cuánto dejar de propinas.

cuenta = int(input('Ingresa el valor de la cuenta: '))

if cuenta < 50000:
    propina = cuenta / 10
    print(f'Propina sugerida: {propina}')
elif cuenta >= 50000 and cuenta < 100000:
    propina = cuenta / 15
    print(f'Propina sugerida: {propina}')
elif cuenta >= 100000:
    propina = cuenta / 20
    print(f'Propina sugerida: {propina}')
