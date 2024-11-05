from fastapi import HTTPException, APIRouter, status
from database import SessionDep
from modelos import Movimiento
from sqlmodel import select

router = APIRouter()


@router.get("/{id}")
def show(session: SessionDep, id: int) -> Movimiento:
    movimiento = session.exec(select(Movimiento).where(Movimiento.id == id)).first()

    if movimiento:
        return movimiento
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Movimiento not found"
    )
