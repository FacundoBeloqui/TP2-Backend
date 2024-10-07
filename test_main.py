from fastapi.testclient import TestClient
from main import app, lista_pokemones

client = TestClient(app)


def test_leer_pokemones():
    # Realiza una petición GET al endpoint /pokemons
    response = client.get("/pokemons")

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
