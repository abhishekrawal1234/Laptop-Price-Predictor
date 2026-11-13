
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from schemas import LaptopInput, PredictionResponse
from predictor import predict_price

# Initialize FastAPI
app = FastAPI(
    title="Laptop Price Predictor API",
    description="Predict laptop prices using a trained VotingRegressor",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173"
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"]
)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Laptop Price Predictor API",
        "status": "running"
    }


# Health check endpoint
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model": "VotingRegressor"
    }


# Laptop price prediction endpoint
@app.post(
    "/predict",
    response_model=PredictionResponse,
    tags=["Prediction"]
)
def predict(laptop: LaptopInput):
    try:
        predicted_price = predict_price(laptop)

        return PredictionResponse(
            predicted_price=predicted_price,
            currency="INR"
        )

    except Exception as e:
        # Log error in terminal for debugging
        import logging
        logging.exception("Prediction failed")

        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Check server logs."
        ) from e
