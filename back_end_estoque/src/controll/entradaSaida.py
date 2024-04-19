from datetime import datetime
from src.model.produtoModel import Entradas, Quantidades
from src.controll.atualizaEstoque import AtualizaEstoque
from src.configs.db import session


class EntradaSaida:

    def entradaProduto(produto):
        data_time = datetime.now()
        produto_id = produto['produto_id']
        tamanho = produto['tamanho'].upper()
        cor = produto['cor'].upper()
        qtde_entrada = produto['qtde_entrada']
        data_insert = Entradas(produto_id=produto_id, tamanho=tamanho, qtde_entrada=qtde_entrada, cor=cor,
                            dataEntrada=data_time, horaEntrada=data_time)
        session.add(data_insert)
        session.commit()
        isRegistered = AtualizaEstoque.estaRegistradoTabelaQuantidade(data_insert)
        if isRegistered:
            id = isRegistered["id"]
            vlr_atual = isRegistered['quantidade'] + (int(qtde_entrada))
            AtualizaEstoque.atualizandoQuantidade(id, vlr_atual)
            return
        AtualizaEstoque.novoProdutoTabelaQuantidade(data_insert)  
        return
    
    def saidaProduto(produto):
        result = []
        produto_id = produto['produto_id']
        #qtde_entrada = produto['qtde_entrada']
        data = session.query(Quantidades).filter(Quantidades.produto_id == produto_id).all()
        
        for produto in data:
            result.append({
                "id": produto.id,
                "tamanho": produto.tamanho,
                "cor": produto.cor,
                "quantidade": produto.quantidade,
            })
        return result

    def historicoEntrada(id):
        lista = []
        data = session.query(Entradas).filter(Entradas.produto_id == id).all()
        print(data)
        for entrada in data:
            lista.append({
                "id": entrada.id,
                "data_entrada": entrada.dataEntrada.strftime("%d/%m/%Y"),
                "hora_entrada": entrada.horaEntrada.strftime("%H:%M:%S"),
                "tamanho": entrada.tamanho,
                "cor": entrada.cor,
                "quantidade": entrada.qtde_entrada,
                "produto_id": entrada.produto_id

            })
        
        return lista
        
   
           

