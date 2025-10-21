print('**** CALCULO DE AREA Y PERIMETRO DE UN RECTANGULO')

# SOLICITAR MEDIDAS
alto = float(input('Ingresar el alto del rectangulo en metros: '))
ancho = float(input('Ingresar el ancho del rectangulo en metros: '))

#CALCULO DE AREA
area = alto * ancho

# CALCULO DE PERIMETRO
perimetro = area * 2

print(f'\nEl area del rectangulo es de {area} metros')
print(f'El perimetro del rectangulo es de {perimetro}')