from sqlmodel import Field, SQLModel, Relationship, JSON
from typing import List, Dict, Optional
import sqlalchemy as sa
from integrante import Integrante
from models import Tipo, Evolucion, Habilidad
from equipo import TeamDataCreate

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
    equipo_id: int | None = Field(default=None, foreign_key="equipo.id")
    equipo: TeamDataCreate | None = Relationship(back_populates="pokemones")
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
