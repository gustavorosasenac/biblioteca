from sqlalchemy import Column, Integer, String
from DB.config import Base, engine

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    autor = Column(String(100))
        
