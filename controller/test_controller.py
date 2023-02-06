from flask import Blueprint

from repository.connection import get_hour

test = Blueprint('test', __name__)


@test.get('/')
def get():
    return get_hour()
