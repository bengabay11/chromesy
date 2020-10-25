from dataclasses import dataclass

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@dataclass
@as_declarative()
class Base(object):
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def json(self) -> dict:
        dict_base = self.__dict__.copy()
        for key in dict_base.copy():
            if key.startswith("_"):
                del dict_base[key]
        return dict_base
