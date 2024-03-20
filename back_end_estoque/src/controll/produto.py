from src.model.produtoModel import Produtos, Categorias, Quantidades
from src.configs.db import session


class Produto:
    
    def buscarTodosProdutos():
        result = []
        
        data = session\
            .query(Produtos)\
            .join(Categorias, Categorias.id == Produtos.categoria_id)\
            .with_entities(
                Produtos.id,
                Produtos.marca,
                Produtos.descricao,
                Produtos.categoria_id,
                Categorias.categoria
            )\
            .all()
        
        for produto in data:
            result.append({
                "id": produto[0],
                "marca": produto[1],
                "descricao": produto[2],
                "categoria_id": produto[3],
                "categoria": produto[4]
            })
        return result
        
        
    def buscarProdutoPeloId(id):
        result = []
        data = session.query(Produtos)\
        .join(Categorias, Categorias.id == Produtos.categoria_id)\
        .join(Quantidades, Quantidades.produto_id == Produtos.id)\
        .filter(Produtos.id == id)\
        .with_entities(
                Produtos.id,
                Produtos.marca,
                Produtos.descricao,
                Produtos.categoria_id,
                Categorias.categoria,
                Quantidades.tamanho,
                Quantidades.cor,
                Quantidades.quantidade,

            )\
            .all()
        if data != []:
            for produto in data:

                result.append({
                    "id": produto[0],
                    "marca": produto[1],
                    "descricao": produto[2],
                    "categoria_id": produto[3],
                    "categoria": produto[4],
                    "tamanho": produto[5],
                    "cor": produto[6],
                    "quantidade": produto[7]
                })

            return result
        
        
        else:
            dataCath = session.query(Produtos)\
            .join(Categorias, Categorias.id == Produtos.categoria_id)\
            .filter(Produtos.id == id)\
            .with_entities(
                    Produtos.id,
                    Produtos.marca,
                    Produtos.descricao,
                    Produtos.categoria_id,
                    Categorias.categoria
                )\
            .all()
            for produto in dataCath:
                result.append({
                    "id": produto[0],
                    "marca": produto[1],
                    "descricao": produto[2],
                    "categoria_id": produto[3],
                    "categoria": produto[4]
                })
            session.expire_all()
            return result
            
            

    def criarNovoProduto(produto):
        
        marca = produto['marca']
        descricao = produto['descricao']
        categoria_id = produto['categoria_id']
        data_insert = Produtos(marca=marca, descricao=descricao, categoria_id=categoria_id)
        session.add(data_insert)
        session.commit()
        

    def produtoPossuiCadastro(produto):
        marca = produto['marca']
        descricao = produto['descricao']
        categoria_id = produto['categoria_id']
        data = session.query(Produtos).filter(Produtos.marca==marca)
        for produto in data:
            if produto.descricao == descricao and produto.categoria_id == categoria_id:
                return ({
                    "id": produto.id,
                    "marca": produto.marca,
                    "descricao": produto.descricao,
                    "categoria_id": produto.categoria_id
                })
        return
            
                
