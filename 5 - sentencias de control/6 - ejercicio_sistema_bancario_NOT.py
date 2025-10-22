print('*** BIENVENIDO AL SISTEMA BANCARIO ***')

salir_sistema_txt = input('Deseas salir del sistema (Si/No): ')
salir_sistema_bool = salir_sistema_txt.strip().lower() == 'si'


print(salir_sistema_bool)

if not salir_sistema_bool:
    print('Continuamos dentro del sistema')
else:
    print('Salimos del sistema')