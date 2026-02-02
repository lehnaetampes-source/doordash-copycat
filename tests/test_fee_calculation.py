import requests

def test_calculate_fee_valid():
    payload = {"distance_km": 10, "weight_kg": 2}
    r = requests.post(
        "http://localhost:8000/calculate-fee/",
        json=payload
    )
    assert r.status_code == 200
    assert "delivery_fee" in r.json()

def test_calculate_fee_invalid():
    payload = {"distance_km": -1, "weight_kg": 2}
    r = requests.post(
        "http://localhost:8000/calculate-fee/",
        json=payload
    )
    assert r.status_code in [400, 422]
