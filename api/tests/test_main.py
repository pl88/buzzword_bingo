from fastapi.testclient import TestClient

from my_api.main import app


client = TestClient(app)


def test_read_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello from buzzword_bingo API"}
