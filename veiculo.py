class Transporte:
    def __init__(self, capacidade, velocidade_maxima):
        self.__capacidade = capacidade
        self.__velocidade_maxima = velocidade_maxima

    def descricao(self):
        print(f'Capacidade: {self.__capacidade} kg \nVelocidade maxima: {self.__velocidade_maxima} km/h')

    def mover(self):
        print(f'O transporte esta em movimento.')


class Onibus(Transporte):
    def __init__(self, capacidade, velocidade_maxima):
        super().__init__(capacidade, velocidade_maxima)

    def mover(self):
        print(f'O onibus está seguindo sua rota.')

class Bicicleta(Transporte):
    def __init__(self, capacidade, velocidade_maxima):
        super().__init__(capacidade, velocidade_maxima)

    def mover(self):
        print(f'A bicicleta está sendo pedalada.')

Onibus1 = Onibus(30,'8o')
bike1 = Bicicleta(1,'40')

