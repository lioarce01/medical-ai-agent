import os
import pandas as pd
from sklearn.ensemble import IsolationForest
from app.infrastructure.influxdb_client import InfluxDBHandler

class AnomalyDetector:
    def __init__(self):
        influx_host = os.getenv("INFLUX_HOST", "influxdb")
        influx_port = int(os.getenv("INFLUX_PORT", "8086"))
        influx_db = os.getenv("INFLUX_DB", "medical_data")
        influx_user = os.getenv("INFLUX_USER", "admin")
        influx_password = os.getenv("INFLUX_PASSWORD", "admin")

        self.influx = InfluxDBHandler(
            host=influx_host,
            port=influx_port,
            database=influx_db,
            username=influx_user,
            password=influx_password
        )

        self.models = {}

    def train_for_patient(self, patient_id: str):
        hr_data = self.influx.query_heart_rate(patient_id, limit=100)
        if len(hr_data) < 10:
            hr_data = [65, 70, 72, 68, 75, 80, 90, 85, 66, 74] * 3

        df = pd.DataFrame({"heart_rate": hr_data})
        model = IsolationForest(contamination=0.1, random_state=42)
        model.fit(df)
        self.models[patient_id] = model
    
    def predict(self, patient_id: str, vitals: dict) -> bool:
        if patient_id not in self.models:
            self.train_for_patient(patient_id)

        heart_rate = vitals.get("heart_rate", 0)
        input_df = pd.DataFrame({"heart_rate": [heart_rate]})
        prediction = self.models[patient_id].predict(input_df)[0]
        return prediction == -1
