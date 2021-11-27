import psycopg2
import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine("postgresql+psycopg2://postgres:5432@localhost/games",
                       client_encoding='utf8')

connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'user'
    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    nik_name = sq.Column(sq.TEXT(20), unique=True)
    user_email = sq.Column(sq.String, unique=True)


def register_user(nik_name, user_email):
    try:
        new_user = User(
            nik_name=nik_name,
            user_email=user_email
        )
        session.add(new_user)
        session.commit()
        return True
    except (IntegrityError, InvalidRequestError):
        return False


def check_db_user(nik_name):
    current_user_name = session.query(User).filter_by(nik_name=nik_name).first()
    return current_user_name


if __name__ == '__main__':
    Base.metadata.create_all(engine)
