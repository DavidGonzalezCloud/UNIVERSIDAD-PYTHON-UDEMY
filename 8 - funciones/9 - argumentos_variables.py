print('***** Argumentos Variables *****')

# El parametro *args tiene que ir al final de la llamada del metodo.
def superheroe_superpoderes (superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')

    # Itereamos los super poderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

#Llamar la funcion
superheroe_superpoderes('spiderman', 'Peter Parker', 'Instinto Aragnido', 'Telaraña', 'regeneracion')
superheroe_superpoderes('Ironman', 'Tony Stark', 'Armadura', 'Playboy', 'Millonario')

superheroe_superpoderes('Mi vecino', 'David Gonzalez')
