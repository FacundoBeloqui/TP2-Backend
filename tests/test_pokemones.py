from fastapi.testclient import TestClient
from main import app
from db import lista_pokemones
from routes.pokemones.pokemon import calcular_debilidades, calcular_fortalezas

client = TestClient(app)


def test_leer_pokemones():
    response = client.get("/pokemones")

    assert response.status_code == 200
    content = response.json()
    assert isinstance(content, list)

    if lista_pokemones:
        assert len(content) == len(lista_pokemones)
        primer_pokemon = content[0]
        assert primer_pokemon["id"] == lista_pokemones[0].id
        assert primer_pokemon["identificador"] == lista_pokemones[0].identificador
        assert primer_pokemon["imagen"] == lista_pokemones[0].imagen
        assert primer_pokemon["tipo"] == lista_pokemones[0].tipo


def test_leer_pokemon_id():
    pokemon_id = 1
    response = client.get(f"/pokemones/{pokemon_id}")

    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "identificador" in data
    assert "id_especie" in data
    assert "altura" in data
    assert "peso" in data
    assert "experiencia_base" in data
    assert "orden" in data
    assert "es_default" in data
    assert "imagen" in data
    assert "tipo" in data
    assert "grupo_de_huevo" in data

    assert data["id"] == pokemon_id


def test_eliminar_pokemon_existente():
    largo_lista_pokemones_original = len(lista_pokemones)
    primer_pokemon = lista_pokemones[0]
    response = client.delete("/pokemones/1")
    assert response.status_code == 200
    assert response.json() == {
        "pokemon": primer_pokemon.model_dump(),
        "debilidades": calcular_debilidades(primer_pokemon),
        "fortalezas": calcular_fortalezas(primer_pokemon),
    }
    assert len(lista_pokemones) == largo_lista_pokemones_original - 1
    assert lista_pokemones[0].id == 2


def test_eliminar_pokemon_ya_eliminado():
    response = client.delete("/pokemones/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Pokemon no encontrado"}


def test_eliminar_pokemon_no_existente():
    response = client.delete("/pokemones/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Pokemon no encontrado"}


def test_eliminar_pokemon_id_invalido():
    response = client.delete("/pokemones/-1")
    assert response.status_code == 400
    assert response.json() == {"detail": "El id debe ser un numero entero"}


def test_leer_pokemon_existente():
    response = client.get("/pokemones/1")
    assert response.status_code == 200
    pokemon = lista_pokemones[0]
    assert response.json() == {
        "pokemon": pokemon.model_dump(),
        "debilidades": calcular_debilidades(pokemon),
        "fortalezas": calcular_fortalezas(pokemon),
    }


def test_leer_pokemon_no_existente():
    response = client.get("/pokemones/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Pokémon no encontrado"}


def test_leer_pokemon_con_id_invalido():
    response = client.get("/pokemones/not_a_number")
    assert response.status_code == 422
