from flask import Blueprint

from database import get_hour

test = Blueprint('test', __name__)


@test.get('/')
def get():
    return get_hour()
