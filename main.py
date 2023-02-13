import os

from dotenv import load_dotenv
from flask import Flask

from controller.servico_controller import servico
from repository.connection import create_db

load_dotenv()

app = Flask(__name__)

create_db(app)

app.register_blueprint(servico, url_prefix='/servico')


def get_port():
    return os.environ.get('PORT', '8080')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=get_port(), debug=True)
