import pytest
from fastapi.testclient import TestClient
from main import app
from sqlmodel import Session, SQLModel, create_engine, select
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
        generacion=[1, 2],
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


def test_leer_pokemon_id(session: Session, client: TestClient) -> None:
    pok1 = Pokemon(
        identificador="Nombre1",
        altura=111,
        peso=2,
        experiencia_base=1,
        imagen="asdada",
        grupo_de_huevo="dasdad",
        generacion=[1, 2],
        habilidades=["comer", "dormir"],
        evoluciones_inmediatas=["pokemon2"],
        tipo=["fuego", "piedra"],
        estadisticas={"ataque": 2, "defensa": 3},
        id_especie=5,
    )
    session.add(pok1)
    session.commit()

    response = client.get(f"/pokemones/{pok1.id}")

    assert response.status_code == 200
    content = response.json()
    assert content["identificador"] == pok1.identificador
    assert content["altura"] == pok1.altura
    assert content["peso"] == pok1.peso
    assert content["experiencia_base"] == pok1.experiencia_base
    assert content["imagen"] == pok1.imagen
    assert content["grupo_de_huevo"] == pok1.grupo_de_huevo
    assert content["generacion"] == pok1.generacion
    assert content["habilidades"] == pok1.habilidades
    assert content["evoluciones_inmediatas"] == pok1.evoluciones_inmediatas
    assert content["tipo"] == pok1.tipo
    assert content["estadisticas"] == pok1.estadisticas
    assert content["id_especie"] == pok1.id_especie


def test_get_pokemones_vacio(client: TestClient) -> None:
    response = client.get(
        "/pokemones/",
    )
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 0


def test_leer_pokemon_no_existente(client: TestClient) -> None:
    response = client.get("/pokemones/9999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Pokemon no encontrado"}


def test_leer_pokemon_con_id_invalido(client: TestClient) -> None:
    response = client.get("/pokemones/abc")
    assert response.status_code == 422


def test_eliminar_pokemon_existente(session: Session, client: TestClient) -> None:
    pok1 = Pokemon(
        identificador="Nombre1",
        altura=111,
        peso=2,
        experiencia_base=1,
        imagen="asdada",
        grupo_de_huevo="dasdad",
        generacion=[1, 2],
        habilidades=["comer", "dormir"],
        evoluciones_inmediatas=["pokemon2"],
        tipo=["fuego", "piedra"],
        estadisticas={"ataque": 2, "defensa": 3},
        id_especie=5,
    )
    session.add(pok1)
    session.commit()

    largo_lista_pokemones_original = len(session.exec(select(Pokemon)).all())

    response = client.delete(f"/pokemones/{pok1.id}")

    assert response.status_code == 200

    largo_lista_pokemones_actual = len(session.exec(select(Pokemon)).all())
    assert largo_lista_pokemones_actual == largo_lista_pokemones_original - 1

    pokemon_eliminado = session.get(Pokemon, pok1.id)
    assert pokemon_eliminado is None


def test_eliminar_pokemon_ya_eliminado(client: TestClient) -> None:
    response = client.delete("/pokemones/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Pokémon no encontrado"}


def test_eliminar_pokemon_no_existente(client: TestClient) -> None:
    response = client.delete("/pokemones/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Pokémon no encontrado"}


def test_eliminar_pokemon_id_invalido(client: TestClient) -> None:
    response = client.delete("/pokemones/-1")
    assert response.status_code == 400
    assert response.json() == {"detail": "El id debe ser un numero entero positivo"}


def test_obtener_movimientos_pokemon_existente_con_movimientos(
    session: Session, client: TestClient
) -> None:
    pok1 = Pokemon(
        identificador="Nombre1",
        altura=111,
        peso=2,
        experiencia_base=1,
        imagen="asdada",
        grupo_de_huevo="dasdad",
        generacion=[1, 2],
        habilidades=["comer", "dormir"],
        evoluciones_inmediatas=["pokemon2"],
        tipo=["fuego", "piedra"],
        estadisticas={"ataque": 2, "defensa": 3},
        id_especie=5,
    )
    session.add(pok1)
    session.commit()

    response = client.get(f"/pokemones/{pok1.id}/movimientos")

    assert response.status_code == 200
    content = response.json()
    assert len(content) > 0


def test_obtener_movimientos_pokemon_no_existente(client: TestClient):
    pokemon_id = 99999
    response = client.get(f"/pokemones/{pokemon_id}/movimientos")

    assert response.status_code == 404
    data = response.json()
    assert data == {"detail": "Pokémon no encontrado"}


def test_obtener_movimientos_pokemon_id_invalido(client: TestClient):
    response = client.get(f"/pokemones/abc/movimientos")

    assert response.status_code == 422
