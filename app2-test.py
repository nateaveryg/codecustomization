import pytest
from app2 import app  # Or backend_handlers depending on your preference
import json


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_discovery_route(client):
    response = client.get("/discovery")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["name"] == "shipping"
    assert data["version"] == "1.0"
    assert "owners" in data
    assert "team" in data
    assert "organization" in data

def test_liveness_route(client):
    response = client.get("/liveness")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "live"
    assert data["code"] == 200
    assert "timestamp" in data

def test_readiness_route(client):
    response = client.get("/readiness")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["status"] == "ready"
    assert data["code"] == 200
    assert "timestamp" in data
