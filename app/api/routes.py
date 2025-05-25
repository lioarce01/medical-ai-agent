from fastapi import APIRouter, Body
from app.context.manager import get_context
from app.models.anomaly_detector import AnomalyDetector
from app.protocols.anomaly_protocol import handle_anomaly

router = APIRouter()

@router.post("/predict")
def predict_vitals(patient_id: str = Body(...), vitals: dict = Body(...)):
    context = get_context(patient_id)
    model = AnomalyDetector()
    is_anomaly = model.predict(vitals)

    if is_anomaly:
        return handle_anomaly(context, vitals)
    return {"status": "normal", "message": "No anomalies detected."} 