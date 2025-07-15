from flask import Blueprint, jsonify, request

produtos_bp = Blueprint('produtos', __name__, url_prefix='/produtos')

# lista de produtos fixos (simulando banco de dados)
LISTA_PRODUTOS = [
    {1:{"nome":"Camisa", "valor":20}},
    {2:{"nome":"Short", "valor":15}},
    {3:{"nome":"Sapato", "valor":10}}
]


# 1️⃣ Listar produtos
# Crie uma rota GET que devolva uma lista de produtos cadastrados.
@produtos_bp.route('/', methods=['GET'])
def index():
    for dic in LISTA_PRODUTOS:
        print(dic)
        
    return jsonify({"LISTA_PRODUTOS": LISTA_PRODUTOS})


# 2️⃣ Adicionar novo produto
# Crie uma rota POST que receba um JSON e adicione um novo produto à lista.
@produtos_bp.route('/', methods=['POST'])
def create():
    produto = request.get_json()

    LISTA_PRODUTOS.append(produto)

    for dic in LISTA_PRODUTOS:
        print(dic)
    return jsonify({'LISTA_PRODUTOS':LISTA_PRODUTOS})


# 3️⃣ Atualizar produto pelo ID
# Crie uma rota PUT que atualize os dados de um produto específico com base no ID passado na URL.
@produtos_bp.route('/<int:id>', methods=['PUT'])
def att(id):
    print(f'Produto para ser atualizado:')
    for dic in LISTA_PRODUTOS:
        if id in dic:
            print(dic[id])
    
    # Atualizando o valor do produto
    dados = request.get_json()
    for dic in LISTA_PRODUTOS:
        if id in dic:
            dic[id]["valor"] = dados.get("valor", dic[id]["valor"])
            dic[id]["nome"] = dados.get("nome", dic[id]["nome"])

    print('Lista de produtos atualizados:')
    for dic in LISTA_PRODUTOS:
        print(dic)

    return jsonify({"LISTA_PRODUTOS":LISTA_PRODUTOS})

            
# 4️⃣ Deletar produto pelo ID
# Crie uma rota DELETE que remova um produto da lista usando o ID informado.
@produtos_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    print('Produto a ser deletado:')
    for dic in LISTA_PRODUTOS:
        if id in dic:
            print(dic[id])

    # Deltando o produto
    for dic in LISTA_PRODUTOS:
        if id in dic:
            dic.pop(id)

    print('Produtos atualizados:')
    for dic in LISTA_PRODUTOS:
        print(dic)

    return jsonify(LISTA_PRODUTOS)


# 5️⃣ Exibir produto específico
# Crie uma rota GET para exibir os detalhes de um único produto pelo ID.
@produtos_bp.route('/<int:id>', methods=['GET'])
def exibir(id):
    print('Detalhes do produto:')
    for dic in LISTA_PRODUTOS:
        if id in dic:
            print(dic[id])
            return jsonify({"Produto:":dic[id]})
        

# 6️⃣ Objetivo: Criar uma rota GET que receba um parâmetro de valor mínimo 
# (ex: /produtos/valor/20) e retorne todos os produtos cujo valor seja igual ou acima desse valor.
@produtos_bp.route('/valor/<int:valor>', methods=['GET'])
def valor_minimo(valor):
    lista_valor_minimo = {}

    print('Produtos com o valor mínimo:')
    for dic in LISTA_PRODUTOS:
        for id,produto in dic.items():
            if produto["valor"] >= valor:
                lista_valor_minimo.update({id:produto})
    
    print(lista_valor_minimo)
    return jsonify({"Lista com os produtos de valor mínimo":lista_valor_minimo})


# 7️⃣ Objetivo: Criar uma rota GET que receba um trecho do nome de um produto
# (ex: /produtos/nome/ca) e retorne todos os produtos que contêm esse trecho (ignorando maiúsculas/minúsculas)
@produtos_bp.route('/nome/<letras>', methods=['GET'])
def trecho_nome(letras):
    lista_trecho_nomes = {}

    for dic in LISTA_PRODUTOS:
        for id,produto in dic.items():
            if letras.lower() in produto["nome"].lower():
                lista_trecho_nomes.update({id:produto['nome']})

    print(f'Esses nomes abaixo tem o trecho: {letras}')
    print(lista_trecho_nomes)
    return jsonify({f"Nomes abaixo que tem o trecho: {letras}":lista_trecho_nomes})


# 8️⃣ Filtrar produtos por faixa de valor
# → Receber dois valores (mínimo e máximo) na URL e retornar produtos dentro dessa faixa.
@produtos_bp.route('/valor/<int:min>/<int:max>', methods=['GET'])
def valor_min_max(min,max):
    lista_min_max = {}
    
    for dic in LISTA_PRODUTOS:
        for id,produto in dic.items():
            if min <= produto['valor'] <= max:
                lista_min_max.update({id:produto})
    
    print(f"Produtos dentro da faixa de preço R${min} e R${max}")
    print(lista_min_max)
    return jsonify({f"Produtos dentro da faixa de preço R${min} e R${max}":lista_min_max})


# 9️⃣ Exibir os produtos ordenados por valor
# → Criar uma rota que ordena os produtos do mais barato ao mais caro (ou vice-versa).
@produtos_bp.route('/ordena', methods=['GET'])
def ordena():
    lista_ordenada = []

    for dic in LISTA_PRODUTOS:
        for id,produto in dic.items():
            lista_ordenada.append({"id":id, "nome":produto['nome'], "valor":produto['valor']})
    
    lista_ordenada = sorted(lista_ordenada, key=lambda valor: valor['valor'])
    
    print("Lista ordenada pelo o preço:")
    print(lista_ordenada)
    return jsonify({"Lista ordenada pelo o preço:":lista_ordenada})