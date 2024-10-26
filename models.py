from typing import List

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class Naturaleza(SQLModel):
    id: int
    nombre: str
    stat_decreciente: str
    stat_creciente: str
    id_gusto_preferido: int
    id_gusto_menos_preferido: int
    indice_juego: int
