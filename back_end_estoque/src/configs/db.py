from sqlalchemy import create_engine

from sqlalchemy.orm import Session

engine = create_engine('mysql+pymysql://root:mudar123@172.17.0.2:3306/estoque')

session = Session()
