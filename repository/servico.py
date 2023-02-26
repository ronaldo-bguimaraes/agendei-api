from database.connection import get_connection
from dto.servico import ServicoDto
from repository.exception import repository_wrapper


class ServicoRepository:
    @repository_wrapper
    def insert(self, servico: ServicoDto):
        query = '''
            insert into cadastro.servico
                (nome, descricao, valor_servico, duracao, id_prestador)
            values
                (%(nome)s, %(descricao)s, %(valor_servico)s, %(duracao)s, %(id_prestador)s)
            ;
        '''
        args = {
            'nome': servico.nome,
            'descricao': servico.descricao,
            'valor_servico': servico.valor_servico,
            'duracao': servico.duracao,
            'id_prestador': 1,
        }
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, args)
                connection.commit()
