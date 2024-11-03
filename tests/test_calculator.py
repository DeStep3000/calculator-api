from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_addition():
    response = client.get("/add?x=1&y=2")  # предполагается, что у вас есть такой эндпоинт
    assert response.status_code == 200
    assert response.json() == {"result": 3}

def test_subtraction():
    response = client.get("/subtract?x=5&y=3")
    assert response.status_code == 200
    assert response.json() == {"result": 2}
