from sqlmodel import Field, SQLModel, Relationship, JSON
from typing import List, Dict, Optional
import sqlalchemy as sa
from integrante import Integrante


class PokemonBase(SQLModel):
    identificador: str
    altura: int
    peso: int
    experiencia_base: int
    imagen: str
    grupo_de_huevo: str


class Pokemon(PokemonBase, table=True):
    id: int = Field(primary_key=True)
    id_especie: int
    integrantes: List["Integrante"] = Relationship(back_populates="pokemon")

    habilidades: Optional[List[str]] = Field(default=None, sa_column=sa.Column(JSON))
    evoluciones_inmediatas: Optional[List[str]] = Field(
        default=None, sa_column=sa.Column(JSON)
    )
    tipo: Optional[List[str]] = Field(default=None, sa_column=sa.Column(JSON))
    estadisticas: Optional[Dict[str, int]] = Field(
        default=None, sa_column=sa.Column(JSON)
    )


class PokemonCreate(PokemonBase):
    pass
