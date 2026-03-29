from fastapi import FastAPI
from models import UserProfile
from recommender import generate_recommendation

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI CONCIERGE Backend Running 🚀"}

@app.post("/recommend")
def recommend(user: UserProfile):
    return generate_recommendation(user.dict())