from flask import Blueprint, request, jsonify
from sqlalchemy import text

from repository.connection import db

servico = Blueprint('servico', __name__)


@servico.get('/list')
def get():
    with db.engine.connect() as conn:
        script = text(
            """
            select distinct t.table_schema from information_schema.tables t
            """
        )
        result = conn.execute(script)
        return [x[0] for x in result.fetchall()]


@servico.post('/')
def post():
    return request.get_json()
