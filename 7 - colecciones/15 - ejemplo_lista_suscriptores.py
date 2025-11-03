print('***** LISTA DE SUSCRIPTORES *****')

suscriptores = {'luisa@mail.com', 'marcos@mail.com', 'elena@mail.com'}
print(f'Lista de suscriptores iniciales: {suscriptores}')

# VERIFICAMOS SI UN NUEVO SUSCRIPTOR YA ESTA EN LA LISTA
nuevo_suscriptore = 'david@mail.com'
if nuevo_suscriptore in suscriptores:
    print(f'El nuevo suscriptor ya esta en la lista: {nuevo_suscriptore}')
else:
    suscriptores.add(nuevo_suscriptore)
    print(f'El nuevo suscriptor se agrego a la lista de suscriptores: {nuevo_suscriptore}')

print('\nLista de suscriptores actualizada: ')
for email in suscriptores:
    print(email)

# ELIMINAMOS SUSCRIPTOR
suscriptor_eliminar = 'elena@mail.com'
suscriptores.remove(suscriptor_eliminar)

print('\nLista de suscriptores actualizada: ')
for email in suscriptores:
    print(email)

# SABER LA CANTIDAD DE SUSCRIPTORES
print(f'\nLa cantidad de suscriptores actuales es: {len(suscriptores)}')
