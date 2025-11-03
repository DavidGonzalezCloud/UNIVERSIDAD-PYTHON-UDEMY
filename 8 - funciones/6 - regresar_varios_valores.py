print(f'***** REGRESAR UNA TUPLA DE CALORES DESDE UNA FUNCION ****')

# DEFINICION DE LA FUNCION
def persona_mayusculas(nombre, apellido, edad):
    print(f'Esta funcion regresa varios valores (tupla)')
    return nombre.upper(), apellido.upper(), edad

# PROGRAMA PRINCIPAL
nombre, apellido, edad = persona_mayusculas('david', 'gonzalez', 32)
print(f'Resultado: {nombre}, {apellido}, {edad}')