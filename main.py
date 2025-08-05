from fastapi import FastAPI
from routers import users, deliveries, wallet
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS setup for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(deliveries.router)
app.include_router(wallet.router)

@app.get("/")
def root():
    return {"message": "Welcome to Loger backend"}
