from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_obtener_todos_los_equipos_pagina_existente():
    # Inicializa la lista de equipos con algunos datos de ejemplo
    global lista_equipos
    lista_equipos = [f"Equipo {i}" for i in range(1, 26)]  # 25 equipos

    response = client.get("/equipos/?pagina=1")

    assert response.status_code == 200
    assert response.json() == lista_equipos[0:10]  # Primeros 10 equipos

    response = client.get("/teams/?pagina=2")

    assert response.status_code == 200
    assert response.json() == lista_equipos[10:20]  # Siguientes 10 equipos

    response = client.get("/teams/?pagina=3")

    assert response.status_code == 200
    assert response.json() == lista_equipos[20:25]  # Últimos 5 equipos


def test_obtener_todos_los_equipos_pagina_no_existente():
    # Con la lista de 25 equipos, la página 4 no debería existir
    response = client.get("/teams/?pagina=4")

    assert response.status_code == 404
    assert response.json() == {"detail": "No se encontro la pagina solicitada"}


def test_obtener_todos_los_equipos_pagina_invalida():
    response = client.get("/teams/?pagina=-1")

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Error en el ingreso. La pagina debe ser un entero mayor a cero"
    }

    response = client.get("/equipos/?pagina=0")

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Error en el ingreso. La pagina debe ser un entero mayor a cero"
    }


def test_obtener_todos_los_equipos_vacia():
    global lista_equipos
    lista_equipos = []  # Lista vacía

    response = client.get("/equipos/?pagina=1")

    assert response.status_code == 404
    assert response.json() == {"detail": "No se encontraron equipos creados"}
