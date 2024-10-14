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
    generaciones: list
    grupo_de_huevo: str
    estadisticas: dict
    habilidades: list[str]
    evoluciones_inmediatas: list


class Movimiento(BaseModel):
    id: int
    nombre: str
    generacion: int
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


class Naturaleza(BaseModel):
    id: int
    nombre: str
    stat_decreciente: str
    stat_creciente: str
    id_gusto_preferido: int
    id_gusto_menos_preferido: int
    indice_juego: int


pokemon_por_id = {}
with open("pokemon.csv") as archivo_pokemon:
    for linea in archivo_pokemon:
        linea = linea.rstrip("\n").split(",")
        if linea[0] == "id":
            continue
        pokemon_por_id[linea[0]] = linea[1]

lista_estadisticas = []
dicc_stats = {}
pokemon_habilidades = []
pokemon_estadisticas = []

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

evoluciones_pokemones = {}
with open("pokemon_evolutions.csv") as evoluciones_csv:
    for linea in evoluciones_csv:
        linea = linea.rstrip("\n").split(",")
        if linea[0] == "id":
            continue
        pokemon_id = int(linea[0])
        evolucion_id = int(linea[1])

        if pokemon_id not in evoluciones_pokemones:
            evoluciones_pokemones[pokemon_id] = []

        if evolucion_id not in evoluciones_pokemones:
            evoluciones_pokemones[evolucion_id] = []

        if pokemon_por_id[str(evolucion_id)] not in evoluciones_pokemones[pokemon_id]:
            evoluciones_pokemones[pokemon_id].append(pokemon_por_id[str(evolucion_id)])
        if pokemon_por_id[str(pokemon_id)] not in evoluciones_pokemones[evolucion_id]:
            evoluciones_pokemones[evolucion_id].append(pokemon_por_id[str(pokemon_id)])


lista_pokemones = []
with open("pokemon.csv") as pokemones:
    for linea in pokemones:
        linea = linea.rstrip("\n").split(",")
        if linea[0] == "id":
            continue
        pokemon = Pokemon(
            id=int(linea[0]),
            identificador=linea[1],
            id_especie=linea[2],
            altura=linea[3],
            peso=linea[4],
            experiencia_base=linea[5],
            orden=linea[6],
            es_default=linea[7],
            tipo=pokemon_tipos.get(linea[0], []),
            imagen=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{linea[0]}.png",
            grupo_de_huevo=huevos_nombres.get(tipo_huevo.get(linea[0], ""), ""),
            estadisticas=dicc_pokemon_stats.get(linea[0], {}),
            habilidades=habilidades_de_cada_pokemon.get(linea[0], []),
            generaciones=generaciones_pokemon.get(linea[0], ""),
            evoluciones_inmediatas=evoluciones_pokemones.get(int(linea[0]), []),
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
                pokemon_nombre = pokemon_por_id[pokemon_id]

                if metodo_nombre.lower() == "nivel":
                    if linea[2] not in movimientos_subida_nivel:
                        movimientos_subida_nivel[linea[2]] = []
                    if pokemon_nombre not in movimientos_subida_nivel[linea[2]]:
                        movimientos_subida_nivel[linea[2]].append(pokemon_nombre)

                elif metodo_nombre.lower() == "máquina":
                    if linea[2] not in movimientos_tm:
                        movimientos_tm[linea[2]] = []
                    if pokemon_nombre not in movimientos_tm[linea[2]]:
                        movimientos_tm[linea[2]].append(pokemon_nombre)

                elif metodo_nombre.lower() == "huevo":
                    if linea[2] not in movimientos_grupo_huevo:
                        movimientos_grupo_huevo[linea[2]] = []
                    if pokemon_nombre not in movimientos_grupo_huevo[linea[2]]:
                        movimientos_grupo_huevo[linea[2]].append(pokemon_nombre)


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
                generacion=int(linea[2]),
                tipo=tipo_nombres[linea[3]],
                poder=linea[4],
                accuracy=linea[6],
                pp=linea[5],
                categoria=dicc_categorias[linea[9]],
                efecto=dicc_efectos[linea[10]],
                pokemones_subida_nivel=movimientos_subida_nivel.get(linea[0], []),
                pokemones_tm=movimientos_tm.get(linea[0], []),
                pokemones_grupo_huevo=movimientos_grupo_huevo.get(int(linea[0]), []),
            )
            lista_movimientos.append(movimiento)
naturalezas_nombres = {}
with open("nature_names.csv") as nombres_naturalezas:
    for linea in nombres_naturalezas:
        linea = linea.rstrip("\n").split(",")
        if linea[1] == "7":
            naturalezas_nombres[linea[0]] = linea[2]
dicc_estadisticas = {}
with open("stats.csv") as estadisticas:
    for linea in estadisticas:
        linea = linea.rstrip("\n").split(",")
        dicc_estadisticas[linea[0]] = linea[2]

lista_naturalezas = []
with open("natures.csv") as naturalezas:
    for linea in naturalezas:
        linea = linea.rstrip("\n").split(",")
        if linea[0] == "id":
            continue
        if linea[2] in dicc_estadisticas:
            estadistica_decreciente = dicc_estadisticas.get(linea[2], "")
        if linea[3] in dicc_estadisticas:
            estadistica_creciente = dicc_estadisticas.get(linea[3], "")
            naturaleza = Naturaleza(
                id=int(linea[0]),
                nombre=naturalezas_nombres[linea[0]],
                stat_decreciente=estadistica_decreciente,
                stat_creciente=estadistica_creciente,
                id_gusto_preferido=int(linea[4]),
                id_gusto_menos_preferido=int(linea[5]),
                indice_juego=int(linea[6]),
            )
            lista_naturalezas.append(naturaleza)
