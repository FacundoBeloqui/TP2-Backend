from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
from db import Team, lista_naturalezas


client = TestClient(app)

def test_leer_naturalezas():
    response = client.get("/teams")

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


# lista_equipos_prueba = [
#         Team(id=1, name="Equipo A", pokemones_incluidos=[
#         {
#             "id": 1,
#             "identificador": "pikachu",
#             "id_especie": 25,
#             "altura": 40,
#             "peso": 60,
#             "experiencia_base": 112,
#             "imagen": "http://example.com/pikachu.png",
#             "tipo": ["Electrico"],
#             "grupo_de_huevo": "Grupo 1",
#             "estadisticas": {"ataque": 55, "defensa": 40},
#             "habilidades": ["static", "lightning-rod"]
#         }]),
#         Team(id=2, name="Equipo B", pokemones_incluidos=[
#         {
#             "id": 2,
#             "identificador": "charmander",
#             "id_especie": 4,
#             "altura": 60,
#             "peso": 85,
#             "experiencia_base": 62,
#             "imagen": "http://example.com/charmander.png",
#             "tipo": ["Fuego"],
#             "grupo_de_huevo": "Grupo 1",
#             "estadisticas": {"ataque": 52, "defensa": 43},
#             "habilidades": ["blaze", "solar-power"]
#         }
#         ]),
# ]


def test_get_team_by_id():
    lista_equipos_prueba = [
        Team(id=1, nombre="Equipo A", pokemones_incluidos=[
        {
            "id": 1,
            "identificador": "pikachu",
            "id_especie": 25,
            "altura": 40,
            "peso": 60,
            "experiencia_base": 112,
            "imagen": "http://example.com/pikachu.png",
            "tipo": ["Electrico"],
            "grupo_de_huevo": "Grupo 1",
            "estadisticas": {"ataque": 55, "defensa": 40},
            "habilidades": ["static", "lightning-rod"]
        }])
    ]
    response = client.get("/teams/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "nombre": "Equipo A", "pokemones_incluidos": [
        {
            "id": 1,
            "identificador": "pikachu",
            "id_especie": 25,
            "altura": 40,
            "peso": 60,
            "experiencia_base": 112,
            "imagen": "http://example.com/pikachu.png",
            "tipo": ["Electrico"],
            "grupo_de_huevo": "Grupo 1",
            "estadisticas": {"ataque": 55, "defensa": 40},
            "habilidades": ["static", "lightning-rod"]
        }]}

def test_get_team_by_id_not_found():
    response = client.get("/teams/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Equipo no encontrado"}


def test_get_team_by_id_invalid():
    response = client.get("/teams/abc")
    assert response.status_code == 400
    assert response.json() == {"detail": "El id debe ser un numero entero"}


def test_create_team():
    pokemon_data = [
        {
            "id": 1,
            "identificador": "pikachu",
            "id_especie": 25,
            "altura": 40,
            "peso": 60,
            "experiencia_base": 112,
            "imagen": "http://example.com/pikachu.png",
            "tipo": ["Electrico"],
            "grupo_de_huevo": "Grupo 1",
            "estadisticas": {"ataque": 55, "defensa": 40},
            "habilidades": ["static", "lightning-rod"]
        },
        {
            "id": 2,
            "identificador": "charmander",
            "id_especie": 4,
            "altura": 60,
            "peso": 85,
            "experiencia_base": 62,
            "imagen": "http://example.com/charmander.png",
            "tipo": ["Fuego"],
            "grupo_de_huevo": "Grupo 1",
            "estadisticas": {"ataque": 52, "defensa": 43},
            "habilidades": ["blaze", "solar-power"]
        }
    ]
    
    team_data = {
        "id": 1,
        "nombre": "Equipo A",
        "pokemones_incluidos": pokemon_data
    }

    response = client.post("/", json=team_data)
    assert response.status_code == 200
    assert response.json() == {"id": 1, "nombre": "Equipo A", "pokemones_incluidos": pokemon_data}

def test_create_team_nombre_vacio():
    pokemon_data = [
        {
            "id": 3,
            "identificador": "bulbasaur",
            "id_especie": 1,
            "altura": 70,
            "peso": 69,
            "experiencia_base": 64,
            "imagen": "http://example.com/bulbasaur.png",
            "tipo": ["Planta", "Veneno"],
            "grupo_de_huevo": "Grupo 1",
            "estadisticas": {"ataque": 49, "defensa": 49},
            "habilidades": ["overgrow", "chlorophyll"]
        }
    ]

    team_data = {
        "nombre": "",
        "pokemones_incluidos": pokemon_data
    }

    response = client.post("/", json=team_data)
    assert response.status_code == 422 


def test_create_team_without_pokemones():
    team_data = {
        "nombre": "Equipo B",
        "pokemones_incluidos": []
    }

    response = client.post("/", json=team_data)
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "nombre": "Equipo B",
        "pokemones_incluidos": []
    }
