print('**** OPERADOR LOGICO NOT ****')

condicion1 = True
resultado = not condicion1

print(f'Operador logico NOT: {resultado}')

# Revisar si una variable es cadena vacia
nombre = 'z '
es_cadena_vacia = not nombre
print(f'\nLa variable no tiene  ningun valor?: {es_cadena_vacia}')

# Revisar si una variable no tiene ningun valor asignado
variable = None
es_variable_sin_valor = not variable
print(f'\nLa variable NO tiene ningun valor?: {es_variable_sin_valor}')