from fastapi import HTTPException, status
from sqlmodel import select

from database import SessionDep
from modelos import Pokemon


def buscar_pokemon(session: SessionDep, id: int) -> Pokemon:
    pokemon = session.exec(select(Pokemon).where(Pokemon.id == id)).first()

    if pokemon:
        return pokemon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found"
    )
