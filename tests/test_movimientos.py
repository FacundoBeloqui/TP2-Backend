from fastapi.testclient import TestClient
from main import app
from db import lista_movimientos

client = TestClient(app)


def test_validar_movimiento():
    response = client.get("/movimientos/1")

    assert response.status_code == 200
    content = response.json()

    assert isinstance(content, dict)

    for movimiento in lista_movimientos:
        if movimiento.id == 1:
            movimiento_esperado = movimiento
            break

    assert movimiento_esperado is not None

    assert content["id"] == movimiento_esperado.id
    assert content["nombre"] == movimiento_esperado.nombre
    assert content["generacion"] == movimiento_esperado.generacion
    assert content["tipo"] == movimiento_esperado.tipo
    assert content["poder"] == movimiento_esperado.poder
    assert content["accuracy"] == movimiento_esperado.accuracy
    assert content["pp"] == movimiento_esperado.pp
    assert content["categoria"] == movimiento_esperado.categoria
    assert content["efecto"] == movimiento_esperado.efecto
    assert (
        content["pokemones_subida_nivel"] == movimiento_esperado.pokemones_subida_nivel
    )
    assert content["pokemones_tm"] == movimiento_esperado.pokemones_tm
    assert content["pokemones_grupo_huevo"] == movimiento_esperado.pokemones_grupo_huevo


def test_validar_id():
    movimiento_id = lista_movimientos[0].id
    response = client.get(f"/movimientos/{movimiento_id}")
    assert response.status_code == 200
    assert response.json()["id"] == movimiento_id


def test_leer_movimiento_id_invalido():
    response = client.get("/movimientos/abc")
    assert response.status_code == 400
    assert response.json() == {"detail": "El id debe ser un numero entero"}


def test_leer_movimiento_no_existente():
    response = client.get(f"/movimientos/9999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Movimiento no encontrado"}
