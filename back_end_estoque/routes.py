from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from src.controll.produto import Produto
from src.controll.categoria import Categoria
from src.controll.entradaSaida import EntradaSaida
from src.controll.usuario import Usuario

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

@app.route('/entradas', methods=['PUT'])
def entradaProduto():
    produto = request.json
    atualizar_produto = EntradaSaida.entradaProduto(produto)
    if atualizar_produto == False:
        return make_response(jsonify("Erro interno"), 400)
    return "Atualizado com sucesso!"

@app.route('/entradas/<int:id>')
def historicoEntradas(id):
    produto = EntradaSaida.historicoEntrada(id)
    return jsonify(produto)

@app.route('/saidas', methods=['POST'])
def saidaProduto():
    produto = request.json
    EntradaSaida.saidaProduto(produto)
    return "Atualizado com sucesso!"

@app.route('/saidas/<int:id>')
def historicoSaida(id):
    produto = EntradaSaida.historicoSaida(id)
    return jsonify(produto)

@app.route('/cadastro', methods=['POST'])
def cadastro_ususario():
    data_usuario = request.json
    usuario = Usuario.cadastro(data_usuario)
    if not usuario:
        return "Erro ao cadastrar usuário"
    return jsonify(usuario)
    
@app.route('/login', methods=['POST'])
def login():
    data_usuario = request.json
    usuario = Usuario.login(data_usuario)
    if usuario == False:
        return "Não existe cadastro"
    return jsonify(usuario)

@app.route('/tamanho_cor', methods=['POST'])
def cadastroTamanhoCor():
    caracteristica = request.json
    caracteristica = EntradaSaida.cadastroTamanhoCor(caracteristica)
    if caracteristica:
        return make_response(jsonify("Já possui cadastro para característica informada!"), 400)
    return make_response(jsonify("Características adicionada com sucesso!"), 201)
if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
