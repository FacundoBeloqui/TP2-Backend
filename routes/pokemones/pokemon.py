from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from database import SessionDep
from db import (
    debilidades_tipos,
    fortalezas_tipos,
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
from modelos import Pokemon, PokemonPublic, PokemonPublicWithRelations
import routes.utils as utils

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
def get_pokemones(session: SessionDep) -> list[PokemonPublic]:
    query = select(Pokemon)
    pokemones = session.exec(query)
    return pokemones


@router.get("/{id}")
def show(session: SessionDep, id: int) -> PokemonPublicWithRelations:
    pokemon = session.exec(select(Pokemon).where(Pokemon.id == id)).first()

    if pokemon:
        pokemon_public_data = {
            "id": pokemon.id,
            "identificador": pokemon.identificador,
            "altura": pokemon.altura,
            "peso": pokemon.peso,
            "experiencia_base": pokemon.experiencia_base,
            "imagen": pokemon.imagen,
            "grupo_de_huevo": pokemon.grupo_de_huevo,
        }

        return PokemonPublicWithRelations(
            **pokemon_public_data,
            debilidades=calcular_debilidades(pokemon),
            fortalezas=calcular_fortalezas(pokemon),
        )


@router.delete("/{id}")
def delete(session: SessionDep, id: int) -> PokemonPublic:
    pokemon = utils.buscar_pokemon(session, id)
    session.delete(pokemon)
    session.commit()
    return pokemon


"""
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
