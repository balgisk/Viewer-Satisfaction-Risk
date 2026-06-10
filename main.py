from fastapi import FastAPI
import predictor

app = FastAPI(
    title="Viewer Satisfaction Prediction API",
    description="Predict movie satisfaction from audience perspective",
    version="1.0"
)

@app.post("/predict")
def predict(data: dict):
    return predictor.predict(data)