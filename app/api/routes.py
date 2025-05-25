from fastapi import APIRouter
from pydantic import BaseModel
from app.context.manager import get_context
from app.models.anomaly_detector import AnomalyDetector
from app.protocols.anomaly_protocol import handle_anomaly
from app.infrastructure.influxdb_client import influx_handler

router = APIRouter()
detector = AnomalyDetector()

class InputData(BaseModel):
    patient_id: str
    vitals: dict

@router.post("/predict")
def predict(data: InputData):
    context = get_context(data.patient_id)
    
    influx_handler.write_heart_rate(data.patient_id, data.vitals.get("heart_rate"))
    
    is_anomaly = detector.predict(data.patient_id, data.vitals)

    if is_anomaly:
        result = handle_anomaly(context, data.vitals)
        return {"status": "anomaly", **result}
    return {"status": "normal", "message": "No anomalies detected."}
