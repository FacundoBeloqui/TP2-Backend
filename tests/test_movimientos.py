from fastapi.testclient import TestClient
from main import app
from db import lista_movimientos

client = TestClient(app)


def test_leer_movimientos():
    # Realiza una petición GET al endpoint /movimientos
    response = client.get("/movimientos")

    # Verifica que la respuesta tenga un código de estado 200
    assert response.status_code == 200
    content = response.json()
    # Verifica que el contenido devuelto sea una lista
    assert isinstance(content, list)
    # Verifica que los datos coincidan con lo que esperas
    assert len(content) == len(lista_movimientos)
    primer_movimiento = content[0]
    assert primer_movimiento["id"] == lista_movimientos[0].id
    assert primer_movimiento["nombre"] == lista_movimientos[0].nombre
    assert primer_movimiento["tipo"] == lista_movimientos[0].tipo
    assert primer_movimiento["poder"] == lista_movimientos[0].poder
