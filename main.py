from sqlalchemy import create_engine
from sqlalchemy .orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:root@localhost:3306/biblioteca")

Session = sessionmaker(bind=engine)
session = Session()



