import pytest
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy.pool import StaticPool
from main import app
from database import get_db
from modelos import Integrante, Team

client = TestClient(app)


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


def test_crear_equipo(client: TestClient, session: Session) -> None:
    data = {"nombre": "Equipo 1", "generacion": 1, "integrantes": []}
    response = client.post("/teams/", json=data)
    assert response.status_code == 201
    content = response.json()
    assert content["nombre"] == "Equipo 1"
    assert content["generacion"] == 1


def test_obtener_equipos(client: TestClient) -> None:
    response = client.get("/teams/")
    assert response.status_code == 200
    content = response.json()
    assert isinstance(content, list)


def test_obtener_equipo_por_id(client: TestClient, session: Session) -> None:
    team = Team(nombre="Equipo 2", generacion=2)
    session.add(team)
    session.commit()
    session.refresh(team)

    response = client.get(f"/teams/{team.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["nombre"] == team.nombre


def test_agregar_integrante(client: TestClient, session: Session) -> None:
    team = Team(nombre="Equipo 3", generacion=3)
    session.add(team)
    session.commit()
    session.refresh(team)

    integrante_data = {
        "nombre": "Integrante 1",
        "id_pokemon": 1,
        "id_naturaleza": 1,
        "movimientos": [1, 2],
    }
    response = client.post(f"/teams/{team.id}/integrantes", json=integrante_data)
    assert response.status_code == 201
    content = response.json()
    assert content["nombre"] == "Integrante 1"


def test_actualizar_integrante(client: TestClient, session: Session) -> None:
    team = Team(nombre="Equipo 4", generacion=4)
    session.add(team)
    session.commit()
    session.refresh(team)

    integrante = Integrante(nombre="Integrante 2", id_equipo=team.id)
    session.add(integrante)
    session.commit()
    session.refresh(integrante)

    update_data = {
        "id_integrante": integrante.id,
        "nombre": "Integrante Actualizado",
        "id_pokemon": 1,
        "id_naturaleza": 1,
        "movimientos": [1, 2],
    }
    response = client.put(f"/teams/{team.id}/integrantes", json=update_data)
    assert response.status_code == 200
    content = response.json()
    assert content["nombre"] == "Integrante Actualizado"


def test_eliminar_integrante(client: TestClient, session: Session) -> None:
    team = Team(nombre="Equipo 5", generacion=5)
    session.add(team)
    session.commit()
    session.refresh(team)

    integrante = Integrante(nombre="Integrante 3", id_equipo=team.id)
    session.add(integrante)
    session.commit()
    session.refresh(integrante)

    response = client.delete(f"/teams/{team.id}/integrantes/{integrante.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["nombre"] == "Integrante 3"

    response = client.get(f"/teams/{team.id}/integrantes/{integrante.id}")
    assert response.status_code == 404


def test_eliminar_equipo(client: TestClient, session: Session) -> None:
    team = Team(nombre="Equipo 6", generacion=6)
    session.add(team)
    session.commit()
    session.refresh(team)

    response = client.delete(f"/teams/{team.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["nombre"] == team.nombre

    response = client.get(f"/teams/{team.id}")
    assert response.status_code == 404


def test_eliminar_equipo_no_existente(client: TestClient) -> None:
    response = client.delete("/teams/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Equipo no encontrado"}


def test_crear_equipo_con_integrantes(client: TestClient, session: Session) -> None:
    data = {
        "nombre": "Equipo 7",
        "generacion": 1,
        "integrantes": [
            {
                "nombre": "Integrante 4",
                "id_pokemon": 1,
                "id_naturaleza": 1,
                "movimientos": [1, 2],
            }
        ],
    }
    response = client.post("/teams/", json=data)
    assert response.status_code == 201
    content = response.json()
    assert content["nombre"] == "Equipo 7"
    assert len(content["integrantes"]) == 1
    assert content["integrantes"][0]["nombre"] == "Integrante 4"
