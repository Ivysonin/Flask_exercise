from flask import Blueprint, request

usuario_bp = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_bp.route('/', methods=['POST'])
def create():
    user = request.get_json()

    print(user)
    return 'Criado usuario'


@usuario_bp.route('/', methods=['GET'])
def index():
    user = [{"nome":"ivyson"}, {"idade":16}, {"ativo":True}]

    for dic in user:
        print(dic)
    return user


@usuario_bp.route('/<int:id>', methods=['PUT'])
def att(id):
    infor = [ { 1:{"nome":"ivyson"} },
              { 2:{"nome":"thauan"} },
              { 3:{"nome":"Ana"} } ]

    print('informações do usuário para atualizar:')
    for dic in infor:
        if id in dic:
            print(dic[id])

    # Atualizando o usuário
    for dic in infor:
        if id in dic:
            dic[id]["nome"] = request.get_json()

    print("informações atualizadas:")
    for dic in infor:
        if id in dic:
            print(dic[id])

    return "usuário atualizado"


@usuario_bp.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    infor = [ { 1:{"nome":"ivyson"} },
              { 2:{"nome":"thauan"} },
              { 3:{"nome":"Ana"} } ]
    
    print("Usuário para deletar:")
    for dic in infor:
        if id in dic:
            print(dic[id])

    # Deletando o usuário
    for dic in infor:
        if id in dic:
            dic.pop(id)

    print("Usuário deletado com sucesso!!!")

    # Exibindo a lista com o usuário deletado
    print()
    print(infor)

    return "Usuário deletado"