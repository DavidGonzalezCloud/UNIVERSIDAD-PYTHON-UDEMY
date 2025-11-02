print('***** COMBINACION DE LISTAS Y TUPLAS *****')

# DEFINIR UNA LISTA QUE ALMACENA TUPLAS DE PRODUCTOS

productos = [
    ('P001', "Camiseta", 20.00),
    ('P002', "Jeans", 30.00),
    ('P003', "Sudadera", 40.00),
]

# Imprimimos la informacion de cada producto

precio_total = 0
for producto in productos:
    id, descripcion, precio = producto
    precio_total += precio
    print(f'ID: {id}')
    print(f'Descripcion: {descripcion}')
    print(f'Precio: ${precio}')
    print('')

print(f'El precio total es: {precio_total}')


