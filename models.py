from typing import List, Dict, Optional
from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship

class TipoBase(SQLModel):
    nombre: str

class Tipo(TipoBase, table=True):
    id: int = Field(primary_key=True)
    pokemones: list["Pokemon"] = Relationship(back_populates="tipo")


class HabilidadBase(SQLModel):
    nombre: str

class Habilidad(HabilidadBase, table=True):
    id: int = Field(primary_key=True)
    pokemones: list["Pokemon"] = Relationship(back_populates="habilidad")


class EvolucionBase(SQLModel):
    nombre: str

class Evolucion(EvolucionBase, table=True):
    id: int = Field(primary_key=True)
    pokemon_id: int = Field(foreign_key="pokemon.id")
    pokemon: "Pokemon" = Relationship(back_populates="evolucion")

class PokemonBase(SQLModel):
    identificador: str
    altura: int
    peso: int
    experiencia_base: int
    imagen: str
    grupo_de_huevo: str
    estadisticas: dict
    evoluciones_inmediatas: List[Evolucion] = Relationship(back_populates="pokemon")

class Pokemon(PokemonBase, table=True):
    id: int = Field(primary_key=True)
    id_especie: int
    habilidades: List[Habilidad] = Relationship(back_populates="pokemones")
    tipos: List[Tipo] = Relationship(back_populates="pokemones")


class PokemonTipo(SQLModel, table=True):
    pokemon_id: int = Field(foreign_key="pokemon.id", primary_key=True)
    tipo_id: int = Field(foreign_key="tipo.id", primary_key=True)
    pokemon: Pokemon = Relationship(back_populates="pokemones_tipo")
    tipo: Tipo = Relationship(back_populates="pokemones")



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


class PokemonTeamCreate(SQLModel):
    id: int
    nombre: str
    movimientos: List[Optional[int]]
    naturaleza_id: int
    stats: dict


class TeamBase(SQLModel):
    generacion: int
    nombre: str
    pokemones: List[PokemonTeamCreate] = Relationship(back_populates="team")


class TeamDataCreate(TeamBase, table=True):
    id: int = Field(primary_key=True)
    # nombre: str
    # generacion: int
    # pokemones: List[PokemonTeamCreate]


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


class Teams(BaseModel):
    id: int
    nombre: str
    pokemones: List[str]


class Movimientomoves(BaseModel):
    id: int
    nombre: str
    nivel: Optional[int] = None
    es_evolucionado: bool = False


class Pokemonmoves(BaseModel):
    id: int
    nombre: str
    tipos: List[int]


class Evolucion(BaseModel):
    id_pokemon_base: int
    id_pokemon_evolucionado: int


class DatosMovimiento(BaseModel):
    movimientos: Dict[int, Movimiento]


class PokemonTeam(BaseModel):
    id: int
    nombre: str
    movimiento_1: Optional[int]
    movimiento_2: Optional[int]
    movimiento_3: Optional[int]
    movimiento_4: Optional[int]
    naturaleza_id: int
    stats: dict


class Team(BaseModel):
    id: int
    generacion: int
    nombre: str
    pokemon_1: Optional[PokemonTeam]
    pokemon_2: Optional[PokemonTeam]
    pokemon_3: Optional[PokemonTeam]
    pokemon_4: Optional[PokemonTeam]
    pokemon_5: Optional[PokemonTeam]
    pokemon_6: Optional[PokemonTeam]


lista_equipos: List[TeamDataCreate] = [
    {
        "id": 1,
        "nombre": "Equipo A",
        "generacion": 1,
        "pokemones": [
            {
                "id": 1,
                "nombre": "Pikachu",
                "movimientos": [1, 2],
                "naturaleza_id": 1,
                "stats": {},
            }
        ],
    },
    {
        "id": 2,
        "nombre": "Equipo B",
        "generacion": 2,
        "pokemones": [
            {
                "id": 2,
                "nombre": "Charmander",
                "movimientos": [2],
                "naturaleza_id": 1,
                "stats": {},
            }
        ],
    },
]

# lista_equipos: List[TeamDataCreate] = []
class DatosMovimiento(SQLModel):
    movimientos: dict[int, Movimiento]

