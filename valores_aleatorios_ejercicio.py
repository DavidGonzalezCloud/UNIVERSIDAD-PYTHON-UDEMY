# sistema de generador de ID unico

from random import randint

# Ingreso de datos
nombre = input('Ingrese el nombre: ')
apellido = input('Ingrese el apellido: ')
anio_nacimiento = input('Ingrese el anio de nacimiento (YYYY): ')

# creacion de ID unico
ID_nombre = nombre.strip().upper()[0:2]
ID_apellido = apellido.strip().upper()[0:2]
ID_nacimiento = anio_nacimiento[2:]
aleatorio = randint(1000,9999)

ID_unico = ID_nombre + ID_apellido + ID_nacimiento + str(aleatorio)

print(f'\nresultado ID unico: {ID_unico}')