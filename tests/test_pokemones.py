import pytest
from fastapi.testclient import TestClient
from main import app
from db import lista_pokemones
from routes.pokemones.pokemon import (
    calcular_debilidades,
    calcular_fortalezas,
    obtener_movimientos_pokemon,
)
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from modelos import Pokemon
from database import get_db


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_db] = get_session_override

    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_leer_pokemones(session: Session, client: TestClient) -> None:
    pok1 = Pokemon(
        identificador="Nombre1",
        altura=111,
        peso=2,
        experiencia_base=1,
        imagen="asdada",
        grupo_de_huevo="dasdad",
        habilidades=["comer", "dormir"],
        evoluciones_inmediatas=["pokemon2"],
        tipo=["fuego", "piedra"],
        estadisticas={"ataque": 2, "defensa": 3},
        id_especie=5,
    )
    session.add(pok1)
    session.commit()

    response = client.get(
        "/pokemones/",
    )

    assert response.status_code == 200
    content = response.json()
    assert len(content) == 1


"""
def test_leer_pokemon_id():
    response = client.get("/pokemones/1")

    assert response.status_code == 200

    data = response.json()["pokemon"]

    assert "id" in data
    assert "identificador" in data
    assert "id_especie" in data
    assert "altura" in data
    assert "peso" in data
    assert "experiencia_base" in data
    assert "tipo" in data
    assert "imagen" in data
    assert "grupo_de_huevo" in data
    assert "estadisticas" in data
    assert "habilidades" in data

    assert data["id"] == 1


def test_leer_pokemon_no_existente():
    response = client.get("/pokemones/9999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Pokémon no encontrado"}


def test_leer_pokemon_con_id_invalido():
    response = client.get("/pokemones/abc")
    assert response.status_code == 422


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


def test_create_pokemon():
    data = {
        "identificador": "Test",
        "altura": 25,
        "peso": 19,
        "experiencia_base": 250,
        "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/numero_id.png",
        "tipo": ["Humo", "Saltar"],
        "grupo_de_huevo": "Huevo",
        "estadisticas": {"ATK": 200, "DEF": 250},
        "habilidades": ["Salto", "Invisible"],
        "generaciones": [],
        "evoluciones_inmediatas": [],
    }
    response = client.post("/pokemones", json=data)
    assert response.status_code == 201
    content = response.json()
    assert isinstance(content, dict)
    assert content["identificador"] == "Test"
    assert content["altura"] == 25
    assert content["peso"] == 19
    assert content["experiencia_base"] == 250
    assert (
        content["imagen"]
        == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/numero_id.png"
    )
    assert content["tipo"] == ["Humo", "Saltar"]
    assert content["grupo_de_huevo"] == "Huevo"
    assert content["estadisticas"] == {"ATK": 200, "DEF": 250}
    assert content["habilidades"] == ["Salto", "Invisible"]
    assert content["evoluciones_inmediatas"] == []
    assert "id" in content
    assert "id_especie" in content


def test_obtener_movimientos_pokemon_existente_con_movimientos():
    pokemon_id = 1
    response = client.get(f"/pokemones/{pokemon_id}/movimientos")

    assert response.status_code == 200
    data = response.json()

    assert "id_pokemon" in data
    assert data["id_pokemon"] == pokemon_id
    assert "nombre_pokemon" in data
    assert "tipos" in data
    assert "movimientos" in data

    movimientos = data["movimientos"]
    assert len(movimientos) > 0
    for movimiento in movimientos:
        assert "id" in movimiento
        assert "nombre" in movimiento
        assert "nivel" in movimiento
        assert "es_evolucionado" in movimiento
        assert movimiento["id"] in datos_movimientos.movimientos


def test_obtener_movimientos_pokemon_no_existente():
    pokemon_id = 99999
    response = client.get(f"/pokemones/{pokemon_id}/movimientos")

    assert response.status_code == 404
    data = response.json()
    assert data == {"detail": "Pokémon no encontrado"}


def test_obtener_movimientos_pokemon_id_invalido():
    response = client.get("/pokemones/abc/movimientos")

    assert response.status_code == 422
    data = response.json()

    assert "detail" in data
    assert "msg" in data["detail"][0]
    assert "type" in data["detail"][0]

    assert (
        data["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )
    assert data["detail"][0]["type"] in ["type_error.integer", "int_parsing"]
"""
