from dto.servico import ServicoDto
from repository.servico import ServicoRepository
from service.exception import service_wrapper


class ServicoService:
    def __init__(self):
        self._repo = ServicoRepository()

    @service_wrapper
    def cadastrar(self, servico: ServicoDto):
        self._repo.insert(servico)
