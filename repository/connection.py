import pymysql
from pymysql import cursors
from sqlalchemy import create_engine


def get_connection():
    engine = create_engine('mysql+pymysql:')
    return pymysql.connect(
        host='',
        user='root',
        password='root',
        cursorclass=cursors.DictCursor,
    )


get_connection()
