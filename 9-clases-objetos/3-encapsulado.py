# ***** TEORIA *****

# Atributos protegidos o privados
    # self._nombre      (Atributo protegido)
    # self.__apellido   (Atributo privado)

# Crear los metodos conocidos como get(leer) y set(modificar)

# ***** EJEMPLO *****

#Definimos la clase coche
class coche:

    def __init__(self, marca, modelo, color):
        self.marca = marca      # Atributo publico
        self._modelo = modelo   # Atributo protegido
        self.__color = color    # Atributo privado

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}''')

# Programa Principal
if __name__ == '__main__':

    #Creamos el primer objeto
    coche1 = coche('Toyota','Yaris','Azul')
    coche1.conducir()

    # No deberias de acceder a los atributos que no sean publicos
    coche1.marca = 'toyota 2'
    coche1._modelo = 'Yaris 2'  # Esto no es una buena practica.
    coche1.__color = 'Rojo'     # Python ignora la modificacion

    coche1.conducir()


