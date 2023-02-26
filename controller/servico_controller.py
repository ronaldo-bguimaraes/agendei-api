from flask import Blueprint, request

from dto.servico import ServicoDto
from service.exception import ServiceException
from service.servico import ServicoService

servico = Blueprint('servico', __name__)

serv = ServicoService()


@servico.post('/')
def post():
    json = request.get_json()
    dto = ServicoDto.from_json(json)
    try:
        serv.cadastrar(dto)
        return 'cadastrado'
    except ServiceException as e:
        return f'erro ao cadastrar: {e}'
