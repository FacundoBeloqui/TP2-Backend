from fastapi import HTTPException, APIRouter
from db import lista_pokemones, Pokemon, Team

router = APIRouter()

lista_equipos = []

generacion = ""


@router.get("/{generacion}")
def limitar_generacion(generacion):
    return generacion


# @router.post("/")
# def ....
#   if generacion == "":
#       return "ingrese una generacion antes de crear un equipo"
#   if generacion.isdecimal:
#       ...............
#       codigo de creacion de equipos
#       lista_equipos.append(equipo)
#   raise .....
#


@router.get("/")
def obtener_todos_los_equipos(pagina: 1):
    if len(lista_equipos) <= 10:
        pagina = 1
        return lista_equipos
