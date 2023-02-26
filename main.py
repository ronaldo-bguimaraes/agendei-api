import os

from flask import Flask

from controller.servico_controller import servico

app = Flask(__name__)

app.register_blueprint(servico, url_prefix='/servico')


def get_port():
    return os.environ.get('PORT', '8080')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=get_port(), debug=True)
