# Innovation-Technology

This repository contains small experimental code snippets.

## Sensor-Agent

`sensor_agent.py` liest Sensordaten aus einer CSV-Datei und gibt einfache Handlungsempfehlungen basierend auf Temperatur, Luftfeuchtigkeit und Lichtniveau aus.

### Beispiel

1. Erstelle eine CSV-Datei `sensor_data.csv` mit den Spalten `temperature`, `humidity` und `light`.
2. Füge Messwerte hinzu, z.B.:

```
temperature,humidity,light
22.5,45,500
26.0,65,900
```

3. Führe den Agenten mit Python aus:

```
python sensor_agent.py sensor_data.csv
```

Der Agent nimmt die letzte Zeile der Datei und gibt passende Empfehlungen aus.
