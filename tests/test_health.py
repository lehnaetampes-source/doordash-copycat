import requests

def test_status():
    r = requests.get("http://localhost:8000/status/")
    assert r.status_code == 200
    assert r.json()["status"] == "Service is up and running"
