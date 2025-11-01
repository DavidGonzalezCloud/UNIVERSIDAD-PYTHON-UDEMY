print('***** PLAYLIST DE CANCIONES *****')
print()

# CREAMOS LA LISTA VACIA
lista_reproduccion = []

# EMPEZAMOS A AGREGAR CANCIONES
lista_reproduccion.append('HOTEL CALIFORNIA - EAGLES')
lista_reproduccion.append('STAYING ALIVE - BEE GEES')
lista_reproduccion.append('DREAM ON - AEROSMITH')

# ORDENAR LA LISTA EN ORDEN ALFABETICO
lista_reproduccion.sort()

# MOSTRAMOS LA LISTA
print(f'Lista de reproduccion en orden alfabetico ascendente:\n{lista_reproduccion}')

# ORDENAR LISTA EN ORDEN ALFABATICO DESCENDENTE
lista_reproduccion.sort(reverse=True)
print()
print(f'Lista de reproduccion en orden alfabetico descendente:\n{lista_reproduccion}')

# MOSTRAR LA LISTA ITERANDO ELEMENTOS
lista_reproduccion.sort()
print()
for cancion in lista_reproduccion:
    print(f'-{cancion}')


