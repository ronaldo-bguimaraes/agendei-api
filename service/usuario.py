from dto.usuario import UsuarioDto
from repository.usuario import UsuarioRepository
from service.exception import service_wrapper


class UsuarioService:
    def __init__(self):
        self._repo = UsuarioRepository()

    @service_wrapper
    def cadastrar(self, usuario: UsuarioDto):
        self._repo.insert(usuario)
