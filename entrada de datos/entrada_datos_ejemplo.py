# Sistema para solicitar informacion del empleado

print('*** Sistema de informacion de empleados ***')

nombre_empleado = input('Introduce tu nombre: ')
edad_empleado = int(input('Introduce tu edad: '))
salario_empleado = float(input('Introduce tu salario: '))
es_jefe_departamento = input('Es jefe de de departamento (si/no): ')

# Vamos a convertir a un tipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

print('\nDatos del empleado:')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}') # Seleccionar la cantidad de decimales que se deben de mostrar
print(f'Es jefe de departamento: {es_jefe_departamento}')


