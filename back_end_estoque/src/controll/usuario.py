from src.model.produtoModel import Usuarios
from src.configs.db import session
import bcrypt

class Usuario:
    def cadastro(usuario):
        nome = usuario['nome']
        email = usuario['email']
        cpf = usuario['cpf']
        senha = usuario['senha']
        senha_encriptada = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

        data_insert = Usuarios(nome=nome, email=email, cpf=cpf, senha=senha_encriptada)
        session.add(data_insert)
        session.commit()
        return 
    
    def login(usuario):
        email = usuario['email']
        senha = usuario['senha'].encode('utf-8')

        usuario_db = session.query(Usuarios).filter(Usuarios.email == email)
        if not usuario_db:
            return False
        
        if bcrypt.checkpw(senha, usuario_db[0].senha.encode('utf-8')):
            return True
        return False
