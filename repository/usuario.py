from database.connection import get_connection
from dto.usuario import UsuarioDto
from repository.exception import repository_wrapper


class UsuarioRepository:
    @repository_wrapper
    def insert(self, usuario: UsuarioDto):
        query = '''
            insert into cadastro.usuario
                (username, password)
            values
                (%(username)s, %(password)s)
            ;
        '''
        args = {
            'username': usuario.username,
            'password': usuario.password,
        }
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, args)
