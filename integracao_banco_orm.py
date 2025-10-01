from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy .orm import declarative_base, sessionmaker

# method factory(fabrica de classes)
Base = declarative_base()

# Criar classe "real"(vai ser a tabela pelo ORM)

class Aluno(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(56), nullable=False)
    idade = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=False)
    #metodo magico
    def __repr__(self):
        return f"Aluno(id={self.id}, nome='{self.nome}',idade={self.idade},email='{self.email}')>"

#Criar engine(cria conexão com o bd)
engine = create_engine("sqlite:///teste_com_orm2.br", echo=True, future=True)

#criar a sessão(isso conecta o engine ao ORM)
Session = sessionmaker(bind=engine,future=True)

#criar as tabelas
Base.metadata.create_all(engine)

#Insert -> inserir alunos na tabela
with Session() as session:
    alunos = [
        Aluno(nome='David',idade=21,email='davidvarao@senai.br'),
        Aluno(nome='Geovanni', idade=23, email='geovanicuricica@senai.br'),
        Aluno(nome='Silva', idade=25, email='silviogaladaglobo@senai.br')

    ]
    session.add_all(alunos)
    session.commit()

#fazer select - consultar o banco
with Session() as session:
    resultado = session.query(Aluno).all()

    for aluno in resultado:
        print(aluno.id, aluno.nome, aluno.idade, aluno.email)





