from fastapi import HTTPException, APIRouter
from db import lista_naturalezas, lista_pokemones, Pokemon, lista_equipos, Team, TeamCreate, lista_movimientos, generaciones_pokemon, pokemon_tipos, lista_naturalezas

generacion = ""

router = APIRouter()


@router.get("/nature")
def leer_naturalezas():
    return lista_naturalezas


@router.get("/")
def obtener_todos_los_equipos(pagina: int = 1):
    if len(lista_equipos) == 0:
        raise HTTPException(status_code=404, detail="No se encontraron equipos creados")
    if pagina <= 0:
        raise HTTPException(
            status_code=400,
            detail="Error en el ingreso. La pagina debe ser un entero mayor a cero",
        )

    if pagina > (len(lista_equipos) + 9) // 10:
        raise HTTPException(
            status_code=404,
            detail="No se encontro la pagina solicitada",
        )
    if len(lista_equipos) <= 10 and pagina == 1:
        return lista_equipos
    return lista_equipos[10 * (pagina - 1) : 10 * pagina]


@router.get("/{team_id}", response_model=Team)
def get_team_by_id(team_id):
    if not team_id.isdecimal():
        raise HTTPException(status_code=400, detail="El id debe ser un numero entero")
    team = None
    for t in lista_equipos:
        if t["id"] == int(team_id):
            team = t
            break
    if team is None: 
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return team


@router.post("/")
def create_team(team: TeamCreate):
    lista_generacion_pokemones = []
    lista_generacion_movimientos = []
    if team.generacion > 9 or team.generacion < 1:
        raise HTTPException(status_code=404, detail="No se encontró la generacion")

    if len(team.pokemones) < 1 or len(team.pokemones) > 6:
        raise HTTPException(status_code=400, detail="Debe elegir al menos 1 pokemon y no mas de 6 pokemones")

    for id_pokemon, generaciones in generaciones_pokemon.items():
        if team.generacion in generaciones:
            for pokemon in lista_pokemones:
                if pokemon.id == int(id_pokemon):
                    lista_generacion_pokemones.append(pokemon)
        
    for movimiento in lista_movimientos:
        if team.generacion == movimiento.generacion:
            lista_generacion_movimientos.append(movimiento)

    pokemon_elegido = []
    movimiento_elegido = []
    for pokemon_team in team.pokemones:
        for p in lista_generacion_pokemones:
            if p.id == pokemon_team.id:
                pokemon_elegido.append(p)
    for movimiento_team in team.pokemones:
        for m in lista_generacion_movimientos:
            if m.id in movimiento_team.movimientos:
                movimiento_elegido.append(m)

    if  len(pokemon_elegido) == 0:
        raise HTTPException(status_code=404, detail="Pokemon seleccionado no encontrado en la generacion")
    
    if len(movimiento_elegido) == 0:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado en la generacion")
    
    nuevo_equipo = {
        "pokemon": pokemon_elegido, 
        "movimiento": movimiento_elegido
    }
    
    lista_equipos.append(nuevo_equipo)

    return nuevo_equipo


@router.patch("/{id_team_a_updatear}")
def actualizar_equipo(id_team_a_updatear: int, team: Team):
    if not id_team_a_updatear:
        raise HTTPException(
            status_code=400, detail="Ingrese el id del equipo a modificar"
        )
    if not lista_equipos:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    for equipo in lista_equipos:
        if id_team_a_updatear == equipo.id:
            equipo.pokemon_1 = team.pokemon_1
            equipo.pokemon_2 = team.pokemon_2
            equipo.pokemon_3 = team.pokemon_3
            equipo.pokemon_4 = team.pokemon_4
            equipo.pokemon_5 = team.pokemon_5
            equipo.pokemon_6 = team.pokemon_6

            return {"message": "Equipo actualizado correctamente", "equipo": equipo}
    raise HTTPException(status_code=404, detail="Equipo no encontrado")