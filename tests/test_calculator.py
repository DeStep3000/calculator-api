import sys
import os
from fastapi.testclient import TestClient
from main import app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

client = TestClient(app)

def test_addition():
    response = client.get("/add?x=1.5&y=2.5")  # Используем float значения
    assert response.status_code == 200
    assert response.json() == {"result": 4.0}  # Ожидаемое значение

def test_subtraction():
    response = client.get("/subtract?x=5.0&y=3.0")  # Используем float значения
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}  # Ожидаемое значение
