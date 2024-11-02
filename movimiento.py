from sqlmodel import Field, SQLModel, Relationship
from typing import List, Dict, Optional
from integrante_movimiento import IntegranteMovimiento
from integrante import Integrante
from models import PokemonSubidaNivel, PokemonGrupoHuevo, PokemonTM


class Movimiento(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    generacion: int
    tipo: str
    poder: str
    accuracy: str
    pp: str
    generacion: int
    categoria: str
    efecto: str

    pokemones_subida_nivel: list["PokemonSubidaNivel"] = Relationship(
        back_populates="movimiento"
    )
    pokemones_tm: list["PokemonTM"] = Relationship(back_populates="movimiento")
    pokemones_grupo_huevo: list["PokemonGrupoHuevo"] = Relationship(
        back_populates="movimiento"
    )
    integrantes: List["Integrante"] = Relationship(
        back_populates="movimientos",
        link_model=IntegranteMovimiento,
    )
