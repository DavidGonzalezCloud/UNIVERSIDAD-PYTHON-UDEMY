print('***** DICCIONARIOS EN PYTHON *****')

# CREAMOS UN DICCIONARIO DE PERSONA CON CLAVE Y VALOR

persona = {
    'nombre': 'David',
    'edad': 32,
    'sexo': 'Masculino',
    'ciudad': 'San Salvador'
}

# ACCEDER A LOS ELEMENTOS DEL DICCIONARIO
print(f'Nombre: {persona["nombre"]}')
print(f'Edad: {persona["edad"]}')
print(f'Sexo: {persona["sexo"]}')
# ACCEDER A LOS ELEMENTOS DEL DICCIONARIO USANDO EL METODO GET
print(f'Ciudad: {persona.get('ciudad')}')


