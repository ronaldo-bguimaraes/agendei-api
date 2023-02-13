from flask import Blueprint, request, jsonify

servico = Blueprint('servico', __name__)


@servico.get('/')
def get():
    return 'user route'


@servico.post('/')
def post():
    return request.get_json()
