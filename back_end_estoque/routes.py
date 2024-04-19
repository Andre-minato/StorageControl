from flask import Flask, jsonify, request
from flask_cors import CORS
from src.controll.produto import Produto
from src.controll.categoria import Categoria
from src.controll.entradaSaida import EntradaSaida

app = Flask(__name__)
cors = CORS(app)

@app.route('/produtos', methods=['POST'])
def inserirProdutos():
    produto = request.json
    temProduto = Produto.produtoPossuiCadastro(produto)
    if temProduto:
        return "Produto já possui cadastro"
    Produto.criarNovoProduto(produto)
    return "produto inserido!"

@app.route('/produtos')
def buscarProdutos():
    produtos = Produto.buscarTodosProdutos()
    return jsonify(produtos)

@app.route('/produtos/<int:id>')
def buscarProdutoPeloId(id):
    produto = Produto.buscarProdutoPeloId(id)
    return jsonify(produto)

@app.route('/categorias', methods=['POST'])
def inserirCategorias():
    categoria = request.json
    temCadastro = Categoria.possuiCadastro(categoria)
    if temCadastro:
        return "Categoria ja está cadastrada!"
    Categoria.criarNovaCategoria(categoria)
    return "Categoria inserido com sucesso"
    

@app.route('/categorias')
def getCategoria():
    categoria = Categoria.buscarTodasCategorias()
    return jsonify(categoria)

@app.route('/entradas', methods=['POST'])
def entradaProduto():
    produto = request.json
    EntradaSaida.entradaProduto(produto)
    return "Atualizado com sucesso!"

@app.route('/entradas/<int:id>')
def historicoEntradas(id):
    produto = EntradaSaida.historicoEntrada(id)
    return jsonify(produto)

@app.route('/saidas', methods=['POST'])
def saidaProduto():
    produto = request.json
    produto = EntradaSaida.saidaProduto(produto)
    if produto:
        return "Atualizado com sucesso!"
    return "Tente mais tarde"

@app.route('/produto_cor')
def buscarQuantidadePelaCor():
    produto = request.json
    quantidade = Produto.buscarPorCor(produto)
    return jsonify(quantidade)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)