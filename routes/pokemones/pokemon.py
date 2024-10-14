from fastapi import HTTPException, APIRouter
from db import lista_pokemones, fortalezas_tipos, debilidades_tipos, Pokemon, PokemonCreate


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
def leer_pokemones():
    return lista_pokemones


@router.get("/{pokemon_id}")
def leer_pokemon(pokemon_id: int):
    pokemon = None
    for p in lista_pokemones:
        if p.id == pokemon_id:
            pokemon = p
            debilidades = calcular_debilidades(pokemon)
            fortalezas = calcular_fortalezas(pokemon)
            break

    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado")

    return {
        "pokemon": pokemon,
        "debilidades": debilidades,
        "fortalezas": fortalezas,
    }


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
def create_pokemon(pokemon: PokemonCreate):
    pokemon_id = len(lista_pokemones)
    nuevo_pokemon = Pokemon(
        id=pokemon_id,
        identificador=pokemon.identificador,
        id_especie=pokemon_id,
        altura=pokemon.altura,
        peso=pokemon.peso,
        experiencia_base=pokemon.experiencia_base,
        imagen=pokemon.imagen,
        tipo=pokemon.tipo,
        grupo_de_huevo=pokemon.grupo_de_huevo,
        estadisticas=pokemon.estadisticas,
        habilidades=pokemon.habilidades
    )
    lista_pokemones.append(nuevo_pokemon)
    return nuevo_pokemon