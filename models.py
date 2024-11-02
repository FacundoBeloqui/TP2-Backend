from typing import List, Dict, Optional
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship


class PokemonTeamCreate(BaseModel):
    id: int
    nombre: str
    movimientos: List[Optional[int]]
    naturaleza_id: int
    stats: dict


class TeamDataCreate(BaseModel):
    id: int
    nombre: str
    generacion: int
    pokemones: List[PokemonTeamCreate]


class TeamCreate(BaseModel):
    generacion: int
    nombre: str
    pokemones: List[PokemonTeamCreate]


class Teams(BaseModel):
    id: int
    nombre: str
    pokemones: List[str]


class Movimientomoves(BaseModel):
    id: int
    nombre: str
    nivel: Optional[int] = None
    es_evolucionado: bool = False


class Pokemonmoves(BaseModel):
    id: int
    nombre: str
    tipos: List[int]


class Evolucion(BaseModel):
    id_pokemon_base: int
    id_pokemon_evolucionado: int


# class DatosMovimiento(BaseModel):
#    movimientos: Dict[int, Movimiento]


class PokemonTeam(BaseModel):
    id: int
    nombre: str
    movimiento_1: Optional[int]
    movimiento_2: Optional[int]
    movimiento_3: Optional[int]
    movimiento_4: Optional[int]
    naturaleza_id: int
    stats: dict


class Team(BaseModel):
    id: int
    generacion: int
    nombre: str
    pokemon_1: Optional[PokemonTeam]
    pokemon_2: Optional[PokemonTeam]
    pokemon_3: Optional[PokemonTeam]
    pokemon_4: Optional[PokemonTeam]
    pokemon_5: Optional[PokemonTeam]
    pokemon_6: Optional[PokemonTeam]


lista_equipos: List[TeamDataCreate] = [
    {
        "id": 1,
        "nombre": "Equipo A",
        "generacion": 1,
        "pokemones": [
            {
                "id": 1,
                "nombre": "Pikachu",
                "movimientos": [1, 2],
                "naturaleza_id": 1,
                "stats": {},
            }
        ],
    },
    {
        "id": 2,
        "nombre": "Equipo B",
        "generacion": 2,
        "pokemones": [
            {
                "id": 2,
                "nombre": "Charmander",
                "movimientos": [2],
                "naturaleza_id": 1,
                "stats": {},
            }
        ],
    },
]

# lista_equipos: List[TeamDataCreate] = []
