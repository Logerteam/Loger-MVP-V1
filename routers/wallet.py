from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/wallet", tags=["Wallet"])

mock_wallet = {"balance": 1000}

class TopUpRequest(BaseModel):
    amount: float

@router.get("/balance")
def get_balance():
    return {"balance": mock_wallet["balance"]}

@router.post("/topup")
def topup_wallet(data: TopUpRequest):
    mock_wallet["balance"] += data.amount
    return {"new_balance": mock_wallet["balance"]}
