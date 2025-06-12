# Innovation-Technology

This repository contains small experimental code snippets.

## Sensor-Agent

`sensor_agent.py` liest Sensordaten aus einer CSV-Datei und gibt Handlungsempfehlungen aus. Optional kann eine zweite CSV-Datei mit Optimalwerten übergeben werden.

### Beispiel

1. Erstelle eine CSV-Datei `sensor_data.csv` mit den Spalten `temperature`, `humidity` und `light`.
2. Füge Messwerte hinzu, z.B.:

```
temperature,humidity,light
22.5,45,500
26.0,65,900
```

3. Optional kannst du eine Datei `optimal_data.csv` anlegen, die die Idealwerte enthält:

```
temperature,humidity,light
21.0,50,600
```

4. Führe den Agenten mit Python aus:

```
python sensor_agent.py sensor_data.csv optimal_data.csv
```

Der Agent nimmt jeweils die letzte Zeile der angegebenen CSV-Dateien und gibt passende Empfehlungen aus.
