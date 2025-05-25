def handle_anomaly(context, vitals):
    message = f"Anomaly detected for patient {context.patient_id}"
    return {
        "status": "anomaly",
        "action": "notify",
        "message": message,
        "heart_rate": vitals.get("heart_rate")
    }
