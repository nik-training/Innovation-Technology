import csv
import sys
from typing import Dict, List


def load_latest_row(csv_path: str) -> Dict[str, float]:
    """Load the last row from a CSV file as a dictionary."""
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        rows: List[Dict[str, str]] = list(reader)
        if not rows:
            raise ValueError("CSV file is empty")
        latest_row = rows[-1]
        return {k: float(v) for k, v in latest_row.items()}


def make_recommendations(data: Dict[str, float]) -> List[str]:
    """Return a list of textual recommendations based on sensor readings."""
    recs: List[str] = []

    temp = data.get("temperature")
    if temp is not None:
        if temp > 25:
            recs.append("Temperatur ist hoch. Kühlung empfohlen.")
        elif temp < 18:
            recs.append("Temperatur ist niedrig. Heizung empfohlen.")

    humidity = data.get("humidity")
    if humidity is not None:
        if humidity > 60:
            recs.append("Hohe Luftfeuchtigkeit. Lüften empfohlen.")
        elif humidity < 30:
            recs.append("Niedrige Luftfeuchtigkeit. Luftbefeuchter empfohlen.")

    light = data.get("light")
    if light is not None:
        if light < 300:
            recs.append("Lichtniveau niedrig. Beleuchtung einschalten.")
        elif light > 800:
            recs.append("Lichtniveau hoch. Abschattung in Erwägung ziehen.")

    if not recs:
        recs.append("Keine speziellen Empfehlungen.")
    return recs


def main(args: List[str]) -> None:
    if len(args) != 2:
        print("Usage: python sensor_agent.py <sensor_data.csv>")
        sys.exit(1)

    csv_path = args[1]
    try:
        data = load_latest_row(csv_path)
    except Exception as exc:
        print(f"Fehler beim Laden der Daten: {exc}")
        sys.exit(1)

    recs = make_recommendations(data)
    print("Empfehlungen basierend auf den letzten Messwerten:")
    for rec in recs:
        print("-", rec)


if __name__ == "__main__":
    main(sys.argv)
