from sqlalchemy import create_engine, text

#Crioação e conexão 
engine = create_engine("sqlite:///teste2.bd", echo= True, future = True)

with engine.connect() as conn:
    conn.execute(text("""
                CREATE TABLE IF NOT EXISTS alunos(
                      id INTEGER PRIMARY KEY AUTOINCREMENT ,
                      nome VARCHAR(50)NOT NULL, 
                      idade INTEGER NOT NULL,
                      email VARCHAR(50) UNIQUE NOT NULL
                      )
                      """))
    conn.commit()

#e2 = create_engine("mysql+pymysql://user:senha@localhost:3306/pizzaria")

#inserir aluno
with engine.connect() as conn:
    conn.execute(text("INSERT INTO alunos(nome,idade,email)VALUES(:nome, :idade, :email)"),
                    [ {"nome":"David","idade":21,"email":"davidvarao@senai.com.br"},
                      {"nome":"Geovani":"idade":23:"email":"geovanicuricica@senai.com.br"},
                      {"nome":"Silvio""idade":25:"email":"silviogaladaglobo@senai.br"}
                    ]
    )
    conn.commit()


#Consulta 1
with engine.conect()as conn:
    resultado = conn.execut(text("SELECT + FROM alunos"))
    for dado in resultado:
      print(dado.id,dado.nome,dado.idade,dado.email)