print('***** Suma con argumentos varibales *****')

# Funcion sumar que acepta argumentos variables.
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Llamamos a la funcion sumar
resultado = sumar(1, 2, 3, 4, 5, 7)
print(f'La suma total es de: {resultado}')

