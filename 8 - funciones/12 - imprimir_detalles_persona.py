print('***** Imprimir detalles de una persona usando kwargs *****')

# funcion que acepta argumento variables en forma de llave valor

def imprimir_detalle_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

# Llamamos a la funcion
imprimir_detalle_persona(nombre='David', edad=32, apellido='Gonzalez', ciudad='Santa Tecla')
print()
imprimir_detalle_persona(nombre='Ernesto', apellido='Lozano')