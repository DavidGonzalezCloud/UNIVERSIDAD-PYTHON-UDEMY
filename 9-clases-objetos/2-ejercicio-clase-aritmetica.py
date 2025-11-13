print('***** EJERCICIO CLASE ARITMETICA ******')

# Definimos nuestra clase

class Aritmetica:

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def suma(self):
        suma = self.numero1 + self.numero2
        print(f'La suma de {self.numero1} y {self.numero2} es: {suma}')

    def resta(self):
        resta = self.numero1 - self.numero2
        print(f'La resta de {self.numero1} y {self.numero2} es: {resta}')

    def multiplicacion(self):
        multiplicacion = self.numero1 * self.numero2
        print(f'La multiplicacion de {self.numero1} y {self.numero2} es: {multiplicacion}')

    def division(self):
        division = self.numero1 / self.numero2
        print(f'La division de {self.numero1} y {self.numero2} es: {division:.2f}')
        

# Creamos el primero objeto
aritmetica1 = Aritmetica(5,6)

# Usamos los metodos de nuestra clase
aritmetica1.suma()
aritmetica1.resta()
aritmetica1.multiplicacion()
aritmetica1.division()

# creamos segundo objeto
aritmetica2 = Aritmetica(12,16)

# Usamos metodos de nuestro segundo obejto
aritmetica2.suma()
aritmetica2.resta()
aritmetica2.multiplicacion()
aritmetica2.division()
