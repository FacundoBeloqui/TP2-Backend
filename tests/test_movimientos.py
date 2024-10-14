from fastapi.testclient import TestClient
from main import app
from db import lista_movimientos

client = TestClient(app)


def test_get_movimientos():
    response = client.get("/movimientos")

    assert response.status_code == 200
    content = response.json()

    assert isinstance(content, list)

    assert len(content) == len(lista_movimientos)

    primer_movimiento = content[0]
    assert primer_movimiento["id"] == lista_movimientos[0].id
    assert primer_movimiento["nombre"] == lista_movimientos[0].nombre
    assert primer_movimiento["tipo"] == lista_movimientos[0].tipo
    assert primer_movimiento["poder"] == lista_movimientos[0].poder
    assert primer_movimiento["accuracy"] == lista_movimientos[0].accuracy
    assert primer_movimiento["pp"] == lista_movimientos[0].pp
    assert primer_movimiento["generacion"] == lista_movimientos[0].generacion


def test_leer_movimientos_vacio():
    lista_movimientos.clear()
    response = client.get("/movimientos")
    assert response.status_code == 200
    assert response.json() == []


def test_leer_movimiento_por_id():
    movimiento_id = lista_movimientos[0].id
    response = client.get(f"/movimientos/{movimiento_id}")
    assert response.status_code == 200
    assert response.json()["id"] == movimiento_id


def test_leer_movimiento_invalido():
    response = client.get("/movimientos/99999")
    assert response.status_code == 404


def test_leer_movimiento_id_invalido():
    response = client.get("/movimientos/abc")
    assert response.status_code == 422


def test_error_manejo():
    lista_movimientos = None
    response = client.get("/movimientos")
    assert response.status_code == 500
