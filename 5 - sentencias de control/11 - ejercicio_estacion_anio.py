print('----- IDENTIFICADOR DE ESTACION DEL AÑO -----')

print('''
MESES DEL AÑO
1 - ENERO
2 - FEBRERO
3 - MARZO
4 - ABRIL
5 - MAYO
6 - JUNIO
7 - JULIO
8 - AGOSTO
9 - SEPTIEMBRE
10 - OCTUBRE
11 - NOVIEMBRE
12 - DICIEMBRE
''')

# Solicitamos la eleccion del mes del anio con un numero
mes = int(input('Ingrese el numero de meses en el que se encuentra: '))

if mes == 1 or mes == 2 or mes == 12:
    print('La estacion del año es invierno')
elif mes == 3 or mes == 4 or mes == 5:
    print('La estacion del año es primavera')
elif mes == 6 or mes == 7 or mes == 8:
    print('La estacion del año es verano')
elif mes == 9 or mes == 10 or mes == 11:
    print('La estacion del año es otoño')
else:
    print('El mes del año ingresado es incorrecto.')
