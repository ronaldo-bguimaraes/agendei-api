from flask import Blueprint, request

user = Blueprint('user', __name__)


@user.get('/')
def get():
    return 'user route'


@user.post('/')
def post():
    return ''
