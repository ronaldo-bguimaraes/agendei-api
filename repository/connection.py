from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:root@db/agendei', echo=True)

session = sessionmaker(bind=engine, future=True)


def get_hour():
    with engine.connect() as connection:
        script = text()
        result = connection.execute(script)
        result = result.fetchone()
        return result[0].__str__()
