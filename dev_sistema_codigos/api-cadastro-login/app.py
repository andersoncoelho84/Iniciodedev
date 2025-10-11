from flask import Flask, request, jsonify

#criar um objeto flask, que vai ser o app
app = Flask(__name__)

#json aceitar caracteres especiais
app.config['JSON_AS_ASCII']= False

#se der errado,descomente o de baixo
#app.json.ensure.ascii = False

#usuario(id,nome,email,senha)
usuarios = [
    {'id':1, 'nome':'Raphamel', 'email':'raphamel@senai.br', 'senha':'Flamengo2019'},
    {'id':2, 'nome':'david','email':'davidvarao@senai.br','senha':'davidvarao@senai.br'},
    {'id':3, 'nome':'Geovani','email':'geo@vanni.br', 'senha':'PizzaioloTricolor'}
]
#pq não estamos usando BD
#ideia de autoincrement
proximo_id = 4

def validar_usuario(dados):
    #validar dados vindo das requisicões
    #3 retornos:
    #1-> se são validos(true/false)
    #2-> Qual foi o erro
    #3-> Dados Validos
    #exisem dados no json?

    if not dados:
        return False, "Corpo da requisição não pode ser vasio", None
    
    #se existe a fumção nome
    if 'nome' not in dados:
        return False, "Camos 'nome' é obrigatorio", None
   
    #já que o campo existe,
    nome = dados.get('nome', '').strip()
    
    #tenho o nome, o que eu quero validar?
    if not nome:
        return False, "Campo 'nome' não pode estar fazio", None
    
    if len(nome)<3:
        return False, "campo 'nome' deve ter no minimo 3 caracter", None
    #------------------------------

    if 'email' not in dados:
        return False, "Campo 'email' é obrigatório", None
    
    email = dados.get('email','').strip().lower()

    if not email:
        return False, "Campo 'email' não pode estar vazio", None
    
    #Certa -> Campo Email existe e o email existe
    email_existente = [ user for user in usuarios if email == user ['email']]    

# Verificar se há algum usuario com esse email
    if len (email_existente)> 0:
        return False, "Este 'email' já esta cadastrado", None 

    #---------------------------------------------------------
    if 'senha' not  in dados:
        return False, "O campo 'senha' e obrigatorio", None
    # senha ja existe
    senha = dados.get('senha','').strip()
    
    if not senha:
        return False," Campo 'senha' não pode estar vazia", None
    
    if len(senha)< 8 and len(senha)> 50:
        return False,"Campo 'senha' com tamanho inválido", None

    dados_validados = {
        'nome':nome,
        'email': email,
        'senha':senha
    }
    return True,None, dados_validados





#roita padrão- Index - Landpage
@app.route('/')
def home():
    return jsonify({'msg':"Bem vindo ao Geovanni's Pizza"})

#Rota GET - Lista usuario
app.route('/usuario', methods=['GET'])
def listar_usuarios():
    #recuperar os usuarios(sem senha)

    usuarios_sem_senha = []

    for usuario in usuarios:
        user = usuario.copy()
        user.pop('senha', None)
        usuarios_sem_senha.append(user)

    return jsonify({'dados': usuarios_sem_senha, 'total': len(usuarios)}),200

#POST -> ideia de Criar Usuários
@app.route('/usuarios', methods=['POST'])
def criar_usuarios():

    global proximo_id
    valido, erro, dados_validos = validar_usuario(request.get_json())


#iniciar o servidro -> porta padrão 5000
if __name__ == '__naim__' :
    app.run(degub=True)

