from fastapi import FastAPI
from routes.main import api_router
from sqlmodel import create_engine, Session, select
from fastapi import Depends, logger
from typing import Annotated
from db import lista_naturalezas
from naturaleza import Naturaleza
from database import engine
import logging


app = FastAPI()
app.include_router(api_router)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
