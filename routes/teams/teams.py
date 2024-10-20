from fastapi import HTTPException, APIRouter
from db import lista_naturalezas, lista_pokemones, Pokemon, lista_equipos, Team, TeamCreate, lista_movimientos

lista_equipos = []

generacion = ""

router = APIRouter()


@router.get("/nature")
def leer_naturalezas():
    return lista_naturalezas


@router.get("/")
def obtener_todos_los_equipos(pagina: int):
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
    return lista_equipos[10 * (pagina - 1) : 10 * (pagina - 1) + 10]


@router.get("/{team_id}", response_model=Team)
def get_team_by_id(team_id):
    if not team_id.isdecimal():
        raise HTTPException(status_code=400, detail="El id debe ser un numero entero")
    team = None
    for t in lista_equipos:
        if t.id == team_id:
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
    
    for pokemon in lista_pokemones:
        if team.generacion in pokemon["generaciones"]:
            lista_generacion_pokemones.append(pokemon)
        
    for movimiento in lista_movimientos:
        if team.generacion == movimiento["generacion"]:
            lista_generacion_movimientos.append(movimiento)

    pokemon_elegido = None
    movimiento_elegido = None
    for p in lista_generacion_pokemones:
        if p["id"] == team.pokemon_id:
            pokemon_elegido = p
    for m in lista_generacion_movimientos:
        if m["id"] == team.movimiento_id:
            movimiento_elegido = m

    if not pokemon_elegido:
        raise HTTPException(status_code=404, detail="Pokemon seleccionado no encontrado en la generacion")
    
    if not movimiento_elegido:
        raise HTTPException(status_code=404, detail="Movimiento no encontrado en la generacion")
    
    nuevo_equipo = {pokemon_elegido, movimiento_elegido}
    
    lista_equipos.append(nuevo_equipo)

    return nuevo_equipo

