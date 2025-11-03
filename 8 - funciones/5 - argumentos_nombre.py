print('***** FUNCION CON ARGUMENTOS POR NOMBRE *****')

def imprimir_persona(nombre, apellido, edad):
    print(f'Nombre: {nombre}')
    print(f'Apellido: {apellido}')
    print(f'Edad: {edad}')

# Primero llamamos la funcion pasando los argumentos de manera posicional
imprimir_persona('Juan', 'Gomez', 18)

# Llamar la funcion usando argumentos por nombre
imprimir_persona(nombre='Carlos', apellido='Lopez', edad=28)

# Llamar la funcion usando argumentos por nombre pero intercambiando el orden
imprimir_persona(edad=38, apellido='Santa', nombre='Juan')

#Agregamos valores por default a los parametros
def imprimir_persona2(nombre, apellido='', edad=0):
    print(f'Nombre: {nombre}')
    print(f'Apellido: {apellido}')
    print(f'Edad: {edad}')

# Argumentos con valores por default
imprimir_persona2(nombre='David',)