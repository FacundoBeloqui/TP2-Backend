from fastapi import HTTPException, status
from sqlmodel import select
from database import SessionDep
from modelos import Pokemon, Team


def buscar_pokemon(session: SessionDep, id: int) -> Pokemon:
    pokemon = session.exec(select(Pokemon).where(Pokemon.id == id)).first()

    if pokemon:
        return pokemon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado"
    )


def buscar_equipo(session: SessionDep, grupo_id: int) -> Team:
    query = select(Team).where(Team.id == grupo_id)
    grupo = session.exec(query).first()

    if grupo:
        return grupo
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Equipo no encontrado"
    )
