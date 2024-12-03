from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from database import SessionDep
from fastapi import HTTPException, APIRouter
from modelos import (
    Naturaleza,
    Integrante,
    Team,
    Pokemon,
    Movimiento,
    TeamPublicWithIntegrantes,
    TeamCreate,
    TeamPublic,
    IntegranteCreate,
    IntegrantePublicWithMovimientos,
    IntegranteUpdate,
)
import routes.utils as utils


generacion = ""

router = APIRouter()


@router.get("/")
def obtener_equipos(session: SessionDep) -> list[Team]:
    query = select(Team)
    equipos = session.exec(query)
    return equipos


@router.get("/{team_id}")
def get_team_by_id(session: SessionDep, team_id: int) -> TeamPublicWithIntegrantes:
    return utils.buscar_equipo(session, team_id)


@router.post("/", response_model=TeamPublicWithIntegrantes)
def create_team(
    session: SessionDep, team_create: TeamCreate
) -> TeamPublicWithIntegrantes:
    if team_create.generacion < 1 or team_create.generacion > 9:
        raise HTTPException(status_code=400, detail="Generacion no permitida")

    if len(team_create.integrantes) < 1 or len(team_create.integrantes) > 6:
        raise HTTPException(
            status_code=400,
            detail="Debe elegir al menos 1 pokemon y no mas de 6 pokemones",
        )

    team = Team(generacion=team_create.generacion, nombre=team_create.nombre)

    session.add(team)
    session.commit()
    session.refresh(team)

    for integrante_data in team_create.integrantes:
        nombre_integrante = session.exec(
            select(Integrante).where(
                Integrante.nombre == integrante_data.nombre,
                Integrante.id_equipo == team.id,
            )
        ).first()

        if nombre_integrante:
            raise HTTPException(
                status_code=400,
                detail=f"Ya existe un integrante con el nombre {integrante_data.nombre} en el equipo.",
            )

        pokemon = session.exec(
            select(Pokemon).where(Pokemon.id == integrante_data.id_pokemon)
        ).first()
        naturaleza = session.exec(
            select(Naturaleza).where(Naturaleza.id == integrante_data.id_naturaleza)
        ).first()

        if not pokemon:
            raise HTTPException(status_code=404, detail="Pokemon no encontrado.")
        if team_create.generacion not in pokemon.generacion:
            raise HTTPException(
                status_code=400,
                detail="El pokemon elegido no pertenece a la generacion elegida.",
            )
        if not naturaleza:
            raise HTTPException(status_code=404, detail="Naturaleza no encontrada.")

        integrante = Integrante(
            nombre=integrante_data.nombre,
            equipo=team,
            pokemon=pokemon,
            naturaleza=naturaleza,
        )

        session.add(integrante)
        session.commit()
        session.refresh(integrante)

        if len(integrante_data.movimientos) < 1 or len(integrante_data.movimientos) > 4:
            raise HTTPException(
                status_code=400,
                detail="El pokemon no tiene la cantidad de movimientos requerida.",
            )

        for movimiento_id in integrante_data.movimientos:
            movimiento = session.exec(
                select(Movimiento).where(Movimiento.id == movimiento_id)
            ).first()
            if not movimiento:
                raise HTTPException(
                    status_code=404,
                    detail=f"Movimiento con id {movimiento_id} no encontrado.",
                )
            if movimiento.generacion > team_create.generacion:
                raise HTTPException(
                    status_code=400,
                    detail="El movimiento elegido no pertenece a la generacion elegida.",
                )
            integrante.movimientos.append(movimiento)
        session.commit()
        team.integrantes.append(integrante)
        session.commit()

    session.commit()
    session.refresh(team)

    return team


@router.put(
    "/{team_id}",
    response_model=IntegrantePublicWithMovimientos,
)
def update_integrante(
    team_id: int,
    session: SessionDep,
    integrante_update: IntegranteUpdate,
) -> IntegrantePublicWithMovimientos:

    team = session.exec(select(Team).where(Team.id == team_id)).first()
    if not team:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")

    integrante = session.exec(
        select(Integrante).where(
            Integrante.id == integrante_update.id_integrante,
            Integrante.id_equipo == team_id,
        )
    ).first()

    if not integrante:
        raise HTTPException(status_code=404, detail="Integrante no encontrado")

    pokemon = session.exec(
        select(Pokemon).where(Pokemon.id == integrante_update.id_pokemon)
    ).first()
    if team.generacion not in pokemon.generacion:
        raise HTTPException(
            status_code=400,
            detail="El pokemon no pertenece a la generacion del equipo",
        )
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon no encontrado.")

    naturaleza = session.exec(
        select(Naturaleza).where(Naturaleza.id == integrante_update.id_naturaleza)
    ).first()
    if not naturaleza:
        raise HTTPException(status_code=404, detail="Naturaleza no encontrada.")

    if len(integrante_update.movimientos) < 1 or len(integrante_update.movimientos) > 4:
        raise HTTPException(
            status_code=400,
            detail="El pokemon no tiene la cantidad de movimientos requerida.",
        )
    integrante.movimientos.clear()
    for movimiento_id in integrante_update.movimientos:
        movimiento = session.exec(
            select(Movimiento).where(Movimiento.id == movimiento_id)
        ).first()
        if not movimiento:
            raise HTTPException(
                status_code=404,
                detail=f"Movimiento con id {movimiento_id} no encontrado.",
            )
        if movimiento.generacion > team.generacion:
            raise HTTPException(
                status_code=400,
                detail="El movimiento elegido no pertenece a la generación elegida.",
            )
        if movimiento in integrante.movimientos:
            raise HTTPException(
                status_code=400,
                detail=f"El movimiento {movimiento.nombre} ya está asignado al Pokémon.",
            )
        integrante.movimientos.append(movimiento)
    integrante.nombre = integrante_update.nombre
    integrante.pokemon = pokemon
    integrante.naturaleza = naturaleza

    session.commit()
    session.refresh(integrante)

    return integrante


@router.post("/{team_id}")
def agregar_integrante(
    team_id: int, integrante_data: IntegranteCreate, session: SessionDep
):
    team = session.exec(select(Team).where(Team.id == team_id)).first()
    nombre_integrante = session.exec(
        select(Integrante).where(
            Integrante.nombre == integrante_data.nombre,
            Integrante.id_equipo == team.id,
        )
    ).first()

    if nombre_integrante:
        raise HTTPException(
            status_code=400,
            detail=f"Ya existe un integrante con el nombre {integrante_data.nombre} en el equipo.",
        )

    pokemon = session.exec(
        select(Pokemon).where(Pokemon.id == integrante_data.id_pokemon)
    ).first()
    naturaleza = session.exec(
        select(Naturaleza).where(Naturaleza.id == integrante_data.id_naturaleza)
    ).first()

    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon no encontrado.")
    if team.generacion not in pokemon.generacion:
        raise HTTPException(
            status_code=400,
            detail="El pokemon elegido no pertenece a la generacion elegida.",
        )
    if not naturaleza:
        raise HTTPException(status_code=404, detail="Naturaleza no encontrada.")

    integrante = Integrante(
        nombre=integrante_data.nombre,
        equipo=team,
        pokemon=pokemon,
        naturaleza=naturaleza,
    )

    session.add(integrante)
    session.commit()
    session.refresh(integrante)

    if len(integrante_data.movimientos) < 1 or len(integrante_data.movimientos) > 4:
        raise HTTPException(
            status_code=400,
            detail="El pokemon no tiene la cantidad de movimientos requerida.",
        )

    for movimiento_id in integrante_data.movimientos:
        movimiento = session.exec(
            select(Movimiento).where(Movimiento.id == movimiento_id)
        ).first()
        if not movimiento:
            raise HTTPException(
                status_code=404,
                detail=f"Movimiento con id {movimiento_id} no encontrado.",
            )
        if movimiento.generacion > team.generacion:
            raise HTTPException(
                status_code=400,
                detail="El movimiento elegido no pertenece a la generacion elegida.",
            )
        integrante.movimientos.append(movimiento)
    session.commit()
    team.integrantes.append(integrante)
    session.commit()
    return "Integrante creado exitosamente"


@router.delete("/{team_id}/{integrante_id}")
def eliminar_integrante(team_id: int, integrante_id: int, session: SessionDep):
    team = session.exec(select(Team).where(Team.id == team_id)).first()
    if not team:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    for integrante in team.integrantes:
        if integrante.id == integrante_id:
            integrante_delete = integrante
    if not integrante_delete:
        raise HTTPException(status_code=404, detail="Integrante no encontrado")
    session.delete(integrante_delete)
    session.commit()
    return integrante_delete


@router.delete("/{id}")
def delete(session: SessionDep, id: int) -> TeamPublic:
    equipo = utils.buscar_equipo(session, id)
    for integrante in equipo.integrantes:
        session.delete(integrante)
    session.delete(equipo)
    session.commit()
    return equipo
