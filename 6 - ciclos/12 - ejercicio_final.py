print('***** EJERCICIO FINAL DE MODULO *****')

cadena = 'Hola mundo'
print(cadena)
longuitud = len(cadena)
numero_vocales = 0

for revision_letra in range(longuitud):
    letra = cadena[revision_letra]
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        numero_vocales += 1

print(numero_vocales)

# OTRA FORMA DE HACERLO
numero_vocales = 0
for j in range(longuitud):
    letra = cadena[j]
    if letra in 'aeiou':
        numero_vocales += 1

print(numero_vocales)


