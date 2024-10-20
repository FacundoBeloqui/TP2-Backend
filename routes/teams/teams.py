from fastapi import HTTPException, APIRouter
from db import (
    lista_naturalezas,
    lista_pokemones,
    PokemonTeam,
    lista_movimientos,
    lista_habilidades,
    Team,
)

lista_equipos = []

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
    return lista_equipos[10 * (pagina - 1) : 10 * pagina]


def normalizar_palabra(palabra):
    vocales_con_tilde = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ü": "u"}
    palabra = palabra.lower()
    palabra_normalizada = ""
    for letra in palabra:
        if letra in vocales_con_tilde:
            palabra_normalizada += vocales_con_tilde[letra]
        else:
            palabra_normalizada += letra
    return palabra_normalizada


@router.patch("/")
def actualizar_equipo(team: Team):
    return team
