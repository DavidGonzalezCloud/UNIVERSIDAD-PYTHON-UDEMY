print('**** SISTEMA DE ENVIOS ****')

# CREAMOS LAS CONTASTANTES
envio_nacional = 10
envio_internacional = 20

# SOLICITAR INFORMACION AL CLIENTE
print('Ingrese el numero del destino: '
      '\n1 - Nacional'
      '\n2 - Internacional')
destino = int(input(':'))
peso = float(input('Cuanto es el peso del paquete en kilos: '))

if destino == 1:
    costo_envio = peso * envio_nacional
    destino_txt = 'Nacional'
else:
    costo_envio = peso * envio_internacional
    destino_txt = 'Internacional'


print('----- Costo de envio -----')
print(f'El tipo de envio seleccionado es: {destino_txt}')
print(f'Costo envio: ${costo_envio:.2f}')

