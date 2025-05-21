# Imagina que tú y yo tenemos un acuerdo: cada día uno diferente paga
# el desayuno, alternando días pares e impares del mes.
#
# Completa el código fuente para que, al ingresar el número del día del mes,
# el programa indique quien paga hoy.

dia = int(input('¿Qué día del mes es hoy? (1-31): '))

residuo = dia % 2
if dia >= 1 and dia <= 31:
    if residuo == 1:
        print('\nHoy el desayuno lo paga Santiago')
    elif residuo == 0:
        print('\nHoy el desayuno lo paga Arias')
else:
    print('\nEsa validacion no esta habilitada')
