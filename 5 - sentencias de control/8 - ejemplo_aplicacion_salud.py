print('*** APLICACION DE SALUD Y FITNESS')

# DEFINIMOS LAS CONTASNTES
metas_pasos_diarios = 10000
calorias_por_paso = 0.04

# SOLICITAR INFORMACION AL USUARIO
nombre_usurio = str(input('Cual es tu nombre?: '))
pasos_diarios = int(input('Cuantos pasos has caminado hoy: '))

# VERIFICAR SI EL USUARIO ALCANZO LA META DE PASOS DIARIOS
meta_alcanzada = pasos_diarios >= metas_pasos_diarios
meta_alcanzada_txt = 'Si' if meta_alcanzada else 'No'

# CALCULAMOS LAS CALORIAS QUEMADAS
calorias_quemadas = pasos_diarios * calorias_por_paso

# MOSTRAMOS LA INFORMACION
print(f'\nUsuario: {nombre_usurio}')
print(f'Pasos dados hoy: {pasos_diarios}')
print(f'Calorias quemadas hoy: {calorias_quemadas}')
print(f'Meta de pasos diarios alcanzada: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es: {metas_pasos_diarios}')