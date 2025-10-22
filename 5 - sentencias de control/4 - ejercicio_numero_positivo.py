print('*** REVISION DE VALOR POSITIVO ***')

# SOLICITAMOS EL NUMERO TIPO ENTERO
numero = int(input('Ingresa un numero: '))

if numero > 0:
    print('El numero es positivo.')
elif numero < 0:
    print('El numero es negativo')
else:
    print('El numero es 0')