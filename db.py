from pydantic import BaseModel


class Pokemon(BaseModel):
    id: int
    identificador: str
    id_especie: int
    altura: int
    peso: int
    experiencia_base: int
    orden: int
    es_default: bool
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
pokemon_tipos = {}
evoluciones_pokemones = {}
lista_pokemones = []

with open("type_names.csv") as nombres_tipos:
    for linea in nombres_tipos:
        linea = linea.rstrip("\n").split(",")
        if linea[1] == "7":
            tipo_nombres[linea[0]] = linea[2]

with open("pokemon_types.csv") as tipos:
    for linea in tipos:
        linea = linea.rstrip("\n").split(",")
        pokemon_id = linea[0]
        nombre_del_tipo = tipo_nombres.get(linea[1], "")
        if nombre_del_tipo != "":
            if pokemon_id not in pokemon_tipos:
                pokemon_tipos[pokemon_id] = []
            pokemon_tipos[pokemon_id].append(nombre_del_tipo)

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
            orden=linea[6],
            es_default=linea[7],
            imagen=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{linea[0]}.png",
            tipo=pokemon_tipos.get(linea[0], []),
        )
        lista_pokemones.append(pokemon)