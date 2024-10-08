from fastapi import HTTPException, APIRouter
from db import lista_pokemones, Pokemon


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
