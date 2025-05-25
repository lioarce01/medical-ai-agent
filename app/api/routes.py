from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/predict")
def predict_vitals(patient_id: str = Body(...), vitals: dict = Body(...)):
    context = get_context(patient_id)
    model = AnomalyDectector()
    is_anomaly = model.predict(vitals)

    if is_anomaly:
        return handle_anomaly(context, vitals)
    return {"status": "normal", "message": "No anomalies detected."} 