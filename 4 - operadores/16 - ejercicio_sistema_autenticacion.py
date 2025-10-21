print('*** SISTEMA DE AUTENTICACION ***')

usuario_registrado = str('david')
contrasena_registrada = str(123)

usuario_ingresado = str(input('Ingrese su usuario: '))
contrasena_ingresado = str(input('Ingrese su contrasena: '))

validacion_datos = usuario_registrado == usuario_ingresado and contrasena_registrada == contrasena_ingresado

print(f'Los datos son correctos? {validacion_datos}')


