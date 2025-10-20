# usar metodo find para encontrar indice de subcadena

cadena = 'David Gonzalez'

subcadena_find = 'Gonzalez'
longuitud = len(subcadena_find)

posicion_inicial = cadena.find(subcadena_find)
print(f'posicion de subcadena_find: {posicion_inicial}')
print(f'La longuitud de la subcadena_find es: {longuitud}')
print(f'La posicion final de la subcadena_find es: {posicion_inicial+longuitud}')
print(f'La extraccion de subcadena es: {cadena[posicion_inicial:posicion_inicial+longuitud]}')