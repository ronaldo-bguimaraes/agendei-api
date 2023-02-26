import os
import pymysql
from pymysql import cursors


def get_connection():
    return pymysql.connect(
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        host=os.environ['DB_HOST'],
        cursorclass=cursors.DictCursor,
    )
