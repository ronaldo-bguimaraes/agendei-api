import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import URL

load_dotenv()


def _get_url():
    return URL.create(
        drivername='mysql+pymysql',
        username=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        host=os.environ['DB_HOST'],
    )


db = SQLAlchemy()


def create_db(app: Flask):
    app.config.update({
        'SQLALCHEMY_DATABASE_URI': _get_url(),
    })
    db.init_app(app)
