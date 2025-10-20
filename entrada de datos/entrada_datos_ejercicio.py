# Ejercicio: crear un programa para solicitar algunos valores importantes para una receta de cocina.

# solicitar datos
print('**** Informacion de recetas de cocina ****')

nombre_receta = input('Nombre de la receta: ')
ingredientes = input('Ingredientes: ')
tiempo = int(input('Tiempo de preparacion en minutos: '))
Dificultad = input('Dificultad (Facil, Media, Alta): ')

print('________________________')
print(f'El nombre de la receta es: {nombre_receta}')
print(f'Los ingredientes de la receta son: {ingredientes}')
print(f'El tiempo de la receta es: {tiempo} minutos. ')
print(f'La dificultad de la receta es: {Dificultad}')

