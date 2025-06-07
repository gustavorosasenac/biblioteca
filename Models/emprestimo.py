from sqlalchemy import Column, Integer, DateTime, ForeignKey
from DB.config import Base

class Emprestimo(Base):
    __tablename__ = "emprestimos"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(ForeignKey("usuarios.id"))
    livro_id = Column(ForeignKey("livros.id"))
    data_emprestimo = Column(DateTime)
    data_devolucao = Column(DateTime, nullable=True)
