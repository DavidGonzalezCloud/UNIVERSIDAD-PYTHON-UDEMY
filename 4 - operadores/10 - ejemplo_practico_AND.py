print('*** SISTEMA DE DESCUENTOS VIP ***')

no_productos_despuesto = 10
cantidad_productos = int(input('Cuantos productos compraste hoy?'))
tiene_mebresia = input('Tienes la membresia de la tienda (Si/No): ')

es_elegible_descuento = cantidad_productos >= no_productos_despuesto and tiene_mebresia.strip().lower() == 'si'

print(f'Tienes acceso al descuento VIP? {es_elegible_descuento}')