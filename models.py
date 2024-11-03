from typing import List, Dict, Optional
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship, Column, JSON
from pokemon import Pokemon
from movimiento import Movimiento


class TipoBase(SQLModel):
    nombre: str

class Tipo(TipoBase, table=True):
    id: int = Field(primary_key=True)
    pokemones: list["Pokemon"] = Relationship(back_populates="tipo")


class HabilidadBase(SQLModel):
    nombre: str

class Habilidad(HabilidadBase, table=True):
    id: int = Field(primary_key=True)
    pokemones: list["Pokemon"] = Relationship(back_populates="habilidad")


class EvolucionBase(SQLModel):
    nombre: str

class Evolucion(EvolucionBase, table=True):
    id: int = Field(primary_key=True)
    pokemon_id: int = Field(foreign_key="pokemon.id")
    pokemon: "Pokemon" = Relationship(back_populates="evolucion")


# class PokemonTipo(SQLModel, table=True):
#     pokemon_id: int = Field(foreign_key="pokemon.id", primary_key=True)
#     tipo_id: int = Field(foreign_key="tipo.id", primary_key=True)
#     pokemon: Pokemon = Relationship(back_populates="pokemones_tipo")
#     tipo: Tipo = Relationship(back_populates="pokemones")


class PokemonSubidaNivel(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    movimiento_id: int = Field(foreign_key="movimiento.id")
    movimiento: Optional[Movimiento] = Relationship(
        back_populates="pokemones_subida_nivel"
    )


class PokemonTM(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    movimiento_id: int = Field(foreign_key="movimiento.id")
    movimiento: Optional[Movimiento] = Relationship(back_populates="pokemones_tm")


class PokemonGrupoHuevo(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    movimiento_id: int = Field(foreign_key="movimiento.id")
    movimiento: Optional[Movimiento] = Relationship(
        back_populates="pokemones_grupo_huevo"
    )


class PokemonTeamCreate(SQLModel):
    id: int
    nombre: str
    movimientos: List[Optional[int]]
    naturaleza_id: int
    stats: dict


class TeamBase(SQLModel):
    generacion: int
    nombre: str
    pokemones: List[PokemonTeamCreate] = Relationship(back_populates="team")


class TeamDataCreate(TeamBase, table=True):
    id: int = Field(primary_key=True)
    # nombre: str
    # generacion: int
    # pokemones: List[PokemonTeamCreate]


# class TeamCreate(TeamBase):
#     pass


class Teams(SQLModel):
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


class DatosMovimiento(BaseModel):
    movimientos: Dict[int, Movimiento]


# lista_equipos: List[TeamDataCreate] = [
#     {
#         "id": 1,
#         "nombre": "Equipo A",
#         "generacion": 1,
#         "pokemones": [
#             {
#                 "id": 1,
#                 "nombre": "Pikachu",
#                 "movimientos": [1, 2],
#                 "naturaleza_id": 1,
#                 "stats": {},
#             }
#         ],
#     },
#     {
#         "id": 2,
#         "nombre": "Equipo B",
#         "generacion": 2,
#         "pokemones": [
#             {
#                 "id": 2,
#                 "nombre": "Charmander",
#                 "movimientos": [2],
#                 "naturaleza_id": 1,
#                 "stats": {},
#             }
#         ],
#     },
# ]

# lista_equipos: List[TeamDataCreate] = []
class DatosMovimiento(SQLModel):
    movimientos: dict[int, Movimiento]
