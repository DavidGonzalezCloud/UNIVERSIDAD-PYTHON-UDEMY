print('*** SISTEMA DE PRESTAMOS DE LIBROS ***')

distancia_permitida_KM = 3
tiene_credencial = input('Cuentas con credencial de estudiante (si/no)?:')
distancia_biblioteca_km = int(input('a cuantos km vives de la biblioteca?:'))

es_elegible_prestamo = tiene_credencial.strip().lower() == 'si' or distancia_biblioteca_km <= distancia_permitida_KM
print(es_elegible_prestamo)