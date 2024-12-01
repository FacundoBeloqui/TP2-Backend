from fastapi import HTTPException, APIRouter, status
from database import SessionDep
from modelos import Naturaleza
from sqlmodel import select

router = APIRouter()


@router.get("/")
def get_naturalezas(session: SessionDep) -> list[Naturaleza]:
    query = select(Naturaleza)
    naturalezas = session.exec(query)
    return naturalezas


@router.get("/{id}")
def show(session: SessionDep, id: int) -> Naturaleza:
    naturaleza = session.exec(select(Naturaleza).where(Naturaleza.id == id)).first()

    if naturaleza:
        return naturaleza
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Naturaleza not found"
    )
