from fastapi import HTTPException, APIRouter
from db import lista_pokemones, fortalezas_tipos, debilidades_tipos, Pokemon, PokemonCreate, datos_pokemon, datos_movimientos_pokemon, datos_movimientos, datos_tipos_pokemon, Evolucion, Movimientomoves


router = APIRouter()


def calcular_debilidades(pokemon):
    debilidades_totales = {}
    for tipo in pokemon.tipo:
        for debilidad, efect in debilidades_tipos.get(tipo, {}).items():
            if debilidad not in debilidades_totales:
                debilidades_totales[debilidad] = 1
            debilidades_totales[debilidad] *= int(efect) / 100
    return debilidades_totales


def calcular_fortalezas(pokemon):
    fortalezas_totales = {}
    for tipo in pokemon.tipo:
        for fortaleza, efect in fortalezas_tipos.get(tipo, {}).items():
            if fortaleza not in fortalezas_totales:
                fortalezas_totales[fortaleza] = 1
            fortalezas_totales[fortaleza] *= int(efect) / 100
    return fortalezas_totales


@router.get("/")
def leer_pokemones():
    return lista_pokemones


@router.get("/{pokemon_id}")
def leer_pokemon(pokemon_id: int):
    pokemon = None
    for p in lista_pokemones:
        if p.id == pokemon_id:
            pokemon = p
            debilidades = calcular_debilidades(pokemon)
            fortalezas = calcular_fortalezas(pokemon)
            break

    if pokemon is None:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado")

    return {
        "pokemon": pokemon,
        "debilidades": debilidades,
        "fortalezas": fortalezas,
    }


@router.delete("/{id}")
def eliminar_pokemon(id):
    if not id.isdecimal():
        raise HTTPException(status_code=400, detail="El id debe ser un numero entero")
    for pokemon in lista_pokemones:
        if pokemon.id == int(id):
            lista_pokemones.remove(pokemon)
            return {
                "pokemon": pokemon,
                "debilidades": calcular_debilidades(pokemon),
                "fortalezas": calcular_fortalezas(pokemon),
            }
    raise HTTPException(status_code=404, detail="Pokemon no encontrado")


@router.post("/", response_model=Pokemon, status_code=201)
def create_pokemon(pokemon: PokemonCreate):
    pokemon_id = len(lista_pokemones) + 1
    nuevo_pokemon = Pokemon(
        id=pokemon_id,
        identificador=pokemon.identificador,
        id_especie=pokemon_id,
        altura=pokemon.altura,
        peso=pokemon.peso,
        experiencia_base=pokemon.experiencia_base,
        imagen=pokemon.imagen,
        tipo=pokemon.tipo,
        grupo_de_huevo=pokemon.grupo_de_huevo,
        estadisticas=pokemon.estadisticas,
        habilidades=pokemon.habilidades,
        generaciones=pokemon.generaciones,
        evoluciones_inmediatas=pokemon.evoluciones_inmediatas
    )
    lista_pokemones.append(nuevo_pokemon)
    return nuevo_pokemon


@router.get("/{pokemon_id}/movimientos")
def obtener_movimientos_pokemon(pokemon_id: int):
    if pokemon_id not in datos_pokemon:
        raise HTTPException(status_code=404, detail="Pokémon no encontrado")

    pokemon = datos_pokemon[pokemon_id]

    if pokemon_id not in datos_movimientos_pokemon:
        raise HTTPException(
            status_code=404, detail="Movimientos no encontrados para este Pokémon"
        )

    movimientos = datos_movimientos_pokemon[pokemon_id]

    lista_movimientos = []

    movimientos_vistos = set()
    for movimiento in movimientos:
        id_movimiento = movimiento["id_movimiento"]
        nivel_movimiento = movimiento["nivel"]

        if id_movimiento not in movimientos_vistos:
            movimientos_vistos.add(id_movimiento)
            if id_movimiento in datos_movimientos.movimientos:
                nombre_movimiento = datos_movimientos.movimientos[id_movimiento].nombre
                lista_movimientos.append(Movimientomoves(id=id_movimiento, nombre=nombre_movimiento, nivel=nivel_movimiento, es_evolucionado=False))

    tipos = datos_tipos_pokemon.get(pokemon_id, [])

    return {
        "id_pokemon": pokemon.id,
        "nombre_pokemon": pokemon.nombre,
        "tipos": tipos,
        "movimientos": [movimiento.dict() for movimiento in lista_movimientos],
    }
