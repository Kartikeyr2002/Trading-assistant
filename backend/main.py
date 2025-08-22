#Purpose - entry point to your FastAPI app
from fastapi import FastAPI
from backend.routes import trade

app = FastAPI()

app.include_router(trade.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Powered Trading Assistant API"}
