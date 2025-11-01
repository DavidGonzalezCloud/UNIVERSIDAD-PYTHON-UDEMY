print('***** PROMEDIO DE CALIFICACIONES *****')

lista_calificacion = []
sumatoria_calificaciones = 0

# SOLICITAMOS CUANTO ES EL NUMERO DE CALIFICACIONES A EVALUAR
numero_evaluaciones = int(input('Ingrese el numero de calificaciones a evaluar: '))

for indice in range(numero_evaluaciones):
    calificacion = float(input(f'Ingrese la calificacion {indice + 1}: '))
    lista_calificacion.append(calificacion)

print(f'Las calificaciones proporcionadas son:\n{lista_calificacion}')

sumatoria_calificaciones = sum(lista_calificacion)
promedio = sumatoria_calificaciones / numero_evaluaciones
print(f'El promedio de calificaciones es: {promedio}')