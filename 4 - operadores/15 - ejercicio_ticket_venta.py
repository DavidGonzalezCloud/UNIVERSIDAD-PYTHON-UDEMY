print('*** GENERACION DE TICKET DE VENTA ***')

# SOLICITAR PRECIO DE LOS PRODUCTOS
precio_leche = float(input('Precio de la leche: '))
precio_pan = float(input('Precio de la pan: '))
precio_lechuga = float(input('Precio de la lechuga: '))
precio_platanos = float(input('Precio de los platanos: '))

# APLICAMOS UN DESCUENTO
porcentaje_descuento = float(input('Descuento a aplicar: '))

# CALCULAMOS EL SUBTOTAL SIN IMPUESTOS
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

#CALCULAMOS DESCUENTO ANTES DE IMPUESTOS
porcentaje_descuento /= 100
monto_descuento = subtotal * porcentaje_descuento
subtotal_descuento = subtotal - monto_descuento

# CALCULO DEL IMPUESTO
impuesto = subtotal_descuento * 0.13

# CALCULO DE PRECIO FINAL
total = subtotal_descuento + impuesto

print(f'''\n*** FACTURA FINAL ***\n

Lista de productos:
1 - Leche               ${precio_leche:.2f}
2 - Pan                 ${precio_pan:.2f}
3 - Lechuga             ${precio_lechuga:.2f}
4 - Platanos            ${precio_platanos:.2f}

Subtotal:               ${subtotal:.2f}
descuento:              ${monto_descuento:.2f}
subtotal con descuento: ${subtotal_descuento:.2f}
Impuesto:               ${impuesto:.2f}
Total:                  ${total:.2f}

''')
