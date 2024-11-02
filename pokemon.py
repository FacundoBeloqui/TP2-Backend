from sqlmodel import Field, SQLModel, Relationship
from typing import List, Dict, Optional
from integrante import Integrante


class PokemonBase(SQLModel):
    identificador: str
    altura: int
    peso: int
    experiencia_base: int
    imagen: str
    tipo: list[str]
    grupo_de_huevo: str
    estadisticas: dict
    habilidades: list[str]
    evoluciones_inmediatas: list


class Pokemon(PokemonBase, table=True):
    id: int = Field(primary_key=True)
    id_especie: int
    integrantes: List["Integrante"] = Relationship(back_populates="pokemon")


class PokemonCreate(PokemonBase):
    pass
