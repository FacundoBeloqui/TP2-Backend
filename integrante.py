# from sqlmodel import Field, SQLModel, Relationship
# from typing import List, Dict, Optional
# from integrante_movimiento import IntegranteMovimiento
# from pokemon import Pokemon
# from naturaleza import Naturaleza
# from movimiento import Movimiento


# class Integrante(SQLModel, table=True):
#     nombre: str = Field(primary_key=True, nullable=False)
#     id_equipo: int
#     id_pokemon: Optional[int] = Field(default=None, foreign_key="pokemon.id")
#     pokemon: "Pokemon" = Relationship(back_populates="integrantes")
#     id_naturaleza: Optional[int] = Field(default=None, foreign_key="naturaleza.id")
#     naturaleza: Optional["Naturaleza"] = Relationship(back_populates="integrantes")
#     movimientos: List["Movimiento"] = Relationship(
#         back_populates="integrantes",
#         link_model=IntegranteMovimiento,
#     )
# from naturaleza import Naturaleza
# from pokemon import Pokemon
# from movimiento import Movimiento
