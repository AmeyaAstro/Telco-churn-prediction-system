from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_churn

app = FastAPI(
    title="Telco Churn Prediction API",
    version="1.0"
)

class CustomerData(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.get("/")
def root():
    return {
        "message": "Telco Churn Prediction API is running"
    }

@app.post("/predict")
def predict(customer: CustomerData):
    customer_dict = customer.model_dump()

    result = predict_churn(customer_dict)

    return result