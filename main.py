from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Pokemon(BaseModel):
    id: int
    identificador: str
    id_especie: int
    altura: int
    peso: int
    experiencia_base: int
    orden: int
    es_default: bool


lista_pokemones = []
contador = 0
with open("pokemon.csv") as pokemones:
    for linea in pokemones:
        contador += 1
        if contador == 1:
            continue
        linea = linea.rstrip("\n")
        linea = linea.split(",")

        pokemon = Pokemon(
            id=linea[0],
            identificador=linea[1],
            id_especie=linea[2],
            altura=linea[3],
            peso=linea[4],
            experiencia_base=linea[5],
            orden=linea[6],
            es_default=linea[7],
        )
        lista_pokemones.append(pokemon)


@app.get("/pokemons")
def leer_pokemones():
    return lista_pokemones
