# ejercicio final de cadenas

print(f'*** Generador de Email ***')
nombre_usuario = 'Ubaldo Acosta Soto'
print(f'Nombre usuario: {nombre_usuario}')

# normalizacion de usuario
nombre_minusculas = nombre_usuario.lower()
# print(nombre_minusculas)
nombre_lista = nombre_minusculas.split()
# print(nombre_lista)
nombre_usuario_normalizado = str(nombre_lista[0]) + '.' + str(nombre_lista[1]) + '.' + str(nombre_lista[2])
print(f'Nombre normalizado: {nombre_usuario_normalizado}')

# normalizacion de Dominio
nombre_empresa = 'Global Mentoring'
extension_dominio = '.com.mx'
print('')
print(f'Nombre empresa: {nombre_empresa}')
print(f'Extension del dominio: {extension_dominio}')

nombre_empresa_miniscula = nombre_empresa.lower()
#print(nombre_empresa_miniscula)
nombre_empresa_lista = nombre_empresa_miniscula.split()
#print(nombre_empresa_lista)
nombre_empresa_normalizado = '@' + str(nombre_empresa_lista[0]) + str(nombre_empresa_lista[1]) + str(extension_dominio)
print(f'dominio de email normalizado: {nombre_empresa_normalizado}')

email = nombre_usuario_normalizado + nombre_empresa_normalizado
print('')
print(f'Email final generado: {email}')
