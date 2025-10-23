print('***** CREACION Y VALIDACION DE PASSWORD *****')

i = False
while not i:
    password = (input('Ingresa el nuevo password: ')
    longuitud = len(password)

    if longuitud < 6:
        print('El password ingresado debe contener al menos 6 caracteres.')
    else:
        print('El password es valido.')
        i = True

