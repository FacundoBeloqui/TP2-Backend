from fastapi import FastAPI
from routes.main import api_router
from sqlmodel import create_engine, Session, select
from fastapi import Depends, logger
from typing import Annotated
from db import lista_naturalezas
from modelos import Naturaleza
from database import engine
import logging
from database import seed_pokemon, seed_naturaleza, seed_movimiento
from sqlalchemy import Engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def init(db_engine: Engine) -> None:
    try:
        with Session(db_engine) as session:
            # Try to create session to check if DB is awake
            session.exec(select(1))
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info("Initializing service")
    init(engine)
    logger.info("Service finished initializing")
    seed_pokemon()
    seed_movimiento()
    seed_naturaleza


app = FastAPI()
app.include_router(api_router)

main()
