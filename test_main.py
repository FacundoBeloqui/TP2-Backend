from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_pokemon():
    data = {"identificador": "Test", "altura": 25, "peso": 19, "experiencia_base": 250, "imagen": "http://youtube.com", "tipo": ["Humo", "Saltar"]}
    response = client.post("/pokemons", json=data)
    assert response.status_code == 201
    content = response.json()
    assert isinstance(content, dict)
    assert content["identificador"] == "Test"
    assert content["altura"] == 25
    assert content["peso"] == 19
    assert content["experiencia_base"] == 250
    assert content["imagen"] == "http://youtube.com"
    assert content["tipo"] == ["Humo", "Saltar"]
    assert "id" in content


