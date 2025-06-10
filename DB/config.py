from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#engine = create_engine("mysql+pymysql://root:Bender741@localhost:3306/biblioteca")

engine = create_engine("sqlite:///biblioteca.db") 

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()