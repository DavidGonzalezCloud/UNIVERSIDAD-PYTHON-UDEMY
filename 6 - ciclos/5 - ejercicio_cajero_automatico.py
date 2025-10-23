print('***** APLICACION DE CAJERO AUTOMATICO *****')

# VARIABLES
saldo_actual = 1000.00
seleccion = 0

while seleccion != 4:
    print('''
Operaciones que puede puedes realizar:
    1. Consulta de Saldo
    2. Retirar efectivo
    3. Depositar efectivo
    4. Salir''')
    seleccion = int(input('Seleccione una opcion valida: '))

    if seleccion == 1:
        print('_______________________________________')
        print(f'\nSaldo actual es: ${saldo_actual:.2f}')
        print('_______________________________________')
    elif seleccion == 2:
        saldo_retirar = float(input('Saldo retirar: '))
        if saldo_actual >= saldo_retirar:
            saldo_actual -= saldo_retirar
            print('_______________________________________')
            print(f'\nSaldo actual es: ${saldo_actual:.2f}')
            print(f'Saldo retirado es: ${saldo_retirar}')
            print('_______________________________________')
        else:
            print('_______________________________________')
            print('Los fondos son nsuficientes.')
            print('_______________________________________')
    elif seleccion == 3:
        saldo_depositar = float(input('Saldo depositar: '))
        saldo_actual += saldo_depositar
        print('_______________________________________')
        print(f'\nEl saldo depositado es: ${saldo_depositar:.2f}')
        print(f'El nuevo saldo es: ${saldo_actual:.2f}')
        print('_______________________________________')
    elif seleccion == 4:
        print('_______________________________________')
        print('\nMuchas gracias. Vuelva pronto')
        print('_______________________________________')
    else:
        print('_______________________________________')
        print('\nOpcion invalida, seleccione una de las opciones del menu.')
        print('_______________________________________')



