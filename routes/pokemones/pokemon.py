from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from database import SessionDep
from db import (
    # SessionDep,
    lista_naturalezas,
    # lista_pokemones,
    # lista_movimientos,
    # lista_habilidades,
    # generaciones_pokemon,
    # pokemon_tipos,
)
from fastapi import HTTPException, APIRouter
from typing import List

# from models import (
#     TeamCreate,
#     TeamDataCreate,
#     Pokemon,
# )
from modelos import Pokemon

router = APIRouter()


def calcular_debilidades(pokemon):
    debilidades_totales = {}
    for tipo in pokemon.tipo:
        for debilidad, efect in debilidades_tipos.get(tipo, {}).items():
            if debilidad not in debilidades_totales:
                debilidades_totales[debilidad] = 1
            debilidades_totales[debilidad] *= int(efect) / 100
    return debilidades_totales


def calcular_fortalezas(pokemon):
    fortalezas_totales = {}
    for tipo in pokemon.tipo:
        for fortaleza, efect in fortalezas_tipos.get(tipo, {}).items():
            if fortaleza not in fortalezas_totales:
                fortalezas_totales[fortaleza] = 1
            fortalezas_totales[fortaleza] *= int(efect) / 100
    return fortalezas_totales


@router.get("/")
def get_pokemones(session: SessionDep) -> list[Pokemon]:
    query = select(Pokemon)
    pokemones = session.exec(query)
    return pokemones


@router.get("/{id}")
def show(session: SessionDep, id: int) -> Pokemon:
    pokemon = session.exec(select(Pokemon).where(Pokemon.id == id)).first()

    if pokemon:
        return pokemon
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon not found"
    )


"""
@router.delete("/{id}")
def eliminar_pokemon(id):
    if not id.isdecimal():
        raise HTTPException(status_code=400, detail="El id debe ser un numero entero")
    for pokemon in lista_pokemones:
        if pokemon.id == int(id):
            lista_pokemones.remove(pokemon)
            return {
                "pokemon": pokemon,
                "debilidades": calcular_debilidades(pokemon),
                "fortalezas": calcular_fortalezas(pokemon),
            }
    raise HTTPException(status_code=404, detail="Pokemon no encontrado")


@router.post("/", response_model=Pokemon, status_code=201)
def create_pokemon(session: SessionDep, pokemon: PokemonBase):
    session.add(pokemon)
    session.commit()
    session.refresh(pokemon)
    return pokemon


@router.get("/{pokemon_id}/movimientos")
def obtener_movimientos_pokemon(pokemon_id: int):
    if pokemon_id not in datos_pokemon:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado")

    pokemon = datos_pokemon[pokemon_id]

    if pokemon_id not in datos_movimientos_pokemon:
        raise HTTPException(
            status_code=404, detail="Movimientos no encontrados para este Pokémon"
        )

    movimientos = datos_movimientos_pokemon[pokemon_id]

    lista_movimientos = []

    movimientos_vistos = set()
    for movimiento in movimientos:
        id_movimiento = movimiento["id_movimiento"]
        nivel_movimiento = movimiento["nivel"]

        if id_movimiento not in movimientos_vistos:
            movimientos_vistos.add(id_movimiento)
            if id_movimiento in datos_movimientos.movimientos:
                nombre_movimiento = datos_movimientos.movimientos[id_movimiento].nombre
                lista_movimientos.append(
                    Movimientomoves(
                        id=id_movimiento,
                        nombre=nombre_movimiento,
                        nivel=nivel_movimiento,
                        es_evolucionado=False,
                    )
                )

    tipos = datos_tipos_pokemon.get(pokemon_id, [])

    return {
        "id_pokemon": pokemon.id,
        "nombre_pokemon": pokemon.nombre,
        "tipos": tipos,
        "movimientos": [movimiento.dict() for movimiento in lista_movimientos],
    }
"""
