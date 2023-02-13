from flask import Blueprint

test = Blueprint('test', __name__)


@test.get('/')
def get():
    return 'hello world'
