from typing import List, Dict, Optional
from sqlmodel import Field, SQLModel, Relationship
from integrante import Integrante


class Naturaleza(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    stat_decreciente: str
    stat_creciente: str
    id_gusto_preferido: int
    id_gusto_menos_preferido: int
    indice_juego: int
    integrantes: List["Integrante"] = Relationship(back_populates="naturaleza")
