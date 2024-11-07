from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from database import SessionDep
from fastapi import HTTPException, APIRouter
from typing import List
from modelos import Naturaleza, Integrante, Team, Pokemon, Movimiento, TeamBase, TeamCreate
import routes.utils as utils
from sqlalchemy.orm import selectinload

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
def get_team_by_id(session:SessionDep, team_id: int):
    return utils.buscar_equipo(session, team_id)


@router.post("/", response_model=Team)
def create_team(session:SessionDep, team_create: TeamCreate):
    team = Team(
        nombre=team_create.nombre,
        generacion=team_create.generacion
    )
    
    # session.add(team)
    # session.commit()  
    # session.refresh(team)

    #integrantes = []
    for integrante_data in team_create.integrantes:
        integrante = Integrante(
            nombre=integrante_data.nombre,
            id_equipo=team.id,
            id_pokemon=integrante_data.id_pokemon,
            id_naturaleza=integrante_data.id_naturaleza,
            #movimientos=integrante_data.movimientos  # Si es necesario
        )
        # if integrante_data.movimientos:
        #     for movimiento_id in integrante_data.movimientos:
        #         # Aquí asumimos que los movimientos ya están en la base de datos
        #         # Debes validar si el movimiento existe antes de asociarlo
        #         movimiento = session.get(Movimiento, movimiento_id)
        #         if movimiento:
        #             integrante.movimientos.append(movimiento)
        #         else:
        #             raise HTTPException(status_code=404, detail=f"Movimiento con id {movimiento_id} no encontrado.")
        #integrantes.append(integrante)
        team.integrantes.append(integrante)
    
    session.add(team)
    session.commit()  
    session.refresh(team)
    # query = select(Team).where(Team.id == team.id).options(selectinload(Team.integrantes))
    # team_with_integrantes = session.exec(query).first()
    #equipos = session.exec(select(Team).options(selectinload(Team.integrantes))).all()
    return team



@router.put("/{id}")
def update(session: SessionDep, id: int, equipo_nuevo: TeamBase) -> Team:
    equipo = utils.buscar_equipo(session, id)
    
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")

    equipo.nombre = equipo_nuevo.nombre
    equipo.generacion = equipo_nuevo.generacion
    
    #equipo.integrantes = equipo_nuevo.integrantes
    
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
