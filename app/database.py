from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://api-user:postgres@postgres/api_db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_factory = sessionmaker(bind=engine, autoflush=True, autocommit=False)
base = declarative_base()


def connect_db():
    db = session_factory()
    try:
        yield db
    finally:
        db.close()

