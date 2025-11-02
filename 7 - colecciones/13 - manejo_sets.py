print("***** MANEJO DE SETS ******")
print('')

# CREAR UN CONJUNTO
mi_set = {1,2,3,4,5,4}
print(mi_set)

# AGREGAR ELEMENTOS AL SET
mi_set.add(7)
mi_set.add(6)
print(mi_set)

# AGREGAR UN ELEMENTO REPETIDO
mi_set.add(3)
print(mi_set)

# ELIMIAR UN ELEMENTO DEL CONJUNTO
mi_set.remove(6)
print(mi_set)

# PODEMOS ITERAR LOS ELEMENTOS DEL SET
for elemento in mi_set:
    print(elemento, end=" ")

# VERIFICAR SI UN VALOR EXISTE EN EL SET
print(f'\nExiste el valor de 3 en el set? {4 in mi_set}')
print(f'Existe el valor de 3 en el set? {6 in mi_set}')

# OBTENER LONGUITUD DEL SET

print(f'La longuitud del conjunto es: {len(mi_set)}')

