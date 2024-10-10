from pydantic import BaseModel
from typing import List


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
    grupo_de_huevo: str


class Movimiento(BaseModel):
    id: int
    nombre: str
    tipo: str
    poder: str
    accuracy: str
    pp: str
    generacion: int
    categoria: str
    efecto: str
    pokemones_subida_nivel: List[str]
    pokemones_tm: List[str]
    pokemones_grupo_huevo: List[str]


pokemon_por_id = {}
with open("pokemon.csv") as archivo_pokemon:
    for linea in archivo_pokemon:
        linea = linea.rstrip("\n").split(",")
        if linea[0] == "id":
            continue
        pokemon_por_id[linea[0]] = linea[1]


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
        if nombre_del_tipo:
            if pokemon_id not in pokemon_tipos:
                pokemon_tipos[pokemon_id] = []
            pokemon_tipos[pokemon_id].append(nombre_del_tipo)

tipo_huevo = {}
huevos_nombres = {}
with open("pokemon_egg_groups.csv") as grupo_huevo:
    for linea in grupo_huevo:
        linea = linea.rstrip("\n").split(",")
        tipo_huevo[linea[0]] = linea[1]

with open("egg_group_prose.csv") as nombres_huevo:
    for linea in nombres_huevo:
        linea = linea.rstrip("\n").split(",")
        if linea[1] == "7":
            huevos_nombres[linea[0]] = linea[2]


lista_pokemones = []
with open("pokemon.csv") as pokemones:
    for linea in pokemones:
        linea = linea.rstrip("\n").split(",")
        if linea[0] == "id":
            continue
        pokemon = Pokemon(
            id=int(linea[0]),
            identificador=linea[1],
            id_especie=int(linea[2]),
            altura=int(linea[3]),
            peso=int(linea[4]),
            experiencia_base=int(linea[5]),
            orden=int(linea[6]),
            es_default=linea[7] == "1",
            imagen=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{linea[0]}.png",
            tipo=pokemon_tipos.get(linea[0], []),
            grupo_de_huevo=huevos_nombres.get(tipo_huevo.get(linea[0], ""), ""),
        )
        lista_pokemones.append(pokemon)


dicc_categorias = {}
dicc_efectos = {}
with open("move_damage_class_prose.csv") as categorias:
    for linea in categorias:
        linea = linea.rstrip("\n").split(",")
        if linea[1] == "7":
            dicc_categorias[linea[0]] = linea[2]

with open("move_effect_prose.csv") as efectos:
    for linea in efectos:
        linea = linea.rstrip("\n").split(",")
        if len(linea) > 2:
            dicc_efectos[linea[0]] = linea[2]


dicc_metodos = {}
movimientos_subida_nivel = {}
movimientos_tm = {}
movimientos_grupo_huevo = {}
with open("pokemon_move_method_prose.csv") as metodos:
    for linea in metodos:
        linea = linea.rstrip("\n").split(",")
        if linea[1] == "7":
            dicc_metodos[linea[0]] = linea[2]
with open("pokemon_moves.csv") as movimientos_pokemon:
    for linea in movimientos_pokemon:
        linea = linea.rstrip("\n").split(",")
        pokemon_id = linea[0]
        metodo_id = linea[3]
        if metodo_id in dicc_metodos:
            metodo_nombre = dicc_metodos[metodo_id]
            if pokemon_id in pokemon_por_id:
                if metodo_nombre.lower() == "nivel":
                    if linea[2] not in movimientos_subida_nivel:
                        movimientos_subida_nivel[linea[2]] = []
                    movimientos_subida_nivel[linea[2]].append(
                        pokemon_por_id[pokemon_id]
                    )
                elif metodo_nombre.lower() == "máquina":
                    if linea[2] not in movimientos_tm:
                        movimientos_tm[linea[2]] = []
                    movimientos_tm[linea[2]].append(pokemon_por_id[pokemon_id])
                elif metodo_nombre.lower() == "huevo":
                    if linea[2] not in movimientos_grupo_huevo:
                        movimientos_grupo_huevo[linea[2]] = []
                    movimientos_grupo_huevo[linea[2]].append(pokemon_por_id[pokemon_id])

lista_movimientos = []
with open("moves.csv") as movimientos:
    for linea in movimientos:
        linea = linea.rstrip("\n").split(",")
        if linea[0] == "id":
            continue
        grupo_huevo_movimiento = huevos_nombres.get(tipo_huevo.get(linea[0], ""), "")
        if (
            linea[9] in dicc_categorias
            and linea[10] in dicc_efectos
            and linea[3] in tipo_nombres
            and grupo_huevo_movimiento
        ):
            movimiento = Movimiento(
                id=int(linea[0]),
                nombre=linea[1],
                tipo=tipo_nombres[linea[3]],
                poder=linea[4],
                accuracy=linea[6],
                pp=linea[5],
                generacion=int(linea[2]),
                categoria=dicc_categorias[linea[9]],
                efecto=dicc_efectos[linea[10]],
                pokemones_subida_nivel=movimientos_subida_nivel.get(linea[0], []),
                pokemones_tm=movimientos_tm.get(linea[0], []),
                pokemones_grupo_huevo=movimientos_grupo_huevo.get(linea[0], []),
            )
            lista_movimientos.append(movimiento)
