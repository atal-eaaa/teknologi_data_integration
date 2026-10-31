import requests
import pandas as pd
import matplotlib.pyplot as plt

# API-endpoint for Forecasts_5Min
url = "https://api.energidataservice.dk/dataset/Forecasts_5Min"

# Parametre – vi henter 1000 rækker, kun Offshore wind forecast
params = {
    "limit": 1000,
    "filter": '{"ForecastType": "Offshore Wind", "PriceArea": "DK1" }',
    "sort": "Minutes5UTC desc"
}

# Hent data fra Energidataservice
response = requests.get(url, params=params)
data = response.json()

# Konverter til DataFrame
df = pd.DataFrame(data["records"])
df = df.sort_values(by = "Minutes5UTC", ascending=True )

# Plot – tid vs. MW forecast
plt.figure(figsize=(10, 6))
plt.scatter(df["Minutes5UTC"], df["ForecastDayAhead"], alpha=1, s=1)
plt.title("Offshore Wind Forecast (10 døgn)")
plt.xlabel("Tid (UTC)")
plt.ylabel("Forecast [MW]")
plt.xticks(df["Minutes5UTC"][::288], rotation=45)
plt.tight_layout()
plt.show()
