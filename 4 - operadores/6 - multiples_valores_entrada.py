print('*** RECIBIR VALORES MULTIPLES CON UNA ENTRADA DEL USUARIO ***')

nombre, apellido = input('Ingrese su nombre y apellido separados por una coma: ').split(',')
print(f'El nombre: {nombre.strip()}')
print(f'El apellido: {apellido.strip()}')
