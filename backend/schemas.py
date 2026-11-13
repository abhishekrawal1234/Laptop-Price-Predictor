
from pydantic import BaseModel, Field


class LaptopInput(BaseModel):
    company: str
    typename: str
    cpu: str
    ram: int = Field(gt=0)
    os: str
    weight: float = Field(gt=0)

    touchscreen: bool
    ips_panel: bool

    screen_size: float = Field(gt=0)
    resolution_width: int = Field(gt=0)
    resolution_height: int = Field(gt=0)

    hdd: int = Field(default=0, ge=0)
    ssd: int = Field(default=0, ge=0)
    hybrid: int = Field(default=0, ge=0)
    flash_drive: int = Field(default=0, ge=0)

    gpu_brand: str


class PredictionResponse(BaseModel):
    predicted_price: float
    currency: str
