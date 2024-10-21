from fastapi.testclient import TestClient
from main import app
from db import lista_naturalezas, Team, PokemonTeam, lista_pokemones, lista_movimientos
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

def test_get_team_by_id_empty_list():
    response = client.get("/teams/1") 
    assert response.status_code == 404
    assert response.json()["detail"] == "Equipo no encontrado"


def test_get_team_by_id():
    global lista_equipos
    lista_equipos.extend([{"id": 1, "nombre": "Equipo A", "generacion": 1, "pokemones": [{"id": 1, "nombre": "Pikachu", "movimientos": [1, 2], "naturaleza_id": 1, "stats": {}}]}, {"id": 2, "nombre": "Equipo B", "generacion": 2, "pokemones": [{"id": 2, "nombre": "Charmander", "movimientos": [2], "naturaleza_id": 1, "stats": {}}]}])

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

# def test_create_team_invalid_generation():
#     response = client.post("/", json={
#         "generacion": 10, 
#         "nombre": "Equipo de Prueba",
#         "pokemones": [pokemon_1.model_dump()]
#     })
#     assert response.status_code == 404
#     assert response.json().detail == "No se encontró la generacion"






# def test_create_team_success():
#     # Supongamos que ya tienes datos de Pokémon y movimientos
#     lista_pokemones.extend([{"id": 1, "nombre": "Equipo A", "generacion": 1, "pokemones": [{"id": 1, "nombre": "Pikachu", "movimientos": [1, 2], "naturaleza_id": 1, "stats": {}}]}, {"id": 2, "nombre": "Equipo B", "generacion": 2, "pokemones": [{"id": 2, "nombre": "Charmander", "movimientos": [2], "naturaleza_id": 1, "stats": {}}]}])
#     # lista_movimientos.extend([
#     #     {"id": 1, "nombre": "Rayo", "generacion": 1},
#     #     {"id": 2, "nombre": "Ascuas", "generacion": 1}
#     # ])
#     # generaciones_pokemon = {
#     #     1: [1],  
#     #     2: [2],  
#     # }

#     team_data = {
#         "nombre": "Equipo A",
#         "generacion": 1,
#         "pokemones": [
#             {"id": 1, "nombre": "Pikachu", "movimientos": [1], "naturaleza_id": 1, "stats": {}}
#         ]
#     }

#     response = client.post("/teams", json=team_data)
#     assert response.status_code == 200
#     content = response.json()
#     assert "pokemon" in content
#     assert len(content["pokemon"]) == 1
#     assert content["pokemon"][0]["nombre"] == "Pikachu"
#     assert len(lista_equipos) == 1


def test_create_team_invalid_generation():
    team_data = {
        "nombre": "Equipo A",
        "generacion": 10, 
        "pokemones": [
            {"id": 1, "nombre": "Pikachu", "movimientos": [1], "naturaleza_id": 1, "stats": {}}
        ]
    }

    response = client.post("/teams/", json=team_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "No se encontró la generacion"


def test_create_team_invalid_pokemons():
    team_data = {
        "nombre": "Equipo A",
        "generacion": 1,
        "pokemones": [] 
    }

    response = client.post("/teams/", json=team_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Debe elegir al menos 1 pokemon y no mas de 6 pokemones"






