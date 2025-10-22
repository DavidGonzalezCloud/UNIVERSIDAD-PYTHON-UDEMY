print('*** SISTEMA DE RESERVAS DE HOTEL\n')

# ASIGNAMOS LOS VALORES CONSTANTES
cuarto_sin_vista_mar = 150.50
cuarto_con_vista_mar = 190.50

# SOLICITAR INFORMACION AL CLIENTE
nombre_cliente = str(input('Nombre del cliente: '))
dias_estadia = int(input('De cuantos dias sera la estadia?: '))
cuarto_elejido = str(input('Desea un cuarto con vista al mar (Si/No)?: '))

cuarto_elegido_bool = cuarto_elejido.strip().lower() == 'si'

if cuarto_elegido_bool:
    costo_total = dias_estadia * cuarto_con_vista_mar
    print(f'\nBienvenido {nombre_cliente} a nuestro maravilloso hotel')
    print('Usted eligio cuarto con vista al mar')
    print(f'Costo total: {costo_total}')
else:
    costo_total = dias_estadia * cuarto_sin_vista_mar
    print(f'\nBienvenido {nombre_cliente} a nuestro maravilloso hotel')
    print('Usted eligio cuarto sin vista al mar')
    print(f'Costo total: {costo_total}')