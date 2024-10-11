from fastapi import HTTPException, APIRouter
from db import lista_pokemones, Pokemon


router = APIRouter()

@router.get("/pokemon/{pokemon_id}", response_model=Pokemon)
def leer_pokemon(pokemon_id: int):
    pokemon = None
    for p in lista_pokemones:
        if p.id == pokemon_id:
            pokemon = p
            break
    
    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado")
    
    return pokemon
        
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
