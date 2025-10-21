print('*** VALOR DENTRO DE RANGO ***')

# SOLICITAR VALOR AL USUARIO
valor = int(input('Ingresa un valor entre 0 y 5: '))

# COMPARACION
rango = (0 <= valor <= 5)

print('El valor de ' + str(valor) + 'esta dentro del rango?' + str(rango))