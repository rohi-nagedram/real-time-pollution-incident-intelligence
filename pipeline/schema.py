"""
Conceptual schema for pollution readings.

Defines the structure expected for each data record
entering the real-time pipeline.
"""

class PollutionReading:
    def __init__(self, city, pollutant, value, unit, timestamp):
        self.city = city
        self.pollutant = pollutant
        self.value = value
        self.unit = unit
        self.timestamp = timestamp
