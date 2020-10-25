import configparser

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_db_engine():
    config = configparser.ConfigParser()
    config.read('config.ini')

    host = config.get('Postgres', 'host')
    dbname = config.get('Postgres', 'dbname')
    port = config.get('Postgres', 'port')
    username = config.get('Postgres', 'username')
    password = config.get('Postgres', 'password')

    return create_engine(
        'postgresql://{username}:{password}@{host}/{dbname}'.format(
            host=host, dbname=dbname, port=port, username=username, password=password
        ), echo=False
    )


def get_session(db_engine):
    session_class = sessionmaker(bind=db_engine)
    return session_class()
