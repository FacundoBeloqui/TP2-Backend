from fastapi import HTTPException, APIRouter
from db import lista_pokemones, Pokemon

router = APIRouter()

lista_equipos = []

generacion = ""


@router.get("/{generacion}")
def limitar_generacion(generacion):
    return generacion


@router.get("/")
def obtener_todos_los_equipos(pagina: 1):
    if len(lista_equipos) == 0:
        raise HTTPException(status_code=404, detail="No se encontraron equipos creados")
    if pagina > (len(lista_equipos) // 10) + 1:
        raise HTTPException(
            status_code=404,
            detail="No se encontro la pagina solicitada. No hay suficientes equipos creados",
        )
    lista_a_mostrar = []
    try:
        for equipo in range(10 * (pagina - 1), 10 * (pagina - 1) + 10):
            lista_a_mostrar.append(equipo)
    except IndentationError:
        pass
    return lista_a_mostrar
