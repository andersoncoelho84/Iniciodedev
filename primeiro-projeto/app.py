from flask import Flask
# importando a Class Flask do modulo flask

#Criar uma instancia do Flask =  objeto
app = Flask(__name__)
#__name__ é o nome do modulo atual -> navegação

#Definir Rotas(Endpoints)
#quando acessar ao servidor,chame essa função
@app.route('/')
def home():
    return 'Bem vindo ao Mundo das APIS'
#flask ele converte string em um resposta HTTP

@app.route('/sobre')
def sobre():
    return 'Estamos na aula de DEV de Sistemas com Flask.'

@app.route('/contato')
def contato():
    return '21 4002-8922 email: ta_dificil@dev_sistemas.senai.br'

#rota com parâmetro
@app.route('/usuario/<nome>')
def usuario(nome):
    return f'Prezado,{nome} espero que essa mensagem o encontre bem.'

#Rota com parâmetro numérico
@app.route('/produto/<int:id>')
def produto(id):
    return f'Voê escolheu o produto com {id}'


#executar o servidor
if __name__ == '__main__':
    app.run(debug=True)
    #debug -> servodor no modo de desenvolvimento
    #ativa o reload automativcamente e mostra os erros de forma detalhada
