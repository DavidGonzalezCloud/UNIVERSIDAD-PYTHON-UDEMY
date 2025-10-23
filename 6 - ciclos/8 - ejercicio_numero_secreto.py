
print('***** ADIVINAR EL NUMERO SECRETO *****')

# GENERAMOS EL NUMERO SECRETO AL AZAR
from random import randint
numero_secreto = randint(1, 50)
numero_intentos = 0

i = False
while not i:
    numero = int(input('Ingresa el numero secreto (entre 1 y 50): '))
    if numero != numero_secreto:
        numero_intentos += 1
        if numero_secreto > numero:
            print('El numero secreto es mayor a el numero ingresado.')
        else:
            print('El numero secreto es menor a el numero ingresado.')

    else:
        print(f'''
        ADIVINASTE EL NUMERO SECRETO: {numero_secreto}
        NUMERO DE INTENTOS: {numero_intentos}
        ''')
        i = True

