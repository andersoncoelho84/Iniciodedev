class Conta:
    # Primeiro metodo sempre é: construtor

    # primeiro "atributo" deve ser: self
    def __init__(self, numConta, titular, saldo=0):
        self.numConta = numConta
        self.titular = titular
        self.saldo = saldo
        inicio = '\nExtrato do(a) ' + self.titular + \
            ' com saldo inicial de: R$ ' + str(self.saldo)
        self.extrato = [inicio]

    def realizarDeposito(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            saida = 'Deposito realizado com' + \
                  ' sucesso no valor de: R$ '+ str(valor) + \
                  '\nSaldo atual' + str(self.realizarDeposito)
            
            self.extrato.append(saida)
        else:
            print('Digite um valor válido')

    def realizarSaque(self, valor):
        if self.saldo >= valor and valor > 0:
            # tudo certo, pode sacar
            self.saldo = self.saldo - valor
            saida = 'Saque realizado com sucesso' + \
                ' no valor de: R$ ' + str(valor)
            self.extrato.append(saida)
        elif valor <= 0:  # else if -> elif
            print('Digite um valor válido')
        else:
            print('Não há saldo suficiente')

    def realizarTransferencia(self, destinatario, valor):
        saida = 'Transferencia para a conta ' + \
            destinatario.numConta + ' no valor de: R$ ' \
            + str(valor)
        self.realizarSaque(valor)
        destinatario.realizarDeposito(valor)
        saida += 'Fim da Transferencia'
    
    def retirarExtrato(self):
        for op in self.extrato:
            print(op)
        print(f'\nSaldo AtualR$ {self.saldo:.2f} \n')

conta1 = Conta('00001', 'Renan')
conta1.realizarDeposito(100)
conta1.realizarSaque(50)
conta2 = Conta('00002', 'Raphael', 2)

conta2.realizarTransferencia(conta1, 1.99)
print(f'R$ {conta2.saldo:.2f}')


conta1.retirarExtrato()