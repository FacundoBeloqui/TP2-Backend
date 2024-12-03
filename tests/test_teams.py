import pytest
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy.pool import StaticPool
from main import app
from database import get_db
from modelos import Integrante, Team, TeamCreate

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


def test_crear_equipo(client: TestClient, session: Session):
    data = {
        "nombre": "Equipo 1",
        "generacion": 1,
        "integrantes": [],
    }
    response = client.post("/teams/", json=data)
    assert response.status_code == 400


def test_obtener_equipos(client: TestClient):
    response = client.get("/teams/")
    assert response.status_code == 200
    content = response.json()
    assert isinstance(content, list)


def test_obtener_equipo_por_id(client: TestClient, session: Session):
    team = Team(nombre="Equipo 2", generacion=2)
    session.add(team)
    session.commit()
    session.refresh(team)

    response = client.get(f"/teams/{team.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["nombre"] == team.nombre


def test_eliminar_equipo(client: TestClient, session: Session):
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


def test_eliminar_equipo_no_existente(client: TestClient):
    response = client.delete("/teams/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Equipo no encontrado"}
