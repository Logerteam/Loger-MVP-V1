from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["Users"])

class User(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(user: User):
    # Dummy logic for now
    if user.username == "admin" and user.password == "password":
        return {"token": "mock-token", "user": user.username}
    return {"error": "Invalid credentials"}
