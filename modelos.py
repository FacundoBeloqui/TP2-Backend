from sqlmodel import Field, SQLModel, Relationship, JSON
from typing import List, Dict, Optional
import sqlalchemy as sa


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


class Naturaleza(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    stat_decreciente: str
    stat_creciente: str
    id_gusto_preferido: int
    id_gusto_menos_preferido: int
    indice_juego: int
    integrantes: List["Integrante"] = Relationship(back_populates="naturaleza")


class PokemonBase(SQLModel):
    identificador: str
    altura: int
    peso: int
    experiencia_base: int
    imagen: str
    grupo_de_huevo: str
    generacion: List[int] = Field(default=None, sa_column=sa.Column(JSON))
    habilidades: Optional[List[str]] = Field(default=None, sa_column=sa.Column(JSON))
    evoluciones_inmediatas: Optional[List[str]] = Field(
        default=None, sa_column=sa.Column(JSON)
    )
    tipo: Optional[List[str]] = Field(default=None, sa_column=sa.Column(JSON))
    estadisticas: Optional[Dict[str, int]] = Field(
        default=None, sa_column=sa.Column(JSON)
    )
    id_especie: int

class Pokemon(PokemonBase, table=True):
    id: int = Field(primary_key=True)
    integrantes: List["Integrante"] = Relationship(back_populates="pokemon")


class PokemonCreate(PokemonBase):
    pass


class PokemonPublic(PokemonBase):
    id: int


class PokemonPublicWithRelations(PokemonBase):
    debilidades: dict[str, float]
    fortalezas: dict[str, float]


class IntegranteMovimiento(SQLModel, table=True):
    __tablename__="integrante_movimiento"
    integrante_id: int = Field(
        nullable=False, foreign_key="integrante.nombre", primary_key=True
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
    pokemones_subida_nivel: Optional[List[str]] = Field(
        default=None, sa_column=sa.Column(JSON)
    )
    pokemones_tm: Optional[List[str]] = Field(default=None, sa_column=sa.Column(JSON))
    pokemones_grupo_huevo: Optional[List[str]] = Field(
        default=None, sa_column=sa.Column(JSON)
    )
    # integrantes: List["Integrante"] = Relationship(
    #     back_populates="movimientos",
    #     link_model=IntegranteMovimiento,
    # )

# class IntegranteBase(SQLModel):
#     movimientos: List[Movimiento] = Relationship(
#         back_populates="integrantes",
#         link_model=IntegranteMovimiento,
#     )





class TeamBase(SQLModel):
    generacion: int
    nombre: str


class Team(TeamBase, table=True):
    __tablename__ = "equipo"
    id: int = Field(primary_key=True)
    integrantes: List["Integrante"] = Relationship(back_populates="equipo")

class TeamCreate(TeamBase):
    integrantes: List["IntegranteCreate"] 

class Integrante(SQLModel, table=True):
    nombre: str = Field(primary_key=True, nullable=False)
    id_equipo: Optional[int] = Field(default=None, foreign_key="equipo.id")
    equipo: Optional["Team"] = Relationship(back_populates="integrantes")
    id_pokemon: Optional[int] = Field(default=None, foreign_key="pokemon.id")
    pokemon: Optional[Pokemon] = Relationship(back_populates="integrantes")
    id_naturaleza: Optional[int] = Field(default=None, foreign_key="naturaleza.id")
    naturaleza: Optional[Naturaleza] = Relationship(back_populates="integrantes")
    # movimientos: Optional[List[Movimiento]] = Relationship(
    #     back_populates="integrantes",
    #     link_model=IntegranteMovimiento,
    # )

class IntegranteCreate(SQLModel):
    nombre: str
    id_pokemon: Optional[int] = None
    id_naturaleza: Optional[int] = None
    movimientos: Optional[List[int]] = []

