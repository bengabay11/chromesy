from contextlib import contextmanager


@contextmanager
def session_scope(session_class):
    session = session_class()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
