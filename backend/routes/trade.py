# Purpose - Defines the /recommend endpoint that returns trade suggestions. 
from fastapi import APIRouter
from backend.services.recommender import generate_trade_recommendations

router = APIRouter()

@router.get("/recommend")
def recommend_trades():
    recommendations = generate_trade_recommendations()
    return {"recommendations": recommendations}
