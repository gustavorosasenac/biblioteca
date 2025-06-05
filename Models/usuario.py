from sqlalchemy import Column, Integer, String

from DB.config import session


class Usuario:

    #def cadastrar_usuario(Base):
        __tablename__ = "usuarios"
        id = Column(Integer, primary_key=True)
        nome = Column(String(100))
        email = Column(String(100))
        nome = input("\nDigite seu nome: ")
        email = input("\nDigite seu e-mail")

        session.add(nome, email)
        session.commit()





