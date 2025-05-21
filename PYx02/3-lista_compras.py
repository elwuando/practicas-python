# Imagina que vamos de compras al Dollar City.
# Crea una lista de compras con los productos que tú y yo
# necesitamos para el GYM
lista_gym = []
while True:
    producto = input('Ingresa un producto'
                     '(escribe "fin" para finalizar): ').lower()

    if producto == 'fin':
        break
    else:
        lista_gym.append(producto)

for producto in lista_gym:
    print(producto)
