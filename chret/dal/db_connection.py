from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chret.dal.session import session_scope


class DBConnection(object):
    def __init__(self):
        self._connection = None
        self._session_class = None

    def connect(self, protocol, database):
        url = f"{protocol}://{database}"
        engine = create_engine(url)
        self._session_class = sessionmaker(bind=engine)
        self._connection = engine.connect()

    @staticmethod
    def create_connection_string(username, password, host, port, route):
        return f"{username}:{password}@{host}:{port}/{route}"

    def select(self, model, serializable=False):
        with session_scope(self._session_class) as session:
            query = session.query(model)
            results = query.all()
            return [result.dict() for result in results] if serializable else results

    def insert(self, row):
        with session_scope(self._session_class) as session:
            session.add(row)

    def update(self):
        pass

    def delete(self):
        pass

    def close(self):
        self._connection.close()
