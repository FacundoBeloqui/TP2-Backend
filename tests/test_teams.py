from fastapi.testclient import TestClient
from main import app
from db import lista_naturalezas
from unittest.mock import patch

client = TestClient(app)


def test_leer_naturalezas():
    response = client.get("/teams")

    assert response.status_code == 200
    content = response.json()
    assert isinstance(content, list)

    if lista_naturalezas:
        assert len(content) == len(lista_naturalezas)
        primera_naturaleza = content[0]
        assert primera_naturaleza["id"] == lista_naturalezas[0].id
        assert primera_naturaleza["nombre"] == lista_naturalezas[0].nombre
        assert (
            primera_naturaleza["stat_decreciente"]
            == lista_naturalezas[0].stat_decreciente
        )
        assert (
            primera_naturaleza["stat_creciente"] == lista_naturalezas[0].stat_creciente
        )
        assert (
            primera_naturaleza["id_gusto_preferido"]
            == lista_naturalezas[0].id_gusto_preferido
        )
        assert (
            primera_naturaleza["id_gusto_menos_preferido"]
            == lista_naturalezas[0].id_gusto_menos_preferido
        )
        assert primera_naturaleza["indice_juego"] == lista_naturalezas[0].indice_juego


def test_obtener_todos_los_equipos_vacia():
    with patch("routes.teams.teams.lista_equipos", new=[]):
        response = client.get("/teams/?pagina=1")
        assert response.status_code == 404
        assert response.json() == {"detail": "No se encontraron equipos creados"}


def test_obtener_todos_los_equipos_pagina_existente():
    with patch(
        "routes.teams.teams.lista_equipos",
        new=[f"Equipo {i}" for i in range(1, 26)],
    ):
        response = client.get("/teams/?pagina=1")
        assert response.status_code == 200
        assert response.json() == [f"Equipo {i}" for i in range(1, 11)]


def test_obtener_todos_los_equipos_pagina_no_existente():
    with patch(
        "routes.teams.teams.lista_equipos",
        new=[f"Equipo {i}" for i in range(1, 26)],
    ):
        response = client.get("/teams/?pagina=4")
        assert response.status_code == 404
        assert response.json() == {"detail": "No se encontro la pagina solicitada"}


def test_obtener_todos_los_equipos_pagina_invalida():
    with patch(
        "routes.teams.teams.lista_equipos",
        new=[f"Equipo {i}" for i in range(1, 26)],
    ):
        response = client.get("/teams/?pagina=-1")
        assert response.status_code == 400
        assert response.json() == {
            "detail": "Error en el ingreso. La pagina debe ser un entero mayor a cero"
        }


def test_obtener_todos_los_equipos_pagina_con_diez():
    with patch(
        "routes.teams.teams.lista_equipos",
        new=[f"Equipo {i}" for i in range(1, 11)],
    ):
        response = client.get("/teams/?pagina=1")
        assert response.status_code == 200
        assert response.json() == [f"Equipo {i}" for i in range(1, 11)]
