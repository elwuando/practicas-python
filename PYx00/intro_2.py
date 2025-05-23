# Escribe un programa que reciba un numero y diga si es par o impar.
numero = 12
residuo = numero % 2
if residuo == 1:
    print('\nEl numero es impar')
elif residuo == 0:
    print('\nEl numero es Par')
else:
    print('\nEsa validacion no esta habilitada')
