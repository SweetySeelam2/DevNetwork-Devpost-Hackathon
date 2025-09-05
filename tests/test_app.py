import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_check():
    """Ensure health endpoint returns OK."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"ok": True}

def test_inbound_sms():
    """Simulate inbound SMS and verify auto-reply response structure."""
    payload = {"msisdn": "+1234567890", "to": "+18334296093", "text": "Hello"}
    response = client.post("/inbound", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert "status" in body