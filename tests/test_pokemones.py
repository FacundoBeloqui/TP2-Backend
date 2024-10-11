from fastapi.testclient import TestClient
from main import app
from db import lista_pokemones

client = TestClient(app)


def test_leer_pokemones():
    # Realiza una petición GET al endpoint /pokemons
    response = client.get("/pokemones")

    # Verifica que la respuesta tenga un código de estado 200
    assert response.status_code == 200
    content = response.json()
    # Verifica que el contenido devuelto sea una lista
    assert isinstance(content, list)

    # Verifica que los datos coincidan con lo que esperas
    if lista_pokemones:
        assert len(content) == len(lista_pokemones)
        primer_pokemon = content[0]
        assert primer_pokemon["id"] == lista_pokemones[0].id
        assert primer_pokemon["identificador"] == lista_pokemones[0].identificador
        assert primer_pokemon["imagen"] == lista_pokemones[0].imagen
        assert primer_pokemon["tipo"] == lista_pokemones[0].tipo


def test_eliminar_pokemon_existente():
    largo_lista_pokemones_original = len(lista_pokemones)
    primer_pokemon = lista_pokemones[0]
    response = client.delete("/pokemones/1")
    assert response.status_code == 200
    assert response.json() == primer_pokemon.model_dump()
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
