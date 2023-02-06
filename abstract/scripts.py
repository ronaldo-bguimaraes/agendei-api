import os


class ScriptsProvider:
    def __init__(self, source: str):
        self._source = source
        self._mapping = {}
        self._preload()
        self._scripts = {}

    def _preload(self):
        for filename in os.listdir(self._source):
            self._mapping[filename] = os.path.join(self._source, filename)

    def get(self, script: str):
        # se o script já foi carregado
        if script in self._scripts:
            return self._scripts.get(script)

        # se o script existe
        if script in self._mapping:
            try:
                with open(self._mapping[script], 'r') as file:
                    self._scripts[script] = file.read()
            except FileNotFoundError as e:
                raise Exception(f'Problema ao carregar script. Erro: {e}')
            return self._scripts.get(script)

        # se o script nao existe
        raise Exception('Script não existe')
