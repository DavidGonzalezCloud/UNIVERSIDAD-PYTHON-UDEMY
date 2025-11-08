print('***** IMPRIMIR DEL 1 AL 5 DE FORMA RECURSIVA *****')

# DEFINIR LA FUNCION RECURSIVA

def funcion_recursiva(numero):
    # Caso base
    if numero == 1:
        print(numero, end=" ")
    else:
        #Caso recursivo
        funcion_recursiva(numero-1)
        print(numero, end=" ")

# Solicitamos numero y llamamos a la funcion

numero = int(input('Ingrese un numero entero: '))
funcion_recursiva(numero)