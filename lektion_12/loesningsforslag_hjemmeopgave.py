import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.frankfurter.dev/v2/rates"

params = {
    "from": "2025-01-01",
    "to": "2025-12-31",
    "base": "USD",
    "quotes": "DKK"
}

response = requests.get(url, params=params)
data = response.json()

# Omdan til DataFrame
df = pd.DataFrame(data)

# Konverter dato til datetime
df["date"] = pd.to_datetime(df["date"])

# Sorter efter dato
df = df.sort_values("date")

# Tegn graf
plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["rate"])
plt.title("USD-kurs i DKK")
plt.xlabel("Dato")
plt.ylabel("DKK pr. USD")
plt.grid(True)
plt.tight_layout()
plt.show()