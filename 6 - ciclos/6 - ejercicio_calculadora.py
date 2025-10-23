print('***** CALCULADORA *****')

i = False
while not i:
    print('''
OPERACIONES QUE PUEDES REALIZAR:
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Salir''')
    seleccion = int(input('Seleccione una opcion del menu: '))
    numero1 = float(input('Ingrese el primer numero: '))
    numero2 = float(input('Ingrese el segundo numero: '))

    if seleccion == 1:
        resultado = numero1 + numero2
        print('________________________________________________')
        print(f'El resultado de la suma es: {resultado:.2f}')
        print('________________________________________________')
    elif seleccion == 2:
        resultado = numero1 - numero2
        print('________________________________________________')
        print(f'El resultado de la resta es: {resultado:.2f}')
        print('________________________________________________')
    elif seleccion == 3:
        resultado = numero1 * numero2
        print('________________________________________________')
        print(f'El resultado de la multiplicacion es: {resultado:.2f}')
        print('________________________________________________')
    elif seleccion == 4:
        resultado = numero1 / numero2
        print('________________________________________________')
        print(f'El resultado de la division es: {resultado:.2f}')
        print('________________________________________________')
    elif seleccion == 5:
        i = True
        print('Hasta pronto.')
    else:
        print('Opcion invalida. Seleccione una de las opciones del menu.')

