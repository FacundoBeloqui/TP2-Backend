from fastapi.testclient import TestClient
from main import app
from db import (
    lista_naturalezas,
    Team,
    PokemonTeam,
    lista_pokemones,
    lista_movimientos,
    lista_equipos,
    Teams,
)
import pytest
from routes.teams.teams import lista_equipos

client = TestClient(app)


def test_leer_naturalezas():
    response = client.get("/teams")


@pytest.fixture(autouse=True)
def reset_lista_equipos():
    global lista_equipos
    lista_equipos.clear()
    yield
    lista_equipos.clear()


def test_no_hay_equipos():
    response = client.get("/teams")
    assert response.status_code == 404
    assert response.json() == {"detail": "No se encontraron equipos creados"}


def test_pagina_invalida_cero():
    lista_equipos.extend(
        [
            "Equipo 1",
            "Equipo 2",
            "Equipo 3",
            "Equipo 4",
            "Equipo 5",
            "Equipo 6",
            "Equipo 7",
            "Equipo 8",
            "Equipo 9",
            "Equipo 10",
            "Equipo 11",
        ]
    )
    response = client.get("/teams", params={"pagina": 0})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Error en el ingreso. La pagina debe ser un entero mayor a cero"
    }


def test_pagina_invalida_menor_que_uno():
    lista_equipos.extend(
        [
            "Equipo 1",
            "Equipo 2",
            "Equipo 3",
            "Equipo 4",
            "Equipo 5",
            "Equipo 6",
            "Equipo 7",
            "Equipo 8",
            "Equipo 9",
            "Equipo 10",
            "Equipo 11",
        ]
    )
    response = client.get("/teams", params={"pagina": -21})
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Error en el ingreso. La pagina debe ser un entero mayor a cero"
    }


def test_pagina_no_encontrada():
    global lista_equipos
    lista_equipos.extend(["Equipo 1", "Equipo 2"])
    response = client.get("/teams", params={"pagina": 2})
    assert response.status_code == 404
    assert response.json() == {"detail": "No se encontro la pagina solicitada"}


def test_obtener_equipos_pagina_1():
    global lista_equipos
    lista_equipos.extend(
        [
            "Equipo 1",
            "Equipo 2",
            "Equipo 3",
            "Equipo 4",
            "Equipo 5",
            "Equipo 6",
            "Equipo 7",
            "Equipo 8",
            "Equipo 9",
            "Equipo 10",
            "Equipo 11",
        ]
    )
    response = client.get("/teams", params={"pagina": 1})
    assert response.status_code == 200
    assert response.json() == lista_equipos[:10]


def test_obtener_equipos_pagina_2():
    global lista_equipos
    lista_equipos.extend(
        [
            "Equipo 1",
            "Equipo 2",
            "Equipo 3",
            "Equipo 4",
            "Equipo 5",
            "Equipo 6",
            "Equipo 7",
            "Equipo 8",
            "Equipo 9",
            "Equipo 10",
            "Equipo 11",
        ]
    )
    response = client.get("/teams", params={"pagina": 2})
    assert response.status_code == 200
    assert response.json() == lista_equipos[10:]


def test_pagina_excesiva():
    global lista_equipos
    lista_equipos.extend(
        [
            "Equipo 1",
            "Equipo 2",
            "Equipo 3",
            "Equipo 4",
            "Equipo 5",
            "Equipo 6",
            "Equipo 7",
            "Equipo 8",
            "Equipo 9",
            "Equipo 10",
            "Equipo 11",
        ]
    )
    response = client.get("/teams", params={"pagina": 3})
    assert response.status_code == 404
    assert response.json() == {"detail": "No se encontro la pagina solicitada"}


def test_leer_naturalezas():
    response = client.get("/teams/nature")
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


def test_get_team_by_id_empty_list():
    response = client.get("/teams/1")
    assert response.status_code == 404
    assert response.json()["detail"] == "Equipo no encontrado"


def test_get_team_by_id():
    global lista_equipos
    lista_equipos.extend(
        [
            {
                "id": 1,
                "nombre": "Equipo A",
                "generacion": 1,
                "pokemones": [
                    {
                        "id": 1,
                        "nombre": "Pikachu",
                        "movimientos": [1, 2],
                        "naturaleza_id": 1,
                        "stats": {},
                    }
                ],
            },
            {
                "id": 2,
                "nombre": "Equipo B",
                "generacion": 2,
                "pokemones": [
                    {
                        "id": 2,
                        "nombre": "Charmander",
                        "movimientos": [2],
                        "naturaleza_id": 1,
                        "stats": {},
                    }
                ],
            },
        ]
    )

    team_id = lista_equipos[0]["id"]
    print("hola")
    response = client.get(f"/teams/{team_id}")
    print("buenas")
    assert response.status_code == 200
    content = response.json()
    assert content["id"] == int(team_id)
    assert content["nombre"] == "Equipo A"
    assert len(content["pokemones"]) == 1
    assert content["pokemones"][0]["nombre"] == "Pikachu"


def test_get_team_by_id_not_found():
    response = client.get("/teams/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Equipo no encontrado"}


def test_get_team_by_id_invalid():
    response = client.get("/teams/abc")
    assert response.status_code == 400
    assert response.json() == {"detail": "El id debe ser un numero entero"}



def test_create_team_success(client: TestClient):
    team_create = {
        "generacion": 1,
        "nombre": "Equipo 1",
        "integrantes": [
            {
                "nombre": "Pikachu",
                "id_pokemon": 1,
                "id_naturaleza": 1,
                "movimientos": [1]
            }
        ]
    }

    response = client.post("/teams/", json=team_create)
    
    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == team_create["nombre"]
    assert len(data["integrantes"]) == 1

def test_create_team_invalid_generation(client: TestClient):
    team_data = {
        "nombre": "Equipo A",
        "generacion": 10,
        "pokemones": [
            {
                "id": 1,
                "nombre": "Pikachu",
                "movimientos": [1],
                "naturaleza_id": 1,
                "stats": {},
            }
        ],
    }

    response = client.post("/teams/", json=team_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "No se encontró la generacion"


def test_create_team_invalid_pokemons(client: TestClient):
    team_data = {"nombre": "Equipo A", "generacion": 1, "pokemones": []}

    response = client.post("/teams/", json=team_data)
    assert response.status_code == 400
    assert (
        response.json()["detail"]
        == "Debe elegir al menos 1 pokemon y no mas de 6 pokemones"
    )