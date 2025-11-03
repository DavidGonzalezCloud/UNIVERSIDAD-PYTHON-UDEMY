print(f'***** OBTENER COORDENADAS X,Y,Z *****')

def obtener_coordenadas():
    x, y, z = 10,20,30
    return x, y, z

# Llamamos la funcion
resultado = obtener_coordenadas()
print(resultado)

# Unpaking de la tupla
x1,y1,z1 = obtener_coordenadas()
print(f'Coordenada x: {x1}, y: {y1}, z: {z1}')