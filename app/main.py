from fastapi import FastAPI, HTTPException
import uuid
from app.models import Receipt, PointsResponse
from app.services import calculate_points
from app.storage import receipt_store

app = FastAPI(title="Receipt Processor")

@app.post("/receipts/process", response_model=dict)
async def process_receipt(receipt: Receipt):
    receipt_id = str(uuid.uuid4())
    points = calculate_points(receipt)
    receipt_store[receipt_id] = points
    return {"id": receipt_id}

@app.get("/receipts/{id}/points", response_model=PointsResponse)
async def get_points(id: str):
    if id not in receipt_store:
        raise HTTPException(status_code=404, detail="No receipt found for that ID.")
    return {"points": receipt_store[id]}
