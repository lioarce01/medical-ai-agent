from app.context.base import PatientContext

_context_store = {}

def get_context(patient_id: str) -> PatientContext:
    if patient_id not in _context_store:
        _context_store[patient_id] = PatientContext(patient_id)
    return _context_store[patient_id]
