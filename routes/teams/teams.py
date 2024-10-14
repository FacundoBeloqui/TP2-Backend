from fastapi import HTTPException, APIRouter
from db import lista_naturalezas


router = APIRouter()


@router.get("/")
def leer_naturalezas():
    return lista_naturalezas
