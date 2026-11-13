import pickle
import numpy as np
import pandas as pd
from pathlib import Path

from schemas import LaptopInput

MODEL_DIR = Path(__file__).resolve().parent / "models"

# Load trained model
with open(MODEL_DIR / "Laptop_Price_Predictor.pkl", "rb") as f:
    model = pickle.load(f)

# Load preprocessor
with open(MODEL_DIR / "preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)


def predict_price(data: LaptopInput) -> float:

    ppi = np.sqrt(
        data.resolution_width**2 +
        data.resolution_height**2
    ) / data.screen_size

    features = pd.DataFrame([{
        "Company": data.company,
        "TypeName": data.typename,
        "Cpu": data.cpu,
        "Ram": data.ram,
        "OpSys": data.os,
        "Weight": data.weight,
        "TouchScreen": int(data.touchscreen),
        "IPS Panel": int(data.ips_panel),
        "ppi": ppi,
        "HDD": data.hdd,
        "SDD": data.ssd,
        "Hybrid": data.hybrid,
        "Flash_drive": data.flash_drive,
        "Gpu_brand": data.gpu_brand
    }])

    transformed = preprocessor.transform(features)

    prediction = model.predict(transformed)[0]

    price = np.exp(prediction)

    return round(float(price), 2)