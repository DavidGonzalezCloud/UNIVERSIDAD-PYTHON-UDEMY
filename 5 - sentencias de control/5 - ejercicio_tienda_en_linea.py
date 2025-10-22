print('*** TIENDA EN LINEA ***')

# SOLICITUD DE INFORMACION
monton_compra = float(input('ingresa el monton compra: '))
tiene_membresia = str(input('Tiene membresia (si/no): '))

if monton_compra > 1000 and str(tiene_membresia).strip().lower() == 'si':
    print('El descuento aplicable a esta compra es de 10%.')
    descuento = 0.1
elif monton_compra < 1000 and str(tiene_membresia).strip().lower() == 'si':
    print('El descuento aplicable para miembros es de 5%.')
    descuento = 0.05
else:
    print('Ya que la compra es menor a $1000 o no es miembre no aplica a descuentos.')
    descuento = 0

monto_descuento = monton_compra * descuento
monto_final = monton_compra - monto_descuento
print(f'Monto de la compra:     ${monton_compra:.2f}')
print(f'Monto de descuento:     ${monto_descuento:.2f}')
print(f'Monto final:            ${monto_final:.2f}')
