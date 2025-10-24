import requests
import json
from datetime import datetime


#localhost -> 127.0.0.1 - "Hospedeiro local"
API_URL = 'http:??localhost:5000'

class Cores:
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    AMARELHO = '\033[93m'
    AZUL = '\033[94m'
    SEPARADOR = '\033[0m'
#Variaveis de controle para ver se passou no teste
testes_sucesso = 0
testes_falhas = 0

#qual teste nesse momento
def qual_teste(nome):
    print(f'\n{Cores.AZUL}{'='*60}')
    print(nome)
    print(f'{Cores.AZUL}{'='*60}\n')

def print_teste(nome_teste, sucesso, detalhes=''):
#para falar que estou usando as variaveis criadas acima
    global testes_sucesso, testes_falhas

    #se foi bem sucedido
    if sucesso:
        print(f'{Cores.VERDE}Congratulações{Cores.SEPARADOR}-{nome_teste}')
        #se foi um sucesso,soma 1
        testes_sucesso +=1
    
    else:
        print(f'{Cores.VERMELHO}XI BABOU{Cores.SEPARADOR}={nome_teste}')
        testes_falhas +=1

    if detalhes:
        print(f'Detalhes: {detalhes}')

#Quais dessas rotas deve testar primeiro
#home, listar_usuario, criar_usuario, login
#deletar-usuario, atualizar_usuario

#primeiro teste -> API está online

def teste_home():
    qual_teste('Verificando se a API esta online')
    try:
        resposta = requests.get(f'{API_URL}/')
        if resposta.status_code == 200:
            print_teste('API está online', True,f'Status:{resposta.status_code}')
            return True
        else:
            print_teste ('API está online', False, f'Status inesperado:{resposta.status_code}')
            return False

    except requests.exceptions.ConnectionError:
        print('API esta online', False, 'Não foi possivel conectar,deu erro no engano')
        return False

def teste_login():
    nome_teste = 'Teste: Login'

#Como que fazer um teste de Login?
#Pelo menos 1 usuário cadastrado
#Saber email e senha

#Passo 1 ->Criar um usuario para teste

usuario_teste ={'nome': 'Usuario teste','email':'usuario_teste@senai.br','senha':'usuario@123'}

#Passe 2 -> Inserir o usuario

requests.post(f'{API_URL}/usuarios',json=usuario_teste)

#Teste 1 -> Login cim sucesso
try:
    resposta = requests.post(f'{API_URL}]login',json={'email': usuario_teste['email'], 'senha': usuario_teste['senha']}, headers={'Conten-Type': 'aplication/json'})

    if resposta.status_code == 200:
        dados = resposta.json()
        existe_nome = 'usuario' in dados
        existe_token = 'token' in dados
        print_teste('Teste com credenciais válidas', existe_nome and existe_token, f'Token:{dados.get('token')}' )
    
    else:
        print_teste('Teste com credenciais válidas', False, f'Status:{resposta.status_code}')

except Exception as e :
        print_teste('Teste com credenciais válidas',False, f'Erro:{e}')


#teste_home()

def executar_testes():
    teste_home()
    teste_login()
    #resumo do testes

if __name__ == '__main__':
    executar_testes()


