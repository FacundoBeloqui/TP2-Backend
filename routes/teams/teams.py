from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from database import SessionDep
from fastapi import HTTPException, APIRouter
from typing import List
from modelos import Naturaleza, Integrante, Team, Pokemon, Movimiento, TeamBase, TeamCreate
import routes.utils as utils

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

"""

@router.get("/")
def obtener_equipos(session: SessionDep):
    query = select(Team)
    equipos = session.exec(query)
    return equipos


# @router.get("/{team_id}")
# def get_team_by_id(session:SessionDep, team_id: int):
#     return utils.buscar_equipo(session, team_id)

"""
@router.post("/", response_model=Team)
def create_team(session:SessionDep, team_create: TeamBase):
    team = Team(
        nombre=team_create.nombre,
        generacion=team_create.generacion
    )
    
    session.add(team)
    session.commit()  # Asegúrate de hacer commit aquí para que el equipo obtenga un id
    
    # Crear y agregar los integrantes
    integrantes = []
    for integrante_data in team.integrantes:
        integrante = Integrante(
            nombre=integrante_data.nombre,
            equipo_id=team.id,  # Asociar al equipo recién creado
            id_pokemon=integrante_data.id_pokemon,
            id_naturaleza=integrante_data.id_naturaleza,
            movimientos=integrante_data.movimientos  # Si es necesario
        )
        integrantes.append(integrante)
    
    session.add_all(integrantes)
    session.commit()  # Commit para los integrantes
    
    # Retornar el equipo con los integrantes
    session.refresh(team)
    return team
"""
    # if team.generacion > 9 or team.generacion < 1:
    #     raise HTTPException(status_code=404, detail="No se encontró la generacion")

    # if len(team.integrantes) < 1 or len(team.integrantes) > 6:
    #     raise HTTPException(
    #         status_code=400,
    #         detail="Debe elegir al menos 1 pokemon y no mas de 6 pokemones",
    #     )

   # pokemones_generacion = session.exec(select(Pokemon).where(Pokemon.generacion == team.generacion))
    #movimientos_generacion = session.exec(select(Movimiento).where(Movimiento.generacion == team.generacion))

    #pokemones_elegidos = session.exec(select(Pokemon).where(pokemon.id == ))

    # pokemon_elegido = []
    # for pokemon_team in team.integrantes:
    #     for p in pokemones_generacion:
    #         if p.id == pokemon_team.id:
    #             pokemon_elegido.append(p)
    #         else:
    #             raise HTTPException(
    #                 status_code=404,
    #                 detail=f"Pokemon {pokemon_team.id} no encontrado en la generación {team.generacion}",
    #             )

    # nuevo_equipo = Team(
    #     generacion=team.generacion,
    #     nombre=team.nombre
    # )

    # session.add(nuevo_equipo)
    # session.commit()

    # for pokemon in pokemon_elegido:
    #     integrante = Integrante(
    #         nombre=pokemon.identificador,
    #         id_equipo=nuevo_equipo.id,
    #         id_pokemon=pokemon.id
    #     )
    #     session.add(integrante)

    # session.commit()

    # session.refresh(nuevo_equipo)
    # return nuevo_equipo

    

    # for id_pokemon, generaciones in generaciones_pokemon.items():
    #     if team.generacion in generaciones:
    #         for pokemon in lista_pokemones:
    #             if pokemon.id == int(id_pokemon):
    #                 lista_generacion_pokemones.append(pokemon)

    # for movimiento in lista_movimientos:
    #     if team.generacion == movimiento.generacion:
    #         lista_generacion_movimientos.append(movimiento)

    # pokemon_elegido = []
    # movimiento_elegido = []
    # for pokemon_team in team.pokemones:
    #     for p in lista_generacion_pokemones:
    #         if p.id == pokemon_team.id:
    #             pokemon_elegido.append(p)
    # for movimiento_team in team.pokemones:
    #     for m in lista_generacion_movimientos:
    #         if m.id in movimiento_team.movimientos:
    #             movimiento_elegido.append(m)

    # if len(pokemon_elegido) == 0:
    #     raise HTTPException(
    #         status_code=404,
    #         detail="Pokemon seleccionado no encontrado en la generacion",
    #     )

    # if len(movimiento_elegido) == 0:
    #     raise HTTPException(
    #         status_code=404, detail="Movimiento no encontrado en la generacion"
    #     )

    # nuevo_equipo = {"pokemon": pokemon_elegido, "movimiento": movimiento_elegido}

    # lista_equipos.append(nuevo_equipo)

    # return nuevo_equipo


"""
@router.put("/{id}")
def update(session: SessionDep, id: int, equipo_nuevo: Integrante) -> list[Integrante]:
    equipo = utils.buscar_equipo(session, id)
    equipo.nombre = equipo_nuevo.nombre
    equipo.pokemones = equipo_nuevo.pokemones
    session.add()
    session.commit()
    session.refresh(equipo)
    return equipo


@router.delete("/{id}")
def delete(session: SessionDep, id: int) -> Team:
    equipo = utils.buscar_equipo(session, id)
    session.delete(equipo)
    session.commit()
    return equipo
"""