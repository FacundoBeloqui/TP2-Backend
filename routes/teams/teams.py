from models import *
from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from database import SessionDep
from fastapi import HTTPException, APIRouter
from typing import List
from modelos import Naturaleza, Integrante, Team

lista_equipos = []
generacion = ""

router = APIRouter()


@router.get("/nature")
def get_naturalezas(session: SessionDep) -> list[Naturaleza]:
    query = select(Naturaleza)
    naturalezas = session.exec(query)
    return naturalezas


"""
@router.get("/")
def obtener_todos_los_equipos(pagina: int = 1):
    if len(lista_equipos) == 0:
        raise HTTPException(status_code=404, detail="No se encontraron equipos creados")
    if pagina <= 0:
        raise HTTPException(
            status_code=400,
            detail="Error en el ingreso. La pagina debe ser un entero mayor a cero",
        )

    if pagina > (len(lista_equipos) + 9) // 10:
        raise HTTPException(
            status_code=404,
            detail="No se encontro la pagina solicitada",
        )
    if len(lista_equipos) <= 10 and pagina == 1:
        return lista_equipos
    return lista_equipos[10 * (pagina - 1) : 10 * pagina]


@router.get("/{team_id}", response_model=TeamDataCreate)
def get_team_by_id(team_id):
    if not team_id.isdecimal():
        raise HTTPException(status_code=400, detail="El id debe ser un numero entero")
    team = None
    for t in lista_equipos:
        if t["id"] == int(team_id):
            team = t
            break
    if team is None:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return team

@router.post("/")
def create_team(team: TeamCreate):
    lista_generacion_pokemones = []
    lista_generacion_movimientos = []
    if team.generacion > 9 or team.generacion < 1:
        raise HTTPException(status_code=404, detail="No se encontró la generacion")

    if len(team.pokemones) < 1 or len(team.pokemones) > 6:
        raise HTTPException(
            status_code=400,
            detail="Debe elegir al menos 1 pokemon y no mas de 6 pokemones",
        )

    for id_pokemon, generaciones in generaciones_pokemon.items():
        if team.generacion in generaciones:
            for pokemon in lista_pokemones:
                if pokemon.id == int(id_pokemon):
                    lista_generacion_pokemones.append(pokemon)

    for movimiento in lista_movimientos:
        if team.generacion == movimiento.generacion:
            lista_generacion_movimientos.append(movimiento)

    pokemon_elegido = []
    movimiento_elegido = []
    for pokemon_team in team.pokemones:
        for p in lista_generacion_pokemones:
            if p.id == pokemon_team.id:
                pokemon_elegido.append(p)
    for movimiento_team in team.pokemones:
        for m in lista_generacion_movimientos:
            if m.id in movimiento_team.movimientos:
                movimiento_elegido.append(m)

    if len(pokemon_elegido) == 0:
        raise HTTPException(
            status_code=404,
            detail="Pokemon seleccionado no encontrado en la generacion",
        )

    if len(movimiento_elegido) == 0:
        raise HTTPException(
            status_code=404, detail="Movimiento no encontrado en la generacion"
        )

    nuevo_equipo = {"pokemon": pokemon_elegido, "movimiento": movimiento_elegido}

    lista_equipos.append(nuevo_equipo)

    return nuevo_equipo
"""


def buscar_equipo(session: SessionDep, grupo_id: int) -> Team:
    query = select(Team).where(Team.id == grupo_id)
    grupo = session.exec(query).first()

    if grupo:
        return grupo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grupo not found")


# @router.put("/{id}")
# def update(session: SessionDep, id: int, equipo_nuevo: Team) -> Team:
#     equipo = buscar_equipo(session, id)
#     equipo. = equipo_nuevo.
#     equipo. = equipo_nuevo.
#     equipo. = equipo_nuevo.
#     session.add()
#     session.commit()
#     session.refresh(equipo)
#     return equipo


@router.delete("/{id}")
def delete(session: SessionDep, id: int) -> Team:
    equipo = buscar_equipo(session, id)
    session.delete(equipo)
    session.commit()
    return equipo


raise HTTPException(status_code=404, detail=f"Equipo con ID {id} no encontrado.")
