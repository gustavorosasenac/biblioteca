from sqlalchemy import Column, Integer, String, ForeignKey
from DB.config import engine, Base, session

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100))

    def cadastrar_usuario():
        novo_usuario = Usuario(
            nome = input("Digite seu nome: "), 
            email = input("Digite seu email: "))
        session.add(novo_usuario)  
        session.commit()  
        print("Usuário adicionado com sucesso!")





