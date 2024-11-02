from sqlmodel import Field, SQLModel, Relationship
from typing import List, Dict, Optional
from integrante_movimiento import IntegranteMovimiento
from integrante import Integrante


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
    pokemones_subida_nivel: List[str]
    pokemones_tm: List[str]
    pokemones_grupo_huevo: List[str]
    integrantes: List["Integrante"] = Relationship(
        back_populates="movimientos",
        link_model=IntegranteMovimiento,
    )
