class PatientContext:
    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.risk_level = "high"
        self.alerts = []
