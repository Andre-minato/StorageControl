from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine('mysql+pymysql://root:mudar123@172.17.0.2:3306/estoque')
      ###create_engine('mysql+pymysql://root:mudar123@172.17.0.2:3307/estoque')

Session = sessionmaker(
    bind=engine,
    expire_on_commit=True
    )
session = Session()
