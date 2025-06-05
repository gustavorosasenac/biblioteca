from sqlalchemy import create_engine
from sqlalchemy .orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:root@localhost:3306/biblioteca")

Base = declarative_base()
class Usuario(Base):

    def cadastrar_usuario(self):
        __tablename__ = "usuarios"
        id = Column(Integer, primary_key=True)
        nome = Column(String(100))
        email = Column(String(100))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


nome = input("\nDigite seu nome: ")
email = input("\nDigite seu e-mail")
#novo_usuario = Usuario(nome="João", email="joao@email.com")
session.add_all()
session.commit()





