print('***** SISTEMA DE INVENTARIO ******')

productos = [{'id': 1, 'nombre':'camisa', 'precio':19.99, 'cantidad':50}, {'id': 2, 'nombre':'Pantalon', 'precio':59.99, 'cantidad':15}]

def mostrar_inventario(imprimir_productos):
    print('\n')
    for imprimir in imprimir_productos:
        print(f'Id: {imprimir.get('id')}, Nombre: {imprimir.get('nombre')}, Precio: ${imprimir.get('precio')}, Cantidad: {imprimir.get('cantidad')}.')

def agregar_inventario():
    id = int(input('ID: '))
    nombre = input('Nombre del producto: ')
    precio = float(input('Precio del producto: '))
    cantidad = int(input('Cnatidad de productos: '))
    producto = [id, nombre, precio, cantidad]
    return producto

def buscar_produto_id():
    print('----- BUSCAR PRODUCTO POR ID ------')
    id_buscar = int(input('Ingresar el id a buscar: '))
    for producto in productos:
        if producto.get('id') == id_buscar:
            print('\nInformacion del producto encontrado: ')
            print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')}, Precio: ${producto.get('precio')}, Cantidad: {producto.get('cantidad')}.')


opcion_menu = 0
while opcion_menu != 4:
    print('\n----- MENU -----')
    print('     1. Mostrar Inventario')
    print('     2. Agregar nuevo producto')
    print('     3. Buscar producto por ID')
    print('     4. Salir')
    opcion_menu = int(input('Proporcionar una opcion (1-4): '))
    
    if opcion_menu == 1:
        mostrar_inventario(productos)

    elif opcion_menu == 2:
        productos.append(agregar_inventario())

    elif opcion_menu == 3:
        buscar_produto_id()

    elif opcion_menu == 4:
        print('\nMuchas gracias. Regrese pronto.')    

    else:
        print('\nLa opcion seleccionada no es valida, seleccion opcion correcta. ')

