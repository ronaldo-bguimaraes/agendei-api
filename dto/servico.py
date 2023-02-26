from datetime import time, datetime


class ServicoDto:
    def __init__(self):
        self.id: int = 0
        self.nome: str = ''
        self.descricao: str = ''
        self.valor_servico: float = 0
        self.duracao: time = time()

    @classmethod
    def from_json(cls, json: dict):
        dto = cls()
        dto.nome = json['nome']
        dto.descricao = json['descricao']
        dto.valor_servico = float(json['valor_servico'])
        dto.duracao = datetime.strptime(json['duracao'], '%H:%M:%S.%f').time()
        return dto
