class AnomalyDetector:
    def predict(self, vitals: dict) -> bool:
        heart_rate = vitals.get("heart_rate", 0)
        return heart_rate > 120