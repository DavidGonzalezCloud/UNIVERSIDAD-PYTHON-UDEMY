# definicion de una clase

# las clases se definen con la primera letra en mayuscula
class Persona:
    
    # Constructor
    # __init__ es llamado dunder o double underscore
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''
        Persona:
            Nombre: {self.nombre}
            Apellido: {self.apellido}''')

# Creacion de objetos
if __name__ == '__main__':
    # Creamos nuestro primer objeto
    persona1 = Persona('Laila', 'Acosta') # Se crea un objeto vacio en memoria
    persona1.mostrar_persona()

    # Mostramos la direccion de memoria de persona1
    print(f'Direccion de memoria persona1: {id(persona1)}')
    print(f'Direccion de memoria hexadecimal persona 1: {hex(id(persona1))}')

    # Creamos segundo objeto
    persona2 = Persona('Ernesto','Gonzalez')
    persona2.mostrar_persona()
