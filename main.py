from fastapi import FastAPI
from routes.main import api_router
from sqlmodel import create_engine, Session
from fastapi import Depends
from typing import Annotated

app = FastAPI()
app.include_router(api_router)

SQLITE_FILE_PATH = "the_coding_stones.db"

engine = create_engine(f"sqlite:///{SQLITE_FILE_PATH}")


def get_db():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
