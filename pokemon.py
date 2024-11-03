from sqlmodel import Field, SQLModel, Relationship
from typing import List, Dict, Optional
from integrante import Integrante
from models import Tipo, Evolucion, Habilidad
from equipo import TeamDataCreate

class PokemonBase(SQLModel):
    identificador: str
    altura: int
    peso: int
    experiencia_base: int
    imagen: str
    tipos: list[Tipo] = Relationship(back_populates="pokemones")
    grupo_de_huevo: str
    estadisticas: dict
    evoluciones_inmediatas: list[Evolucion] = Relationship(back_populates="pokemon")
    habilidades: list[Habilidad] = Relationship(back_populates="pokemones")


class Pokemon(PokemonBase, table=True):
    id: int = Field(primary_key=True)
    id_especie: int
    equipo_id: int | None = Field(default=None, foreign_key="equipo.id")
    equipo: TeamDataCreate | None = Relationship(back_populates="pokemones")
    integrantes: List["Integrante"] = Relationship(back_populates="pokemon")


class PokemonCreate(PokemonBase):
    pass
