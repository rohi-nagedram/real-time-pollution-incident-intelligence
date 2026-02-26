"""
Incident Detection Logic

This module contains the core decision-making logic.
It converts raw PM2.5 readings into actionable incidents.
"""

PM25_SAFE_THRESHOLD = 100  # µg/m³ (configurable)

class PollutionIncidentDetector:
    def __init__(self, threshold=PM25_SAFE_THRESHOLD):
        self.threshold = threshold

    def evaluate(self, reading):
        """
        Decide whether a pollution reading is safe or unsafe.

        reading: dict with keys [city, value, timestamp]
        """
        if reading["value"] > self.threshold:
            return {
                "city": reading["city"],
                "status": "INCIDENT",
                "reason": "PM2.5 above safe limit",
                "value": reading["value"],
                "timestamp": reading["timestamp"],
            }

        return {
            "city": reading["city"],
            "status": "NORMAL",
            "value": reading["value"],
            "timestamp": reading["timestamp"],
        }
