print('\n***** FACTORIAL DE UN NUMERO *****\n')

def factorial_numero(numero):
    if numero in (0,1):
        return 1
    else: # Sacando el factorial con funcion recursiva (tambien se puese sacar con el ciclo for)
        factorial_parcial = numero * factorial_numero(numero - 1)
        return factorial_parcial


# SOLICITAR UN NUMERO DE ENTER PARA EL FACOTRIAL
numero_solicitado = int(input('Ingrese un numero entero positivo para sacar el factorial: '))

# LLAMAMOS A LA FUNCION
factorial_final = factorial_numero(numero_solicitado)

#IMPRIMIMOS EL RESULTADO
print(f'El factorial del numero {numero_solicitado} es: {factorial_final}')

