from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/deliveries", tags=["Deliveries"])

class DeliveryRequest(BaseModel):
    pickup_point: str
    drop_points: List[str]
    weight: float
    time_window: str
    reverse_pickup: Optional[bool] = False

@router.post("/create")
def create_delivery(data: DeliveryRequest):
    # Mock price estimation
    base_price = 50
    price = base_price + data.weight * 2 + len(data.drop_points) * 10
    return {
        "status": "Order Created",
        "details": data,
        "estimated_price": price,
        "tracking_id": "LOG123456"
    }
