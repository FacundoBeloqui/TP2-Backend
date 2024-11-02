from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship, Column
from sqlalchemy import JSON


class TipoBase(SQLModel):
    nombre: str


class Tipo(TipoBase, table=True):
    id: int = Field(primary_key=True)
    pokemones: list["Pokemon"] = Relationship(back_populates="tipos")


class HabilidadBase(SQLModel):
    nombre: str


class Habilidad(HabilidadBase, table=True):
    id: int = Field(primary_key=True)
    pokemones: list["Pokemon"] = Relationship(back_populates="habilidades")


class EvolucionBase(SQLModel):
    nombre: str


class Evolucion(EvolucionBase, table=True):
    id: int = Field(primary_key=True)
    pokemon_id: int = Field(foreign_key="pokemon.id")
    pokemon: "Pokemon" = Relationship(back_populates="evoluciones_inmediatas")


class PokemonBase(SQLModel):
    identificador: str
    altura: int
    peso: int
    experiencia_base: int
    imagen: str
    grupo_de_huevo: str
    estadisticas: dict[str, int] = Field(sa_column=Column(JSON))


class Pokemon(PokemonBase, table=True):
    id: int = Field(primary_key=True)
    id_especie: int
    evoluciones_inmediatas: list[Evolucion] = Relationship(back_populates="pokemon")
    habilidades: list[Habilidad] = Relationship(back_populates="pokemon")
    tipos: list[Tipo] = Relationship(back_populates="pokemon")


class PokemonCreate(PokemonBase):
    pass


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

    pokemones_subida_nivel: list["PokemonSubidaNivel"] = Relationship(
        back_populates="movimiento"
    )
    pokemones_tm: list["PokemonTM"] = Relationship(back_populates="movimiento")
    pokemones_grupo_huevo: list["PokemonGrupoHuevo"] = Relationship(
        back_populates="movimiento"
    )


class PokemonSubidaNivel(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    movimiento_id: int = Field(foreign_key="movimiento.id")
    movimiento: "Movimiento" = Relationship(back_populates="pokemones_subida_nivel")


class PokemonTM(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    movimiento_id: int = Field(foreign_key="movimiento.id")
    movimiento: "Movimiento" = Relationship(back_populates="pokemones_tm")


class PokemonGrupoHuevo(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    movimiento_id: int = Field(foreign_key="movimiento.id")
    movimiento: "Movimiento" = Relationship(back_populates="pokemones_grupo_huevo")


class PokemonTeamCreate(SQLModel):
    id: int
    nombre: str
    movimientos: list[int] = Field(sa_column=Column(JSON))
    naturaleza_id: int
    stats: dict[str, int] = Field(sa_column=Column(JSON))


class TeamBase(SQLModel):
    generacion: int
    nombre: str
    pokemones: list["PokemonTeamCreate"] = Relationship(back_populates="team")


# class TeamDataCreate(TeamBase, table=True):
#   id: int = Field(primary_key=True)
# nombre: str
# generacion: int
# pokemones: list[PokemonTeamCreate]


# class TeamCreate(TeamBase):
#     pass


class Naturaleza(SQLModel, table=True):
    id: int = Field(primary_key=True)
    nombre: str
    stat_decreciente: str
    stat_creciente: str
    id_gusto_preferido: int
    id_gusto_menos_preferido: int
    indice_juego: int


class Teams(SQLModel):
    id: int
    nombre: str
    pokemones: list["Pokemon"] = Relationship(back_populates="teams")


class Movimientomoves(SQLModel):
    id: int
    nombre: str
    nivel: int = None
    es_evolucionado: bool = False


class Pokemonmoves(SQLModel):
    id: int
    nombre: str
    tipos: list["Tipo"] = Relationship(back_populates="pokemon_moves")


class Evolucion(SQLModel):
    id_pokemon_base: int
    id_pokemon_evolucionado: int


class DatosMovimiento(SQLModel):
    movimientos: dict[int, Movimiento]
