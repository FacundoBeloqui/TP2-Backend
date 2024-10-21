from fastapi import HTTPException, APIRouter
from db import Team, TeamCreate, lista_equipos

router = APIRouter()

@router.get("/")
def get_teams():
    return lista_equipos

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

@router.post("/", response_model=Team)
def create_team(team: TeamCreate):
    team_id = len(lista_equipos) + 1
    new_team = Team(
        id=team_id,
        nombre=team.nombre,
        pokemones_incluidos=team.pokemones_incluidos
    )
    lista_equipos.append(new_team)
    return new_team
