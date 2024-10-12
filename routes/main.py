from fastapi import APIRouter
from routes.pokemones import pokemon
from routes.movimientos import movimiento

api_router = APIRouter()
api_router.include_router(pokemon.router, prefix="/pokemones")
api_router.include_router(movimiento.router, prefix="/movimientos")
