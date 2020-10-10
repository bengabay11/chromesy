from typing import Type, Any

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from chpass.dal.models.Base import Base
from chpass.dal.session import session_scope


class DBConnection(object):
    def __init__(self) -> None:
        self._connection = None
        self._session_class = None

    def connect(self, protocol: str, database: str) -> None:
        url = f"{protocol}://{database}"
        engine = create_engine(url)
        self._session_class = sessionmaker(bind=engine)
        self._connection = engine.connect()

    def select(self, model: Type[Base], serializable: bool = False) -> list:
        with session_scope(self._session_class) as session:
            query = session.query(model)
            results = query.all()
            return [result.json() for result in results] if serializable else results

    def insert(self, row: Base) -> None:
        with session_scope(self._session_class) as session:
            session.add(row)

    def update(self, row: Base, column: Any, new_value: Any) -> None:
        setattr(row, column, new_value)

    def delete(self, row: Base) -> None:
        with session_scope(self._session_class) as session:
            session.delete(row)

    def close(self) -> None:
        self._connection.close()
