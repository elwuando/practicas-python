# Realizar una funcion que reciba 4 numeros e imprima el mas grande.

def numero_grande(n1,n2,n3,n4): # Definimos una función con parametros n1,n2,n3,n4.

    if n1 >= n2 and n1 >= n3 and n1 >= n4:
        print(f"\n{n1} es el mas grande") # Entonces n1 es el mayor.
    elif n2 >= n1 and n2 >= n3 and n2 >= n4:
        print(f"\n{n2} es el mas grande") # Entonces n2 es el mayor.
    elif n3 >= n1 and n3 >= n2 and n3 >= n4:
        print(f"\n{n3} es el mas grande") # Entonces n3 es el mayor.
    else:
        print(f"\n{n4} es el mas grande") # Entonces n4 es el mayor.

numero_grande(1, 4, 5, 4) # Agregamos un valor numerico siguiendo el orden de los parametros en el función definida numero_grande.

# Aprobado por challane

