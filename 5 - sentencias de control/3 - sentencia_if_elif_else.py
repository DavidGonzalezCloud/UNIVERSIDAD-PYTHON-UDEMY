print('*** Sentencia IF, ELIF, ELSE ***')

edad = int(input('ingresa tu edad: '))

if edad >= 18:
    print('Eres mayor de edad.')
elif 13 <= edad < 18:
    print('Eres un adolecente.')
else:
    print('Eres menor de edad.')