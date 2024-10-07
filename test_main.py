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


def test_eliminar_pokemon_existente():
    # Realiza una petición DELETE para eliminar un Pokémon existente
    response = client.delete("/pokemones/1")

    # Verifica que la respuesta tenga un código de estado 200
    assert response.status_code == 200
    assert response.json() == {"Mensaje": "Pokémon eliminado correctamente"}

    # Verifica que el Pokémon ha sido eliminado de la lista
    assert len(lista_pokemones) == 1
    assert lista_pokemones[0].id == 2  # Verifica que el Pokémon restante sea bulbasaur


def test_eliminar_pokemon_ya_eliminado():
    # Intentar eliminar el mismo Pokémon que ya fue eliminado
    response = client.delete("/pokemones/1")  # ID que ya no existe

    # Verifica que la respuesta tenga un código de estado 404
    assert response.status_code == 404
    assert response.json() == {"detail": "Pokémon no encontrado"}


def test_eliminar_pokemon_no_existente():
    # Realiza una petición DELETE para eliminar un Pokémon que no existe
    response = client.delete("/pokemones/999")  # ID que no existe

    # Verifica que la respuesta tenga un código de estado 404
    assert response.status_code == 404
    assert response.json() == {"detail": "Pokémon no encontrado"}


def test_eliminar_pokemon_id_invalido():
    # Realiza una petición DELETE con un ID negativo
    response = client.delete("/pokemones/-1")

    # Verifica que la respuesta tenga un código de estado 400
    assert response.status_code == 400
    assert response.json() == {"detail": "ID debe ser un número positivo"}
