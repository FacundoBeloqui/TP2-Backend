from collections.abc import Generator
from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, Session, select
import logging
from modelos import Movimiento, Pokemon, Naturaleza, Team
from db import lista_movimientos, lista_pokemones, lista_naturalezas, lista_equipos

SQLITE_FILE_PATH = "the_coding_stones.db"

engine = create_engine(f"sqlite:///{SQLITE_FILE_PATH}")


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]

logger = logging.getLogger(__name__)


def seed_naturaleza():
    with Session(engine) as session:
        if session.exec(select(Naturaleza)).first():
            logger.info("NOT loading seeds")
            return

        logger.info("Loading seeds...")

        session.add_all(lista_naturalezas)

        session.commit()

        logger.info("Seeds loaded on Db")


def seed_pokemon():
    with Session(engine) as session:
        if session.exec(select(Pokemon)).first():
            logger.info("NOT loading seeds")
            return

        logger.info("Loading seeds...")

        session.add_all(lista_pokemones)

        session.commit()

        logger.info("Seeds loaded on Db")


def seed_movimiento():
    with Session(engine) as session:
        if session.exec(select(Movimiento)).first():
            logger.info("NOT loading seeds")
            return

        logger.info("Loading seeds...")

        session.add_all(lista_movimientos)

        session.commit()

        logger.info("Seeds loaded on Db")


def seed_equipo():
    with Session(engine) as session:
        if session.exec(select(Team)).first():
            logger.info("NOT loading seeds")
            return

        logger.info("Loading seeds...")

        session.add_all(lista_equipos)

        session.commit()

        logger.info("Seeds loaded on Db")
