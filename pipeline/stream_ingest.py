"""
Conceptual streaming ingestion.

Represents how pollution readings would arrive continuously
from sensors or data providers in a real system.
"""

from schema import PollutionReading

def pollution_stream():
    yield PollutionReading("Delhi", "PM2.5", 95, "µg/m³", "10:00")
    yield PollutionReading("Delhi", "PM2.5", 180, "µg/m³", "10:05")
    yield PollutionReading("Delhi", "PM2.5", 320, "µg/m³", "10:10")
