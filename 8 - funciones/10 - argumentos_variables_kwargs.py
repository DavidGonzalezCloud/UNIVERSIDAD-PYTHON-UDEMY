# *args - arguments - tupla
# **kwargs

print('*** Argumentos variables en forma de dict ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

# Llamamos la funcion

superheroe_superpoderes('spiderman', 'instinto Aracnido', edad=17, empresa='marvel')
superheroe_superpoderes('ironman', 'armadura', 'playboy', 'millonario', edad=50, empresa='marvel', posicion='Jefe')


