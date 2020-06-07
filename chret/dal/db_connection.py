from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnection(object):
    def __init__(self):
        self._engine = None
        self._session_class = None

    def connect(self, protocol, path):
        url = f"{protocol}://{path}"
        self._engine = create_engine(url)
        self._session_class = sessionmaker(bind=self._engine)
        self._engine.connect()

    def select(self, object):
        with session_scope(self._session_class) as session:
            return session.query(object).fetchall()

    def insert(self):
        with session_scope(self._session_class) as session:
            session.add(object)
            session.commit()

    def update(self):
        pass

    def delete(self):
        pass

    def close(self):
        self._engine.close()


@contextmanager
def session_scope(session_class):
    session = session_class()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()