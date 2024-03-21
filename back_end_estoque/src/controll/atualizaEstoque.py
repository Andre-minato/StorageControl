from src.model.produtoModel import Quantidades
from src.configs.db import session



class AtualizaEstoque:
    def novoProdutoTabelaQuantidade(produto):
        produto_id = produto.produto_id
        tamanho = produto.tamanho
        cor = produto.cor
        quantidade = produto.qtde_entrada
        entrada_id = produto.id
        data_insert = Quantidades(produto_id=produto_id, tamanho=tamanho, cor=cor,
                               quantidade=quantidade, entrada_id=entrada_id)
        session.add(data_insert)
        session.commit()
        return
        
    def estaRegistradoTabelaQuantidade(data):
        cor = data.cor
        tamanho = data.tamanho
        produto_id = data.produto_id
        data = session.query(Quantidades).filter(Quantidades.produto_id==produto_id).all()
        
        
        for Quantidade in data:
            if Quantidade.cor == cor and Quantidade.tamanho == tamanho:
                return {
                    "id": Quantidade.id,
                    "tamanho": Quantidade.tamanho,
                    "cor": Quantidade.cor,
                    "quantidade": Quantidade.quantidade,
                    "produto_id": Quantidade.produto_id
                }
        return
    def atualizandoQuantidade(id, vlr_atual):
        session.query(Quantidades).filter(Quantidades.id == id).update({Quantidades.quantidade: vlr_atual})
        session.commit()
        return
        
        

        
        
