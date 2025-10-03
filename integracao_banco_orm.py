from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, CheckConstraint 
from sqlalchemy .orm import declarative_base, sessionmaker, relationship 

# method factory(fabrica de classes)
Base = declarative_base()

# Criar classe "real"(vai ser a tabela pelo ORM)

class Aluno(Base):
    __tablename__ = 'alunos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(56), nullable=False)
    idade = Column(Integer, nullable=False)
    email = Column(String, unique=True, nullable=False)

class Disciplina(Base):
    __tablbename__ ='disciplina'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(62), nullable=False, unique=True)
    carga_horaria = Column(Integer, nullable=False)
    CheckConstraint('carga_horarioa > 0')

    #
    #
    alunos = relationship('AlunoDisciplina', back_populates='Disciplina')

    def __repe__(self):
        return f"<Disciplina(id=({self.id}), noeme=({self.nome}), carga_horaria={self.carga_horaria})>"


#back_populates -> referencia reciproca
#em outras palafras -> quando você associa a Aluno à AlunoDisciplina é associada a Aluno
    disciplina = relationship('AlunoDisciplina', back_populates='Aluno')
     
    #metodo magico
    def __repr__(self):
        return f"<Aluno(id={self.id}, nome='{self.nome}',idade={self.idade},email='{self.email}')>"

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






