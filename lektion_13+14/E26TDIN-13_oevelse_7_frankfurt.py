import requests


# API-kald
response = requests.get(
    "https://api.frankfurter.dev/v2/rates",
    params={
        "from"   : "2026-09-01",
        "to"     : "2026-10-21",
        "base"   : "DKK",
        "quotes" : "NOK"
    },
    headers={ "User-Agent": "API-Kursus-EAAA" }
)

response.raise_for_status()

