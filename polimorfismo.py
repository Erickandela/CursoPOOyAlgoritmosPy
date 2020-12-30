class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Caminando')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Me mueo en bicicleta')
        # super().avanza()

def main():
    persona = Persona('Erick')
    persona.avanza()

    ciclista= Ciclista('Candela')
    ciclista.avanza()

if __name__ == '__main__':
    main()