"""
Pipeline Runner

Connects streaming input to incident detection.
This represents the full real-time decision pipeline.
"""

from stream_ingest import pollution_stream
from incident_detector import PollutionIncidentDetector

def run():
    detector = PollutionIncidentDetector()

    for reading in pollution_stream():
        result = detector.evaluate(reading)
        print(result)

if __name__ == "__main__":
    run()
