from fastapi import HTTPException, APIRouter
from db import lista_pokemones, Pokemon, PokemonCreate


router = APIRouter()


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
        tipo=pokemon.tipo
    )
    lista_pokemones.append(nuevo_pokemon)
    return nuevo_pokemon