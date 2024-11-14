from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from database import SessionDep
from fastapi import HTTPException, APIRouter
from typing import List
from modelos import (
    Naturaleza,
    Integrante,
    Team,
    Pokemon,
    Movimiento,
    TeamBase,
    TeamPublicWithIntegrantes
)
import routes.utils as utils
from sqlalchemy.orm import selectinload
import sqlalchemy.future

generacion = ""

router = APIRouter()


@router.get("/nature")
def get_naturalezas(session: SessionDep) -> list[Naturaleza]:
    query = select(Naturaleza)
    naturalezas = session.exec(query)
    return naturalezas


@router.get("/")
def obtener_equipos(session: SessionDep) -> list[Team]:
    query = select(Team)
    equipos = session.exec(query)
    return equipos


@router.get("/{team_id}")
def get_team_by_id(session: SessionDep, team_id: int):
    return utils.buscar_equipo(session, team_id)


@router.post("/", response_model=Team)
def create_team(session: SessionDep, team_create: TeamPublicWithIntegrantes):

    if team_create.generacion < 1 or team_create.generacion > 9: 
        raise HTTPException(status_code=400, detail="Generacion no permitida")

    team = Team(
        nombre=team_create.nombre, 
        generacion=team_create.generacion
    )

    session.add(team)
    session.commit()
    #session.refresh(team)

    #integrantes = []
    for integrante_data in team_create.integrantes:
        pokemon = session.get(Pokemon, integrante_data.id_pokemon)
        if team_create.generacion not in pokemon.generacion:
            raise HTTPException(status_code=400, detail="El pokemon elegido no corresponde a esta generacion.")
        naturaleza = session.get(Naturaleza, integrante_data.id_naturaleza)

        if not pokemon:
            raise HTTPException(status_code=404, detail="Pokemon no encontrado.")
        if not naturaleza:
            raise HTTPException(status_code=404, detail="Naturaleza no encontrada.")

        integrante = Integrante(
            nombre=integrante_data.nombre,
            id_equipo=team.id,
            id_pokemon=pokemon.id,
            id_naturaleza=naturaleza.id,
        )

        if integrante_data.movimientos:
            for movimiento_id in integrante_data.movimientos:
                #movimiento = session.get(Movimiento, movimiento_id)
                movimiento = session.exec(select(Movimiento).where(Movimiento.id == movimiento_id)).first()
                if movimiento != None and (team_create.generacion in movimiento.generacion):
                    integrante.movimientos.append(movimiento)
                else:
                    raise HTTPException(
                        status_code=404,
                        detail=f"Movimiento con id {movimiento_id} no encontrado.",
                    )

        #integrantes.append(integrante)
        team_create.integrantes.append(integrante)
    #session.add(team)
    team.integrantes = team_create.integrantes
    session.commit()
    session.refresh(team)

    # equipo_con_integrantes = session.exec(
    #     sqlalchemy.future.select(Team)
    #     .options(selectinload(Team.integrantes))
    #     .where(Team.id == team.id)
    # ).scalar_one()

    return team


@router.put("/{id}")
def update(session: SessionDep, id: int, equipo_nuevo: TeamBase) -> Team:
    equipo = utils.buscar_equipo(session, id)

    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")

    equipo.nombre = equipo_nuevo.nombre
    equipo.generacion = equipo_nuevo.generacion

    # equipo.integrantes = equipo_nuevo.integrantes

    session.add(equipo)
    session.commit()
    session.refresh(equipo)

    return equipo


@router.delete("/{id}")
def delete(session: SessionDep, id: int) -> Team:
    equipo = utils.buscar_equipo(session, id)
    session.delete(equipo)
    session.commit()
    return equipo
