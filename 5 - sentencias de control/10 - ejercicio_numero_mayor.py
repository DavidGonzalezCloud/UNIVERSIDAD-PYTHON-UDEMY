print("----- SISTEMA DE ELECCION DE NUMERO MAYOR -----")

# SOLICITAR NUMEROS AL USUARIO
numero1 = int(input('Numero 1: '))
numero2 = int(input('Numero 2: '))

# COMPARAMOS LOS NUMERO PARA SABER CUAL ES EL NUMERO MAYOR

if numero1 > numero2:
    print(f'El numero {numero1} es mayor a {numero2}')
else:
    print(f'El numero {numero2} es mayor a {numero1}')