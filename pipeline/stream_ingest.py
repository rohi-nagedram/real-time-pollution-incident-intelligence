"""
Streaming Data Ingestion (Simulated)

This simulates a real-time pollution data stream.
No APIs are used to ensure reliability during evaluation.
"""

import time

def pollution_stream():
    """
    Yields pollution readings one-by-one,
    mimicking real-time sensor behavior.
    """
    readings = [
        {"city": "Delhi", "value": 85,  "timestamp": "10:00"},
        {"city": "Delhi", "value": 140, "timestamp": "10:05"},
        {"city": "Delhi", "value": 95,  "timestamp": "10:10"},
        {"city": "Delhi", "value": 320, "timestamp": "10:15"},
    ]

    for reading in readings:
        yield reading
        time.sleep(1)  # simulate streaming delay
