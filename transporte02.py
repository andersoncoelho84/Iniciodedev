class veiculo:
    def __init__(self, Marca,passageiros, velocidade_maxima,ano):
        self.__Marca = marca
        self.__passageiros = passageiros
        self.__velocidade_maxima = velocidade_maxima
        self.__ano = ano
        self.__cores ['Branco','Azul','Vermelho','Preto']

    def getMarca(self):
        return self.__marca

    def getPassageiros(self):
        return self.__passageiros    
    
    def getVelocidade_maxima(self):
         return self.__velocidade_maxima 
           
    def getAno(self):
         return self.__ano
    
    def velocidade_maxima(self):
         print(f'O veiculo está na velocidade de {'self.__velocidade'} é a via e de no maximo 50')

    def acelerar(self):
         print(f'Este {} acelera sempre no limite da via')

veiculo1 = onibus('MArcopolo',)