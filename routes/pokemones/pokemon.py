from fastapi import HTTPException, APIRouter
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from db import lista_pokemones, fortalezas_tipos, debilidades_tipos, Pokemon


router = APIRouter()


def calcular_debilidades(pokemon):
    debilidades_totales = {}
    for tipo in pokemon.tipos:
        for debilidad, efect in debilidades_tipos.get(tipo, {}).items():
            if debilidad not in debilidades_totales:
                debilidades_totales[debilidad] = 1
            debilidades_totales[debilidad] *= int(efect) / 100
    return debilidades_totales


def calcular_fortalezas(pokemon):
    fortalezas_totales = {}
    for tipo in pokemon.tipos:
        for fortaleza, efect in fortalezas_tipos.get(tipo, {}).items():
            if fortaleza not in fortalezas_totales:
                fortalezas_totales[fortaleza] = 1
            fortalezas_totales[fortaleza] *= int(efect) / 100
    return fortalezas_totales


@router.get("/{id}")
def get_pokemon_id(id: int):
    for pokemon in lista_pokemones:
        if pokemon.id == id:
            return {
                "pokemon": pokemon,
                "debilidades": calcular_debilidades(pokemon),
                "fortalezas": calcular_fortalezas(pokemon),
            }
    raise HTTPException(status_code=404, detail="Pokémon no encontrado")


@router.get("/")
def leer_pokemones():
    return lista_pokemones


@router.delete("/{id}")
def eliminar_pokemon(id):
    if not id.isdecimal():
        raise HTTPException(status_code=400, detail="El id debe ser un numero entero")
    for pokemon in lista_pokemones:
        if pokemon.id == int(id):
            lista_pokemones.remove(pokemon)
            return pokemon
    raise HTTPException(status_code=404, detail="Pokemon no encontrado")
