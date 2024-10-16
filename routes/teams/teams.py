from fastapi import HTTPException, APIRouter
from db import lista_naturalezas, lista_pokemones, Pokemon, lista_equipos, Team, TeamCreate

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
