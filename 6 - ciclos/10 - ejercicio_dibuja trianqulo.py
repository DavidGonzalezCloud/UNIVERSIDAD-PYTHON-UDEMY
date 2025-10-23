print('***** DIBUJAR TRIANGULO *****')

numero_filas = int(input('De cuantas filas tiene que ser el triangulo: '))

for fila in range(1, numero_filas + 1):
    espacios_blanco = ' ' * (numero_filas - fila)
    asteriscos = '*' * (2 * fila - 1)
    print(espacios_blanco + asteriscos)




