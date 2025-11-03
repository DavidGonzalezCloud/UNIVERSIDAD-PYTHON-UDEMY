# Primera forma de usar los modulos
import modulo_sumar

# Segunda forma de usar los modulos
#from modulo_sumar import sumar

print(f'***** FUNCION SUMAR *****')

# PROGRAMA PRINCIAL, LLAMAMOS A LA FUNCION
resultado_suma = modulo_sumar.sumar(5,6)
print(f'El resultado de la funcion sumar es: {resultado_suma}')

