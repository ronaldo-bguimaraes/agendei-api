from abstract.scripts import ScriptsProvider

scripts = ScriptsProvider(source='scripts')

script = scripts.get('usuario').get('create')

print(script)
