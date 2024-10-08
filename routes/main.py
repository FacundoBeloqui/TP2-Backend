from fastapi import APIRouter
from routes.pokemones import pokemon

api_router = APIRouter()
api_router.include_router(pokemon.router, prefix="/pokemones")
