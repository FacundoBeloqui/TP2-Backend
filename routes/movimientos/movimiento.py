from fastapi import HTTPException, APIRouter, status
from database import SessionDep
from db import lista_movimientos
from modelos import Movimiento
from sqlmodel import select

router = APIRouter()


"""def buscar_movimiento(session: SessionDep, id: int):
    movimiento = session.exec(select(Movimiento).where(Movimiento.id == id)).first()

    if movimiento:
        return movimiento
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento not found"
    )"""


@router.get("/{id}")
def show(session: SessionDep, id: int) -> Movimiento:
    movimiento = session.exec(select(Movimiento).where(Movimiento.id == id)).first()

    if movimiento:
        return movimiento
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento not found"
    )
