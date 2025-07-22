from flask import Blueprint, make_response, jsonify

user_bp = Blueprint('user', __name__, url_prefix='/user')


# Testando rota com make_response()
@user_bp.route('/', methods=['GET'])
def index():
    lista_user = {'id':1, 'nome':'ivyson', 'idade':16}

    return make_response({'Lista usuário':lista_user})


# Testando rota com jsonify()
@user_bp.route('/2', methods=['GET'])
def index2():
    lista_user = {'id':1, 'nome':'ivyson', 'idade':16}

    return jsonify({'Lista usuário':lista_user})