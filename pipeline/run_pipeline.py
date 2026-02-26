"""
Real-Time Incident Detection Logic.

Processes pollution readings as a stream and flags
dangerous air quality conditions immediately.
"""

from stream_ingest import pollution_stream

PM25_THRESHOLD = 150  # µg/m³

def detect_incident(reading):
    if reading.value > PM25_THRESHOLD:
        return "INCIDENT: UNSAFE AIR"
    return "NORMAL"

def run_pipeline():
    for reading in pollution_stream():
        status = detect_incident(reading)
        print(
            reading.city,
            reading.pollutant,
            reading.value,
            reading.unit,
            reading.timestamp,
            status
        )

# Conceptual entry point
run_pipeline()
