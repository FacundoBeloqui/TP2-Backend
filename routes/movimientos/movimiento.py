"""from fastapi import HTTPException, APIRouter
from db import lista_movimientos


router = APIRouter()


@router.get("/{id}")
def leer_movimiento_id(id):
    if not id.isdecimal():
        raise HTTPException(status_code=400, detail="El id debe ser un numero entero")
    for movimiento in lista_movimientos:
        if movimiento.id == int(id):
            return movimiento
    raise HTTPException(status_code=404, detail="Movimiento no encontrado")
"""
