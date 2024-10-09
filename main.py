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
    imagen: str
    tipo: list[str]

class PokemonCreate(BaseModel):
    identificador: str
    altura: int
    peso: int
    experiencia_base: int
    imagen: str
    tipo: list[str]


tipo_nombres = {}
with open("type_names.csv") as nombres_tipos:
    for linea in nombres_tipos:
        linea = linea.rstrip("\n").split(",")
        if linea[1] == "7":
            tipo_nombres[linea[0]] = linea[2]

pokemon_tipos = {}
with open("pokemon_types.csv") as tipos:
    for linea in tipos:
        linea = linea.rstrip("\n").split(",")
        pokemon_id = linea[0]
        nombre_del_tipo = tipo_nombres.get(linea[1], "")
        if nombre_del_tipo != "":
            if linea[0] not in pokemon_tipos:
                pokemon_tipos[linea[0]] = []
            pokemon_tipos[linea[0]].append(nombre_del_tipo)

lista_pokemones = []
with open("pokemon.csv") as pokemones:
    for linea in pokemones:
        linea = linea.rstrip("\n")
        linea = linea.split(",")
        if linea[0] == "id":
            continue
        pokemon = Pokemon(
            id=linea[0],
            identificador=linea[1],
            id_especie=linea[2],
            altura=linea[3],
            peso=linea[4],
            experiencia_base=linea[5],
            imagen=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{linea[0]}.png",
            tipo=pokemon_tipos.get(linea[0], []),
        )
        lista_pokemones.append(pokemon)


@app.post("/pokemons", response_model=Pokemon, status_code=201)
def create_pokemon(pokemon: PokemonCreate):
    pokemon_id = len(lista_pokemones)
    nuevo_pokemon = Pokemon(
        id=pokemon_id,
        identificador=pokemon.identificador,
        id_especie=pokemon_id,
        altura=pokemon.altura,
        peso=pokemon.peso,
        experiencia_base=pokemon.experiencia_base,
        imagen=pokemon.imagen,
        tipo=pokemon.tipo
    )
    lista_pokemones.append(nuevo_pokemon)
    return nuevo_pokemon