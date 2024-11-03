from sqlmodel import Field, SQLModel, Relationship
from typing import List, Dict, Optional
from movimiento import Movimiento
from naturaleza import Naturaleza
from pokemon import Pokemon
from integrante_movimiento import IntegranteMovimiento


class Integrante(SQLModel, table=True):
    nombre: str = (Field(primary_key=True, nullable=False),)
    id_equipo: int
    id_pokemon: Optional[int] = Field(default=None, foreign_key="pokemon.id")
    pokemon: Pokemon = Relationship(back_populates="integrante")
    id_naturaleza: Optional[int] = Field(default=None, foreign_key="naturaleza.id")
    naturaleza: Optional[Naturaleza] = Relationship(back_populates="integrante")
    movimientos: List["Movimiento"] = Relationship(
        back_populates="integrante",
        link_model=IntegranteMovimiento,
    )
