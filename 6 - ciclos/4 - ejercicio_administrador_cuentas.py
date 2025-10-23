print('*** Sistema de administracion de cuentas ***')

contador = 1
seleccion = 0

while contador == 1:
    print('''
    Menu:
        1. crear cuenta
        2. Eliminar cuenta
        3. Salir''')
    seleccion = int(input('Selecciona una opcion: '))
    if seleccion == 1:
        print('\nCreando una nueva cuenta')
    elif seleccion == 2:
        print('\nEliminando cuenta')
    elif seleccion == 3:
        print('\nSaliendo del sistema. Hasta pronto')
        contador = 0
    else:
        print('\nOpcion invalida, seleccione una opcion valida')





