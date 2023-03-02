import sqlalchemy as database

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from settings.config import ENGINE_DATABASE

# create_engine - создает привязку к базе
engine = create_engine(ENGINE_DATABASE)
# session позволяет проводить операции с бд
session = scoped_session(sessionmaker(
    autoflush=False, autocommit=False, bind=engine)
)

Base = declarative_base()
# Чтобы запросы можно было писать вот так: Model.query(). Это короче, чем session.query(Model),
# и сессию импортировать не надо
Base.query = session.query_property()


def create_db():
    # создает схему бд это произойдет при запуске приложения
    Base.metadata.create_all(bind=engine)
