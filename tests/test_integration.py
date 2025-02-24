import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_execute_command_integration():
    response = client.post("/execute/", json={"command": "echo Hello, World!"})
    assert response.status_code == 200
    assert response.json()["result"].strip() == "Hello, World!"

def test_execute_invalid_command_integration():
    response = client.post("/execute/", json={"command": "invalid_command"})
    assert response.status_code == 500