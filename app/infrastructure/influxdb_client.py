from influxdb import InfluxDBClient
import os

class InfluxDBHandler:
    def __init__(self, host: str, port: int, database: str, username: str = None, password: str = None):
        self.client = InfluxDBClient(
            host=host,
            port=port,
            username=username,
            password=password,
            database=database
        )
    

    def query_heart_rate(self, patient_id: str, limit: int = 100):
        query = f'''
        SELECT "heart_rate"
        FROM "vitals"
        WHERE "patient_id" = '{patient_id}'
        ORDER BY time DESC
        LIMIT {limit}
        '''
        result = self.client.query(query)
        points = list(result.get_points())
        heart_rates = [point['heart_rate'] for point in reversed(points)]
        return heart_rates
    
    def write_heart_rate(self, patient_id: str, heart_rate: float):
        json_body = [
            {
                "measurement": "vitals",
                "tags": {
                    "patient_id": patient_id
                },
                "fields": {
                    "heart_rate": heart_rate
                }
            }
        ]
        self.client.write_points(json_body)


influx_handler = InfluxDBHandler(
    host=os.getenv("INFLUX_HOST", "localhost"),
    port=int(os.getenv("INFLUX_PORT", 8086)),
    database=os.getenv("INFLUX_DB", "medical_data"),
    username=os.getenv("INFLUX_USER", None),
    password=os.getenv("INFLUX_PASSWORD", None))