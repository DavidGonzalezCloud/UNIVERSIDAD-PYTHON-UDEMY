print('\n***** CALCULO DE POTENCIA DE UN NUMERO *****\n')

def calculo_potencia(numero, exponente):
    if exponente == 0:
        return 1
    else:
        potencia_parcial = numero * calculo_potencia(numero, exponente - 1)
        return potencia_parcial

# solicitamos el numero y luego la potencia

a = int(input('Ingrese el numero base: '))
b = int(input('Ingrese la potencia para el numero base: '))

# Llamamos a la funcion
resultado_final = calculo_potencia(a,b)

# Imprimimos resultado
print(resultado_final)