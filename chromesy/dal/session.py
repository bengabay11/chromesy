from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker


@contextmanager
def session_scope(session_class: sessionmaker) -> None:
    session = session_class()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
