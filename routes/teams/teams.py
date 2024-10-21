from fastapi import HTTPException, APIRouter
from typing import List
from db import (
    lista_naturalezas,
    lista_pokemones,
    lista_movimientos,
    lista_habilidades,
    TeamCreate,
    TeamDataCreate,
    generaciones_pokemon,
)

generacion = ""
lista_equipos = []
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


@router.patch("/{id_team_a_updatear}/{id_pokemon_a_updatear}")
def actualizar_equipo(
    id_team_a_updatear: int, id_pokemon_a_updatear: int, team: TeamCreate
):
    if not lista_equipos:
        raise HTTPException(status_code=404, detail="No hay equipos disponibles")

    if id_team_a_updatear is None:
        raise HTTPException(
            status_code=400, detail="Ingrese el id del equipo a modificar"
        )

    if id_pokemon_a_updatear is None:
        raise HTTPException(status_code=400, detail="Ingrese un pokemon para editar")

    for equipo in lista_equipos:
        if id_team_a_updatear == equipo.id:
            for indice in len(equipo.pokemones):
                if equipo.pokemones[indice].id == id_pokemon_a_updatear:
                    v_f = False
                    for id_pokemon, generaciones in generaciones_pokemon.items():
                        if (
                            equipo.pokemones[indice].id == int(id_pokemon)
                            and equipo.generacion in generaciones
                        ):
                            v_f = True
                            break
                    if not v_f:
                        raise HTTPException(
                            status_code=422,
                            detail=f"El pokemon {equipo.pokemones[indice].id} no pertenece a la generacion definida en el equipo: {equipo.id}",
                        )

                    for movimiento in equipo.pokemones[indice].movimientos:
                        if len(equipo.pokemones[indice].movimientos) > 4:
                            raise HTTPException(
                                status_code=400,
                                detail="Se pueden asignar solo 4 movimientos",
                            )
                        if movimiento != 0:
                            v_f = False
                            for mov in lista_movimientos:
                                if (
                                    movimiento == mov.id
                                    and equipo.generacion >= mov.generacion
                                ):
                                    v_f = True
                                    break
                            if not v_f:
                                raise HTTPException(
                                    status_code=422,
                                    detail=f"El movimiento {movimiento} del pokemon_id {equipo.pokemones[indice].id} no pertenece a la generacion definida en el equipo {equipo.id}",
                                )
                    equipo.pokemones[indice] = team.pokemones
                    return equipo

            raise HTTPException(
                status_code=404, detail="Pokemon no encontrado en el equipo"
            )

    raise HTTPException(status_code=404, detail="Equipo no encontrado")


@router.delete("/{id}")
def eliminar_equipo(id: int):
    for equipo in lista_equipos:
        if equipo.id == id:
            lista_equipos.remove(equipo)
            return {"detail": f"Equipo con ID {id} eliminado exitosamente."}

    raise HTTPException(status_code=404, detail=f"Equipo con ID {id} no encontrado.")
