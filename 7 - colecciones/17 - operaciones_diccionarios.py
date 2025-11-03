print('***** DICCIONARIOS EN PYTHON *****')

# CREAMOS UN DICCIONARIO DE PERSONA CON CLAVE Y VALOR

persona = {
    'nombre': 'David',
    'edad': 32,
    'sexo': 'Masculino',
    'ciudad': 'San Salvador'
}

# MODIFICAR UN VALOR DEL DICCIONARIO
persona['edad'] = 18

print(persona)
print(f'Le nueva edad es {persona["edad"]}')

# AGREGAR UN NUEVO ELEMENTO
persona['profesion'] = 'ingeniero'
print(persona)

# ELIMINAR ELEMENTO DEL DICCIONARIO
del persona['edad']
print(persona)

# SEGUNDO METODO PARA ELIMINAR ELEMENTO DEL DICCIONARIO
persona.pop('sexo')
print(persona)

# ITERAR ELEMENTOS DE UN DICCIONARIO
for llave, valor in persona.items():
    print(f'La llave es {llave} y es el valor es {valor}')

# OBTENER SOLO LOS VALORES DE LA LLAVE-VALOR
print('\nValores del diccionario: ')
for valor in persona.values():
    print(valor)

# OBTENER SOLO LAS LLAVES DE LA LLAVE-VALOR
print('\nLlaves del diccionario: ')
for llave in persona.keys():
    print(llave)