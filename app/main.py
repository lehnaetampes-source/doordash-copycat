from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DeliveryFeeRequest(BaseModel):
    distance_km: float
    weight_kg: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the DoorDash Delivery Fee Service API"}

@app.get("/status/")
def service_status():
    return {"status": "Service is up and running"}

@app.post("/calculate-fee/")
def calculate_fee(request: DeliveryFeeRequest):
    base_fee = 5.0
    return {
        "delivery_fee": base_fee
        + 1.5 * request.distance_km
        + 0.5 * request.weight_kg
    }
