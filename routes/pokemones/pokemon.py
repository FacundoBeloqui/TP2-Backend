from fastapi import APIRouter, HTTPException, status
from sqlmodel import select
from database import SessionDep
from db import (
    debilidades_tipos,
    fortalezas_tipos,
    lista_pokemones,
    movimientos_aprendibles_por_pokemon,
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
from modelos import Pokemon, PokemonPublic, PokemonPublicWithRelations, PokemonCreate
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
def get_pokemones(session: SessionDep) -> list[Pokemon]:
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
            "id_especie": pokemon.id_especie,
            "altura": pokemon.altura,
            "peso": pokemon.peso,
            "experiencia_base": pokemon.experiencia_base,
            "imagen": pokemon.imagen,
            "grupo_de_huevo": pokemon.grupo_de_huevo,
            "generacion": pokemon.generacion,
            "tipo": pokemon.tipo,
            "estadisticas": pokemon.estadisticas,
            "habilidades": pokemon.habilidades,
            "evoluciones_inmediatas": pokemon.evoluciones_inmediatas,
        }

        return PokemonPublicWithRelations(
            **pokemon_public_data,
            debilidades=calcular_debilidades(pokemon),
            fortalezas=calcular_fortalezas(pokemon),
        )
    else:
        raise (
            HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado"
            )
        )


@router.delete("/{id}")
def delete(session: SessionDep, id: int) -> PokemonPublic:
    if id <= 0:
        raise HTTPException(
            status_code=400, detail="El id debe ser un numero entero positivo"
        )

    pokemon = session.get(Pokemon, id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado")
    session.delete(pokemon)
    session.commit()
    return pokemon


@router.post("/", response_model=Pokemon, status_code=201)
def create_pokemon(session: SessionDep, pokemon_create: PokemonCreate):
    pokemon = Pokemon(
        id_especie=pokemon_create.id_especie,
        identificador=pokemon_create.identificador,
        altura=pokemon_create.altura,
        peso=pokemon_create.peso,
        experiencia_base=pokemon_create.experiencia_base,
        imagen=pokemon_create.imagen,
        tipo=pokemon_create.tipo,
        grupo_de_huevo=pokemon_create.grupo_de_huevo,
        generacion=pokemon_create.generacion,
        estadisticas=pokemon_create.estadisticas,
        habilidades=pokemon_create.habilidades,
        evoluciones_inmediatas=pokemon_create.evoluciones_inmediatas,
    )
    session.add(pokemon)
    session.commit()
    session.refresh(pokemon)
    return pokemon


@router.get("/{pokemon_id}/movimientos")
def obtener_movimientos_pokemon(pokemon_id: int):
    pokemon = movimientos_aprendibles_por_pokemon[str(pokemon_id)]
    if not pokemon:
        raise (
            HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Pokemon no encontrado"
            )
        )
    else:
        return pokemon
