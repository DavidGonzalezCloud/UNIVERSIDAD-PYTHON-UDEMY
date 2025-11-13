# USAREMOS EL EJEMPLO DE LA CLASE ANTERIOR

# Definimos la clase coche
class coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca      
        self._modelo = modelo   
        self._color = color    

    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')


    # Definimos metodos get y set

    def get_marca(self):
        return self._marca
    def set_marca(self, marca):
        self._marca = marca
    
    def get_modelo(self):
        return self._modelo
    def set_modelo(self, modelo):
        self._modelo = modelo

    # Definimos los metodos get y set de manera mas pythonica.

    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, color):
        self._color = color
    

# Programa Principal
if __name__ == '__main__':

    #Creamos el primer objeto
    coche1 = coche('Toyota','Yaris','Azul')
    coche1.conducir()

    #Buenas practicas: usar metodos set y get
    coche1.set_marca('Hyundai')
    coche1.set_modelo('Elantra')
    coche1.color = 'Verde'

    coche1.conducir()

    # Probamos como funciona la nueva forma de definir los metodos get and set
    print(f'\nEl Color del coche es: {coche1.color}')
    # Modificamos el color
    coche1.color = "Cafe"
    print(f'\nEl nuevo color del coche es: {coche1.color}')


    # Preguntamos directamente los atributos de un objeto.
    print(f'Atributos del coche1: {coche1.__dict__}')
