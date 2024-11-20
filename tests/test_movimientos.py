import pytest
from fastapi.testclient import TestClient
from main import app
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool
from modelos import Movimiento
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


def test_leer_movimientos(session: Session, client: TestClient) -> None:
    mov1 = Movimiento(
        nombre="Movimiento1",
        generacion=1,
        tipo="fuego",
        poder="50",
        accuracy="100",
        pp="15",
        categoria="especial",
        efecto="quemar",
        pokemones_subida_nivel=["pokemon1", "pokemon2"],
        pokemones_tm=["pokemon3", "pokemon4"],
        pokemones_grupo_huevo=["pokemon5", "pokemon6"],
    )
    session.add(mov1)
    session.commit()

    response = client.get(
        "/movimientos/",
    )

    assert response.status_code == 200
    content = response.json()
    assert len(content) == 1


def test_get_movimientos_vacio(client: TestClient) -> None:
    response = client.get(
        "/movimientos/",
    )
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 0


def test_obtener_movimiento_existente(session: Session, client: TestClient) -> None:
    movimiento = Movimiento(
        id=1,
        nombre="pokemon1",
        generacion=1,
        tipo="fuego",
        poder="110",
        accuracy="85",
        pp="5",
        categoria="especial",
        efecto="puede causar quemaduras",
    )
    session.add(movimiento)
    session.commit()

    response = client.get(f"/movimientos/{movimiento.id}")
    assert response.status_code == 200
    content = response.json()
    assert content["nombre"] == movimiento.nombre
    assert content["tipo"] == movimiento.tipo
    assert content["poder"] == movimiento.poder
    assert content["accuracy"] == movimiento.accuracy
    assert content["pp"] == movimiento.pp
    assert content["categoria"] == movimiento.categoria
    assert content["efecto"] == movimiento.efecto


def test_obtener_movimiento_no_existente(client: TestClient) -> None:
    response = client.get("/movimientos/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Movimiento not found"}


def test_obtener_movimiento_id_invalido(client: TestClient) -> None:
    response = client.get("/movimientos/abc")
    assert response.status_code == 422
