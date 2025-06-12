import csv
import sys
from typing import Dict, List, Optional


def load_latest_row(csv_path: str) -> Dict[str, float]:
    """Load the last row from a CSV file as a dictionary."""
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        rows: List[Dict[str, str]] = list(reader)
        if not rows:
            raise ValueError("CSV file is empty")
        latest_row = rows[-1]
        return {k: float(v) for k, v in latest_row.items()}


def make_recommendations(data: Dict[str, float], optimal: Optional[Dict[str, float]] = None) -> List[str]:
    """Return a list of textual recommendations based on sensor readings.

    If ``optimal`` is provided, each sensor value is compared against the
    corresponding optimal value. Otherwise, simple threshold-based rules are
    used.
    """

    recs: List[str] = []

    if optimal:
        for key, val in data.items():
            opt_val = optimal.get(key)
            if opt_val is None:
                continue
            if val > opt_val:
                recs.append(
                    f"{key.capitalize()} über Optimalwert ({val} > {opt_val}). Wert senken."
                )
            elif val < opt_val:
                recs.append(
                    f"{key.capitalize()} unter Optimalwert ({val} < {opt_val}). Wert erhöhen."
                )
    else:
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
        recs.append("Alle Werte im optimalen Bereich.")
    return recs


def main(args: List[str]) -> None:
    if len(args) not in (2, 3):
        print("Usage: python sensor_agent.py <sensor_data.csv> [optimal_data.csv]")
        sys.exit(1)

    data_path = args[1]
    optimal_path = args[2] if len(args) == 3 else None

    try:
        data = load_latest_row(data_path)
    except Exception as exc:
        print(f"Fehler beim Laden der Daten: {exc}")
        sys.exit(1)

    optimal = None
    if optimal_path:
        try:
            optimal = load_latest_row(optimal_path)
        except Exception as exc:
            print(f"Fehler beim Laden der Optimaldaten: {exc}")
            sys.exit(1)

    recs = make_recommendations(data, optimal)
    print("Empfehlungen basierend auf den letzten Messwerten:")
    for rec in recs:
        print("-", rec)


if __name__ == "__main__":
    main(sys.argv)
