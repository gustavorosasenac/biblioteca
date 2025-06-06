from sqlalchemy import Column, Integer, String
from DB.config import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100))





