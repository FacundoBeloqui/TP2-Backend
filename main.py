from fastapi import FastAPI
from routes.main import api_router
from sqlmodel import create_engine, Session, select
from fastapi import Depends, logger
from typing import Annotated
#from naturaleza import Naturaleza
from db import lista_naturalezas
from models import Naturaleza

app = FastAPI()
app.include_router(api_router)

SQLITE_FILE_PATH = "the_coding_stones.db"

engine = create_engine(f"sqlite:///{SQLITE_FILE_PATH}")


def get_db():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]

def seed():
    with Session(engine) as session:
        if session.exec(select(Naturaleza)).first():
            logger.info("NOT loading seeds")
            return

        logger.info("Loading seeds...")

        session.add_all(lista_naturalezas)
        session.commit()
        logger.info("Seeds loaded on Db")

        