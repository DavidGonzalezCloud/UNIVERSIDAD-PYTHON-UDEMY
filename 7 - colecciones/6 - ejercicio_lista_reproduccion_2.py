print('***** PLAYLIST DE CANCIONES *****')
print()

# CREAMOS LA LISTA VACIA
lista_reproduccion = []

# SOLICITAMOS AL USUARIO EL NUMERO DE CANCIONES PARA LA PLAYLIST
numero_canciones = int(input('Ingrese el numero de canciones en la lista: '))

# ITERAMOS CADA ELEMENTO DE LA LISTA PARA AGREGAR UN NUEVO ELEMENTO
for indice in range(numero_canciones):
    cancion = input(f'Ingrese el cancion {indice + 1}: ')
    lista_reproduccion.append(cancion)

# MOSTRAR LA LISTA ITERANDO ELEMENTOS
lista_reproduccion.sort()
print()
for cancion in lista_reproduccion:
    print(f'-{cancion}')