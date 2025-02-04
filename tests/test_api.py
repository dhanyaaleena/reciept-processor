from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_process_receipt():
    receipt = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
            {"shortDescription": "Emils Cheese Pizza", "price": "12.25"}
        ],
        "total": "18.74"
    }
    response = client.post("/receipts/process", json=receipt)
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_points():
    receipt = {
        "retailer": "M&M Corner Market",
        "purchaseDate": "2022-03-20",
        "purchaseTime": "14:33",
        "items": [
            {"shortDescription": "Gatorade", "price": "2.25"},
            {"shortDescription": "Gatorade", "price": "2.25"}
        ],
        "total": "4.50"
    }
    post_response = client.post("/receipts/process", json=receipt)
    receipt_id = post_response.json()["id"]
    get_response = client.get(f"/receipts/{receipt_id}/points")
    assert get_response.status_code == 200
    assert "points" in get_response.json()
