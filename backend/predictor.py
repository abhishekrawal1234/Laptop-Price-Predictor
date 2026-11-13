import pickle
from pathlib import Path

MODEL_PATH = (
    Path(__file__).resolve().parent
    / "models"
    / "Laptop_Price_Predictor.pkl"
)

# Load the trained VotingRegressor
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


def predict_price(features):
    prediction = model.predict(features)
    return float(prediction[0])