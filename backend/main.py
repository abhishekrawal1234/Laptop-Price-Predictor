from fastapi import FastAPI
from predictor import model

app = FastAPI(
    title="Laptop Price Predictor API",
    description="Laptop price prediction using VotingRegressor",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Laptop Price Predictor API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": type(model).__name__
    }