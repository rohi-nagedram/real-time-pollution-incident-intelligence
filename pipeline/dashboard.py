# Console-based live dashboard for pollution incidents

from stream_ingest import pollution_stream
from run_pipeline import detect_incident

def run_dashboard():
    print("\nLIVE POLLUTION DASHBOARD")
    print("=" * 50)
    print("City | Pollutant | Value | Status")
    print("=" * 50)

    for reading in pollution_stream():
        status = detect_incident(reading)
        print(
            f"{reading.city} | "
            f"{reading.pollutant} | "
            f"{reading.value}{reading.unit} | "
            f"{status}"
        )

if __name__ == "__main__":
    run_dashboard()
