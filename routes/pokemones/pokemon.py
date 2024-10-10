from fastapi import HTTPException, APIRouter
from db import lista_pokemones, pokemon_tipos, debilidades_tipos, Pokemon


router = APIRouter()


def calcular_debilidades(pokemon_id):
    debilidades_totales = {}
    for tipo in pokemon_tipos.get(pokemon_id, []):
        for debilidad, efect in debilidades_tipos[tipo].items():
            if debilidad not in debilidades_totales:
                debilidades_totales[debilidad] = 1
            debilidades_totales[debilidad] *= int(efect) / 100
    return debilidades_totales


@router.get("/")
def leer_pokemones():
    lista = []
    for pokemon in lista_pokemones:
        lista += pokemon + calcular_debilidades(pokemon.id) + ","
    return lista


@router.delete("/{id}")
def eliminar_pokemon(id):
    if not id.isdecimal():
        raise HTTPException(status_code=400, detail="El id debe ser un numero entero")
    for pokemon in lista_pokemones:
        if pokemon.id == int(id):
            lista_pokemones.remove(pokemon)
            return pokemon
    raise HTTPException(status_code=404, detail="Pokemon no encontrado")
