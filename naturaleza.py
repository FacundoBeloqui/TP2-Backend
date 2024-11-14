# from sqlmodel import Field, SQLModel, Relationship, JSON
# from typing import List, Dict, Optional
# import sqlalchemy as sa


# class PokemonSubidaNivel(SQLModel, table=True):
#     id: int = Field(primary_key=True)
#     nombre: str
#     movimiento_id: int = Field(foreign_key="movimiento.id")
#     movimiento: "Movimiento" = Relationship(back_populates="pokemones_subida_nivel")


# class PokemonTM(SQLModel, table=True):
#     id: int = Field(primary_key=True)
#     nombre: str
#     movimiento_id: int = Field(foreign_key="movimiento.id")
#     movimiento: "Movimiento" = Relationship(back_populates="pokemones_tm")


# class PokemonGrupoHuevo(SQLModel, table=True):
#     id: int = Field(primary_key=True)
#     nombre: str
#     movimiento_id: int = Field(foreign_key="movimiento.id")
#     movimiento: "Movimiento" = Relationship(back_populates="pokemones_grupo_huevo")


# class Naturaleza(SQLModel, table=True):
#     id: int = Field(primary_key=True)
#     nombre: str
#     stat_decreciente: str
#     stat_creciente: str
#     id_gusto_preferido: int
#     id_gusto_menos_preferido: int
#     indice_juego: int
#     integrantes: List["Integrante"] = Relationship(back_populates="naturaleza")




