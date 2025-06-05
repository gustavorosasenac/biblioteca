from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:Bender741@localhost:3306/biblioteca")

Base = declarative_base()

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()