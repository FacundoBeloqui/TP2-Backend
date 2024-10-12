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
    estadisticas: dict[str, int]
    habilidades: list[str]
    generaciones: list


class Team(BaseModel):
    id: int
    nombre: str
    pokemones_incluidos: list[Pokemon]


dicc_stats = {}
with open("stats.csv") as f:
    for i, linea in enumerate(f):
        if i == 0:
            continue
        linea = linea.rstrip("\n").split(",")
        id_stat = int(linea[0])
        nombre_stat = linea[2]
        if id_stat in dicc_stats:
            dicc_stats[id_stat].append(dicc_stats)
        else:
            dicc_stats[id_stat] = nombre_stat

dicc_pokemon_stats = {}
with open("pokemon_stats.csv") as pokemon_stats:
    for i, linea in enumerate(pokemon_stats):
        lista_habilidades = []
        if i == 0:
            continue
        linea = linea.rstrip("\n").split(",")
        pokemon_id = linea[0]
        stat_id = int(linea[1])
        base_stat = int(linea[2])
        stat_nombre = dicc_stats[stat_id]
        if pokemon_id not in dicc_pokemon_stats:
            dicc_pokemon_stats[pokemon_id] = {}
        dicc_pokemon_stats[pokemon_id][stat_nombre] = base_stat

nombres_habilidades = {}
with open("ability_names.csv") as ability_names:
    for i, linea in enumerate(ability_names):
        if i == 0:
            continue
        linea = linea.rstrip("\n").split(",")
        if linea[1] == "7":
            nombres_habilidades[linea[0]] = linea[2]


habilidades_de_cada_pokemon = {}
with open("pokemon_abilities.csv") as pokemon_abilities:
    for i, linea in enumerate(pokemon_abilities):
        if i == 0:
            continue
        linea = linea.rstrip("\n").split(",")
        id_pokemon = linea[0]
        nombre_del_movimiento = nombres_habilidades.get(linea[1])
        if id_pokemon not in habilidades_de_cada_pokemon:
            habilidades_de_cada_pokemon[id_pokemon] = []
        habilidades_de_cada_pokemon[id_pokemon].append(nombre_del_movimiento)


tipo_nombres = {}
with open("type_names.csv") as nombres_tipos:
    for linea in nombres_tipos:
        linea = linea.rstrip("\n").split(",")
        if linea[1] == "7":
            tipo_nombres[linea[0]] = linea[2]

debilidades_tipos = {}
fortalezas_tipos = {}
with open("type_efficacy.csv") as efectividad_tipos:
    for linea in efectividad_tipos:
        linea = linea.rstrip("\n").split(",")
        if linea[0] == "damage_type_id":
            continue
        efectividad = linea[2]
        nombre_tipo_daño = tipo_nombres[linea[1]]
        nombre_tipo_target = tipo_nombres[linea[0]]
        if nombre_tipo_daño not in debilidades_tipos:
            debilidades_tipos[nombre_tipo_daño] = {}
        debilidades_tipos[nombre_tipo_daño][nombre_tipo_target] = efectividad
        if nombre_tipo_target not in fortalezas_tipos:
            fortalezas_tipos[nombre_tipo_target] = {}
        fortalezas_tipos[nombre_tipo_target][nombre_tipo_daño] = efectividad


pokemon_tipos = {}
with open("pokemon_types.csv") as tipos:
    for linea in tipos:
        linea = linea.rstrip("\n").split(",")
        pokemon_id = linea[0]
        nombre_del_tipo = tipo_nombres.get(linea[1], "")
        if nombre_del_tipo != "":
            if pokemon_id not in pokemon_tipos:
                pokemon_tipos[pokemon_id] = []
            pokemon_tipos[pokemon_id].append(nombre_del_tipo)

generaciones_pokemon = {}
with open("pokemon_form_generations.csv") as generaciones_csv:
    for linea in generaciones_csv:
        linea = linea.rstrip("\n").split(",")
        pokemon_id = linea[0]
        generacion = linea[1]
        if pokemon_id == "pokemon_form_id":
            continue
        if pokemon_id not in generaciones_pokemon:
            generaciones_pokemon[pokemon_id] = []
        generaciones_pokemon[pokemon_id].append(int(generacion))


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
            orden=linea[6],
            es_default=linea[7],
            tipo=pokemon_tipos.get(linea[0], []),
            imagen=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{linea[0]}.png",
            estadisticas=dicc_pokemon_stats.get(linea[0], ""),
            habilidades=habilidades_de_cada_pokemon.get(linea[0], []),
            generaciones=generaciones_pokemon.get(linea[0], ""),
        )
        lista_pokemones.append(pokemon)
