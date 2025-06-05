from sqlalchemy import Column, Integer, String
from DB.config import engine, Base, session

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    autor = Column(String(100))

    def cadastrar_livro():
        novo_livro = Livro(
            titulo = input("Digite O nome do livro: "), 
            autor = input("Digite o nome do autor: "))
        session.add(novo_livro)  
        session.commit()  
        print("Livro adicionado com sucesso")
        
