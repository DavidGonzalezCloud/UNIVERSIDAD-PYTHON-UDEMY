# Creamos una lista
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Modificar los elementos de una lista
mi_lista[0] = 10
print(mi_lista)

# Agregar un nuevo elemento al final de la lista
mi_lista.append(6)
print(mi_lista)

# Anadir un nuevo elemento en un indice especifico
mi_lista.insert(2, 11)
print(mi_lista)

# Eliminar elementos de una lista
# Usando el metodo remove
mi_lista.remove(11) #se elimina el valor 11 de la lista
print(mi_lista)

# Removemos por indice con el metodo pop
mi_lista.pop(0)
print(mi_lista)

# Eliminar usando la palabra del
del mi_lista[8]
print(mi_lista)

