from fastapi.testclient import TestClient
from main import app
from db import lista_movimientos

client = TestClient(app)


def test_leer_movimiento_id():
    movimiento_id = 1
    response = client.get("/movimientos/1")

    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert "nombre" in data
    assert "tipo" in data
    assert "poder" in data
    assert "accuracy" in data
    assert "pp" in data
    assert "generacion" in data
    assert "categoria" in data
    assert "efecto" in data
    assert "pokemones_subida_nivel" in data
    assert "pokemones_tm" in data
    assert "pokemones_grupo_huevo" in data

    assert data["id"] == movimiento_id


def test_leer_movimiento_id_invalido():
    response = client.get("/movimientos/abc")
    assert response.status_code == 400
    assert response.json() == {"detail": "El id debe ser un numero entero"}

def test_leer_movimiento_por_id():
    movimiento_id = lista_movimientos[0].id
    response = client.get(f"/movimientos/{movimiento_id}")
    assert response.status_code == 200
    assert response.json()["id"] == movimiento_id


def test_leer_movimiento_no_existente():
    movimiento_id = 9999
    response = client.get(f"/movimientos/{movimiento_id}")

def test_leer_movimiento_invalido():
    response = client.get("/movimientos/99999")
    assert response.status_code == 404


def test_leer_movimiento_id_invalido():
    response = client.get("/movimientos/abc")
    assert response.status_code == 422


def test_error_manejo():
    lista_movimientos = None
    response = client.get("/movimientos")
    assert response.status_code == 404
    assert response.json() == {"detail": "Movimiento no encontrado"}
