print('***** AGENDA DE CONTACTOS *****')

agenda = {
    'Carlos': {
        'telefono': '123456789',
        'email': 'carlos@mail.com',
        'direccion': 'calle principal 123',
    },
    'Maria': {
        'telefono': '987654321',
        'email': 'maria@mail.com',
        'direccion': 'avenida central 123',
    },
    'Pedro': {
        'telefono': '456123789',
        'email': 'Pedro@mail.com',
        'direccion': 'Plaza Mayor 789'
    }
}

# ACCEDER A LOS DATOS DE LOS SUB DICCIONARIOS
print(f'''Informacion de contacto de Maria:
    Telefono: {agenda["Maria"]["telefono"]}
    Email: {agenda["Maria"]["email"]}'
    Direccion: {agenda["Maria"]["direccion"]}
''')

# AGREGAMOS UN NUEVO CONTACTO
agenda['Ana'] = {
    'telefono': '123456789',
    'email': 'ana@mail.com',
    'direccion': 'boulevar el ejercito'
}

print(agenda)

# ELIMINAR UN CONTACTO EXISTENTE
agenda.pop('Carlos')
print(agenda)

#MOSTRAR LOS CONTACTOS DE LA AGENDA
for nombre, valores in agenda.items():
    print(f'''\n***** CONTACTOS EN LA AGENDA *****
    Nombre: {nombre}
        Telefono: {valores['telefono']}
        Email: {valores['email']}
        Direccion: {valores['direccion']}
    ''')

