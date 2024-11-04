"""from typing import List, Dict, Optional, Annotated
from sqlmodel import (
    Field,
    SQLModel,
    Relationship,
    Column,
    JSON,
    create_engine,
    Session,
    select,
)
from fastapi import Depends, logger




class TipoBase(SQLModel):
    nombre: str

class Tipo(TipoBase, table=True):
    id: int = Field(primary_key=True)
    #pokemones: list["Pokemon"] = Relationship(back_populates="tipo")
    pokemon_id: int = Field(foreign_key="pokemon_id")


class HabilidadBase(SQLModel):
    nombre: str

class Habilidad(HabilidadBase, table=True):
    id: int = Field(primary_key=True)
    # pokemones: list["Pokemon"] = Relationship(back_populates="habilidad")
    pokemones: List["Pokemon"] = Relationship(back_populates="habilidad")


class EvolucionBase(SQLModel):
    nombre: str

class Evolucion(EvolucionBase, table=True):
    id: int = Field(primary_key=True)
    pokemon_id: int = Field(foreign_key="pokemon.id")
    pokemon: "Pokemon" = Relationship(back_populates="evolucion")


# class PokemonTipo(SQLModel, table=True):
#     pokemon_id: int = Field(foreign_key="pokemon.id", primary_key=True)
#     tipo_id: int = Field(foreign_key="tipo.id", primary_key=True)
#     pokemon: "Pokemon" = Relationship(back_populates="pokemones_tipo")
#     tipo: Tipo = Relationship(back_populates="pokemones")


class IntegranteMovimiento(SQLModel, table=True):
    integrante_id: int = Field(
        nullable=False, foreign_key="integrante.id", primary_key=True
    )
    movimiento_id: int = Field(
        nullable=False, foreign_key="movimiento.id", primary_key=True
    )



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
    # pokemones_subida_nivel: list["PokemonSubidaNivel"] = Relationship(
    #     back_populates="movimiento"
    # )
    pokemones_subida_nivel: List["PokemonSubidaNivel"] = Relationship(
        back_populates="movimiento"
    )
    # pokemones_tm: list["PokemonTM"] = Relationship(back_populates="movimiento")
    pokemones_tm: List["PokemonTM"] = Relationship(back_populates="movimiento")
    # pokemones_grupo_huevo: list["PokemonGrupoHuevo"] = Relationship(
    #     back_populates="movimiento"
    # )
    pokemones_grupo_huevo: List["PokemonGrupoHuevo"] = Relationship(
        back_populates="movimiento"
    )
    integrantes: List["Integrante"] = Relationship(
        back_populates="movimientos",
        link_model=IntegranteMovimiento,
    )


class PokemonSubidaNivel(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    movimiento_id: int = Field(foreign_key="movimiento.id")
    movimiento: Optional[Movimiento] = Relationship(
        back_populates="pokemones_subida_nivel"
    )


class PokemonTM(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    movimiento_id: int = Field(foreign_key="movimiento.id")
    movimiento: Optional[Movimiento] = Relationship(back_populates="pokemones_tm")


class PokemonGrupoHuevo(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    movimiento_id: int = Field(foreign_key="movimiento.id")
    movimiento: Optional[Movimiento] = Relationship(
        back_populates="pokemones_grupo_huevo"
    )




# class PokemonTeamCreate(SQLModel):
#     id: int
#     nombre: str
#     movimientos: List[Optional[int]]
#     naturaleza_id: int
#     stats: dict


# class TeamBase(SQLModel):
#     generacion: int
#     nombre: str
#     pokemones: List[PokemonTeamCreate] = Relationship(back_populates="team")


# class TeamDataCreate(TeamBase, table=True):
#     id: int = Field(primary_key=True)
    # nombre: str
    # generacion: int
    # pokemones: List[PokemonTeamCreate]


# class TeamCreate(TeamBase):
#     pass


class Teams(SQLModel):
    id: int
    nombre: str
    pokemones: List[str]


# class Movimientomoves(BaseModel):
#     id: int
#     nombre: str
#     nivel: Optional[int] = None
#     es_evolucionado: bool = False


# class Pokemonmoves(BaseModel):
#     id: int
#     nombre: str
#     tipos: List[int]


# class Evolucion(BaseModel):
#     id_pokemon_base: int
#     id_pokemon_evolucionado: int


# class DatosMovimiento(BaseModel):
#     movimientos: Dict[int, Movimiento]


# lista_equipos: List[TeamDataCreate] = [
#     {
#         "id": 1,
#         "nombre": "Equipo A",
#         "generacion": 1,
#         "pokemones": [
#             {
#                 "id": 1,
#                 "nombre": "Pikachu",
#                 "movimientos": [1, 2],
#                 "naturaleza_id": 1,
#                 "stats": {},
#             }
#         ],
#     },
#     {
#         "id": 2,
#         "nombre": "Equipo B",
#         "generacion": 2,
#         "pokemones": [
#             {
#                 "id": 2,
#                 "nombre": "Charmander",
#                 "movimientos": [2],
#                 "naturaleza_id": 1,
#                 "stats": {},
#             }
#         ],
#     },
# ]

# lista_equipos: List[TeamDataCreate] = []
class DatosMovimiento(SQLModel):
    movimientos: dict[int, "Movimiento"]


    



class PokemonBase(SQLModel):
    identificador: str
    altura: int
    peso: int
    experiencia_base: int
    imagen: str
    grupo_de_huevo: str
    habilidades: Optional[List[str]] = Field(default=None, sa_column=sa.Column(JSON))
    evoluciones_inmediatas: Optional[List[str]] = Field(
        default=None, sa_column=sa.Column(JSON)
    )
    tipo: Optional[List[Tipo]] = Relationship(back_populates="pokemon_id")
    estadisticas: Optional[Dict[str, int]] = Field(
        default=None, sa_column=sa.Column(JSON)
    )


class Pokemon(PokemonBase, table=True):
    id: int = Field(primary_key=True)
    id_especie: int
    #equipo_id: int | None = Field(default=None, foreign_key="equipo.id")
    #equipo: TeamDataCreate | None = Relationship(back_populates="pokemones")
    #integrantes: List["Integrante"] = Relationship(back_populates="pokemon")


class PokemonCreate(PokemonBase):
    pass



class Integrante(SQLModel, table=True):
    nombre: str = Field(primary_key=True, nullable=False)
    id_equipo: int
    id_pokemon: Optional[int] = Field(default=None, foreign_key="pokemon.id")
    pokemon: "Pokemon" = Relationship(back_populates="integrantes")
    id_naturaleza: Optional[int] = Field(default=None, foreign_key="naturaleza.id")
    naturaleza: Optional["Naturaleza"] = Relationship(back_populates="integrantes")
    movimientos: List["Movimiento"] = Relationship(
        back_populates="integrantes",
        link_model=IntegranteMovimiento,
    )



class Naturaleza(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    stat_decreciente: str
    stat_creciente: str
    id_gusto_preferido: int
    id_gusto_menos_preferido: int
    indice_juego: int
    integrantes: List["Integrante"] = Relationship(back_populates="naturaleza")




class PokemonTeamCreate(SQLModel):
    id: int
    nombre: str
    movimientos: List[Optional[int]]
    naturaleza_id: int
    stats: dict

class TeamBase(SQLModel):
    generacion: int
    nombre: str
    #pokemones: list["PokemonTeamCreate"] = Relationship(back_populates="equipo")
    # pokemones: list["Integrante"] = Relationship(back_populates="equipo")
    pokemones: List["Integrante"] = Relationship(back_populates="equipo")



class TeamDataCreate(TeamBase, table=True):
    id: int = Field(primary_key=True)
    # nombre: str
    # generacion: int
    # pokemones: List[PokemonTeamCreate]


# class TeamCreate(TeamBase):
#     pass
"""