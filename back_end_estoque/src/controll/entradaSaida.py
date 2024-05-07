from datetime import datetime
from src.model.produtoModel import Entradas, Quantidades, Saidas
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
        id = isRegistered["id"]
        if isRegistered['quantidade'] == None:
            vlr_entrada = (int(qtde_entrada))
            AtualizaEstoque.atualizandoQuantidade(id, vlr_entrada)  
            return
        vlr_atual = isRegistered['quantidade'] + (int(qtde_entrada))
        AtualizaEstoque.atualizandoQuantidade(id, vlr_atual)
        return
        
    def cadastroTamanhoCor(produto):
        result=[]
        produto_id = int(produto['produto_id'])
        tamanho = produto['tamanho'].upper()
        cor = produto['cor'].upper()
        verificar_caracteristica = session.query(Quantidades)\
            .filter(Quantidades.produto_id == produto_id)\
                .all()
        for data in verificar_caracteristica:
            if data.produto_id == produto_id and data.tamanho == tamanho and data.cor == cor:
                return True
        data_insert = Quantidades(produto_id=produto_id, tamanho=tamanho, cor=cor)
        session.add(data_insert)
        session.commit()
        return

    def saidaProduto(produto):
        result = []
        data_time = datetime.now()
        produto_id = produto['produto_id']
        tamanho = produto['tamanho'].upper()
        cor = produto['cor'].upper()
        qtde_saida = int(produto['qtde_saida'])
        data_insert = Saidas(produto_id=produto_id, tamanho=tamanho, qtde_saida=qtde_saida, cor=cor,
                            dataSaida=data_time, horaSaida=data_time)
        #caracteristica_produto = {'produto_id': produto_id, 'tamanho': tamanho, 'cor': cor}
        verificar_produto = AtualizaEstoque.estaRegistradoTabelaQuantidade(data_insert)
        if verificar_produto:
            data = session.query(Quantidades).filter(Quantidades.id == verificar_produto['id']).all()
            
            for produto in data:
                result.append({
                    "id": produto.id,
                    "tamanho": produto.tamanho,
                    "cor": produto.cor,
                    "quantidade": produto.quantidade,
                })
            qtde = result[0]['quantidade']
            tamanho = result[0]['tamanho']
            cor = result[0]['cor']
            id = result[0]['id']
            if qtde < qtde_saida:
                return False
            data_insert = Saidas(produto_id=produto_id, tamanho=tamanho, qtde_saida=qtde_saida, cor=cor,
                                dataSaida=data_time, horaSaida=data_time)
            session.add(data_insert)
            session.commit()
            qtde_atual = qtde - qtde_saida
            AtualizaEstoque.atualizandoQuantidade(id, qtde_atual)
            return 
        return

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
        
    def historicoSaida(id):
        lista = []
        data = session.query(Saidas).filter(Saidas.produto_id == id).all()
        #print(data)
        for saida in data:
            lista.append({
                "id": saida.id,
                "data_entrada": saida.dataSaida.strftime("%d/%m/%Y"),
                "hora_entrada": saida.horaSaida.strftime("%H:%M:%S"),
                "tamanho": saida.tamanho,
                "cor": saida.cor,
                "quantidade": saida.qtde_saida,
                "produto_id": saida.produto_id

            })
        
        return lista
           

