from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Pokemon(BaseModel):
    id: int
    identificador: str
    _id_especie: int
    _altura: int
    _peso: int
    _experiencia_base: int
    _orden: int
    _es_default: bool
    imagen: str
    tipo: str


lista_nombres_tipos = []
with open("type_names.csv") as nombres_tipos:
    for linea in nombres_tipos:
        linea = linea.rstrip("\n").split(",")
        if linea[1] == "7":
            lista_nombres_tipos.append(linea)
lista_tipos = []
with open("pokemon_types.csv") as tipos:
    for linea in tipos:
        linea = linea.rstrip("\n").split(",")
        lista_tipos.append(linea)
lista_pokemones = []
with open("pokemon.csv") as pokemones:
    for contador, linea in enumerate(pokemones):
        linea = linea.rstrip("\n").split(",")
        tipo_pokemon = None
        for tipo in lista_tipos:
            if tipo[0] == linea[0]:
                tipo_id = tipo[1]
                for nombre_tipo in lista_nombres_tipos:
                    if tipo_id == nombre_tipo[0]:
                        tipo_pokemon = nombre_tipo[2]
                        break
                break

        if tipo_pokemon:
            pokemon = Pokemon(
                id=int(linea[0]),
                identificador=linea[1],
                imagen=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{linea[0]}.png",
                tipo=tipo_pokemon,
            )
            lista_pokemones.append(pokemon)


@app.get("/pokemons")
def leer_pokemones():
    return lista_pokemones
