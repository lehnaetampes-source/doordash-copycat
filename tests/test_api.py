import requests

BASE_URL = "http://localhost:8000"

def test_root():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_status():
    response = requests.get(f"{BASE_URL}/status/")
    assert response.status_code == 200
    assert response.json()["status"] == "Service is up and running"

def test_calculate_fee():
    payload = {
        "distance_km": 10,
        "weight_kg": 2
    }
    response = requests.post(
        f"{BASE_URL}/calculate-fee/",
        json=payload
    )
    assert response.status_code == 200
    assert "delivery_fee" in response.json()
