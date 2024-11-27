from fastapi import APIRouter
from routes.pokemones import pokemon
from routes.movimientos import movimiento
from routes.teams import teams
from routes.naturalezas import naturaleza

api_router = APIRouter()
api_router.include_router(pokemon.router, prefix="/pokemones")
api_router.include_router(movimiento.router, prefix="/movimientos")
api_router.include_router(teams.router, prefix="/teams")
api_router.include_router(naturaleza.router, prefix="/naturalezas")
