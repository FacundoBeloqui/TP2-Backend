# from sqlmodel import Field, SQLModel, Relationship
# from typing import List, Dict, Optional
# from integrante import Integrante


# class PokemonTeamCreate(SQLModel):
#     id: int
#     nombre: str
#     movimientos: List[Optional[int]]
#     naturaleza_id: int
#     stats: dict

# class TeamBase(SQLModel):
#     generacion: int
#     nombre: str
#     #pokemones: list["PokemonTeamCreate"] = Relationship(back_populates="equipo")
#     pokemones: list["Integrante"] = Relationship(back_populates="equipo")



# class TeamDataCreate(TeamBase, table=True):
#     id: int = Field(primary_key=True)
#     # nombre: str
#     # generacion: int
#     # pokemones: List[PokemonTeamCreate]


# # class TeamCreate(TeamBase):
# #     pass