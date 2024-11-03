from fastapi import FastAPI
from routes.main import api_router
from sqlmodel import create_engine, Session, select
from fastapi import Depends, logger
from typing import Annotated
from db import lista_naturalezas
from naturaleza import Naturaleza
from database import engine


app = FastAPI()
app.include_router(api_router)


def seed():
    with Session(engine) as session:
        if session.exec(select(Naturaleza)).first():
            logger.info("NOT loading seeds")
            return

        logger.info("Loading seeds...")

        session.add_all(lista_naturalezas)
        session.commit()
        logger.info("Seeds loaded on Db")
