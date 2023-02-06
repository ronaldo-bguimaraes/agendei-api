import os
import re


class ScriptsProvider:
    def __init__(self, source: str):
        self._source = source
        self._mapping = {}
        self._preload()
        self._scripts = {}
        self._parsed = {}

    def _preload(self):
        for filename in os.listdir(self._source):
            match = re.match(r'(?P<filename>.+)\.sql$', filename, re.IGNORECASE)
            if match:
                self._mapping[match.group('filename')] = os.path.join(self._source, filename)

    def _parse_script(self, code: str):
        return dict(
            re.findall(r'-{2}\s*name\s*:\s*(.+?)\s+(.+?)\s*(?=-{2}|$)', code, re.DOTALL)
        )

    def get(self, name: str):
        # se o script já foi carregado
        if name in self._scripts:
            if name in self._parsed:
                return self._parsed[name]
            self._parsed[name] = self._parse_script(self._scripts[name])
            return self.get(name)

        # se o script existe
        if name in self._mapping:
            try:
                with open(self._mapping[name], 'r') as file:
                    self._scripts[name] = file.read()
            except FileNotFoundError as e:
                raise Exception(f'Problema ao carregar script. Erro: {e}')
            return self.get(name)

        # se o script nao existe
        raise Exception('Script não existe')
