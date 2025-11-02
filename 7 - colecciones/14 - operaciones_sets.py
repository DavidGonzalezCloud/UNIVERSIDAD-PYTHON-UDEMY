print('***** OPERACIONES CON SET *****')

a = {1,2,3,4}
b = {3,4,5,6}

# UNIR DOS SETS
union = a | b
print(f'Union de a y b: {union}')

# INTERSECCION DE DOS SETS (VALORES QUE SE REPITEN)
interseccion = a & b
print(f'Interseccion de a y b: {interseccion}')

# DIFERENCIA DE A - B
# AL CONJUNTO A SE LE QUITAN LOS VALORES REPETIDOS DEL CONJUNTO B
# LOS DEMAS VALORES DEL CONJUNTO B NO SE AGREGAN

diferencia = a - b
print(f'Diferencia de a y b: {diferencia}')
