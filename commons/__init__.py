from sqlalchemy import create_engine
from .models import schemas


from sqlalchemy.engine import Engine

# to return
from sqlalchemy.orm import Session


class UnknownDBError(Exception):
    pass


SQL_ALCHEMY_ENGINES = {
    "antispeedbump": create_engine(
        "sqlite:////Users/berkay/Documents/workspace/Data/antispeedbump/antispeedbump.db",
        echo=False,
    )
}


def _create_table(model: str, db_engine: Engine):
    # example usage: _create_table("Sites", SQL_ALCHEMY_ENGINES['sites'])

    model = getattr(schemas, model)
    print("model", model)
    model.__table__.create(db_engine)


def engine(db_name: str = "antispeedbump") -> Engine:
    try:
        return SQL_ALCHEMY_ENGINES[f"{db_name}"]
    except KeyError:
        raise UnknownDBError


def session(db_name: str = "antispeedbump") -> Session:
    return Session(engine(db_name), expire_on_commit=False)
