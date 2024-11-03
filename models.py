"""from typing import List, Dict, Optional, Annotated
from sqlmodel import (
    Field,
    SQLModel,
    Relationship,
    Column,
    JSON,
    create_engine,
    Session,
    select,
)
from fastapi import Depends, logger




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


class PokemonTipo(SQLModel, table=True):
    pokemon_id: int = Field(foreign_key="pokemon.id", primary_key=True)
    tipo_id: int = Field(foreign_key="tipo.id", primary_key=True)
    pokemon: "Pokemon" = Relationship(back_populates="pokemones_tipo")
    tipo: Tipo = Relationship(back_populates="pokemones")





class PokemonTeamCreate(SQLModel):
    id: int
    nombre: str
    movimientos: list[int] = Field(sa_column=Column(JSON))
    naturaleza_id: int
    stats: dict[str, int] = Field(sa_column=Column(JSON))


class TeamBase(SQLModel):
    generacion: int
    nombre: str
    pokemones: list["PokemonTeamCreate"] = Relationship(back_populates="team")


# class TeamDataCreate(TeamBase, table=True):
#   id: int = Field(primary_key=True)
# nombre: str
# generacion: int
# pokemones: list[PokemonTeamCreate]


# class TeamCreate(TeamBase):
#     pass


class Teams(SQLModel):
    id: int
    nombre: str
    pokemones: list["Pokemon"] = Relationship(back_populates="teams")


class Movimientomoves(SQLModel):
    id: int
    nombre: str
    nivel: int = None
    es_evolucionado: bool = False


class Pokemonmoves(SQLModel):
    id: int
    nombre: str
    tipos: list["Tipo"] = Relationship(back_populates="pokemon_moves")


class Evolucion(SQLModel):
    id_pokemon_base: int
    id_pokemon_evolucionado: int


class DatosMovimiento(SQLModel):
    movimientos: dict[int, "Movimiento"]

"""
